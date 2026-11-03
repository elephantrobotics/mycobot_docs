# 机器人 ROS STAG码视觉跟踪

## 1 设备说明

myCobot 280 Arduino + 树莓派4B开发板 + myCobot 摄像头模组

## 2 硬件安装

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/JetsonXavierNX_Effect.mp4" type='video/mp4' >
</video>

## 3 原理说明

该程序结合了：

- YOLOv8 目标识别模型（分类物体如“apple”、“banana”）

- MyCobot 机械臂（带吸泵）

- 摄像头图像采

- GPIO 控制吸泵电磁

实现流程如下：

```bash
摄像头采集图像 → YOLOv8识别物体 → 获取物体中心点像素坐标 → 将像素坐标转换为真实机械臂坐标 → 控制机械臂移动并吸取 → 移动至分类投放点A/B/C/D → 释放物体 → 回初始位置
```

吸泵的启停通过 Jetson GPIO 控制，控制引脚为 BOARD 16。

## 4 程序运行

**YOLOv8模型文件下载：** [best.pt](https://download.elephantrobotics.com/software/drivers/best.pt)

```python
import cv2
import time
import threading
import traceback
from ultralytics import YOLO
from pymycobot import MyCobot280
import Jetson.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

class ElephantDetection:
    def __init__(self, model_path):
        self.model = YOLO(model_path)  # 加载 YOLOv8 模型

    def infer(self, frame):
        results = self.model(frame)[0]  # 对图像进行推理
        result_image = frame.copy()
        rect_list = []
        classnames = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 获取边框坐标
            w, h = x2 - x1, y2 - y1
            label = int(box.cls[0])  # 获取类别索引
            conf = float(box.conf[0])  # 获取置信度
            name = self.model.names[label]  # 获取类别名称


            # 添加矩形框和类别标签到图像上
            cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(result_image, f'{name} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            rect_list.append(((x1, y1), w, h, name, conf))
            classnames.append(name)

        return result_image, rect_list, classnames

class ElephantMotionControl:
    def __init__(self):
        self.task_completed = True
        self.mc = MyCobot280('/dev/ttyTHS0', 1000000)  # 初始化机械臂
        time.sleep(1.5)

        self.cam_coords = [197.8, -47.2, 236.2, -174.25, -0.66, -49.3]  # 相机视角下的中心点坐标
        self.init_pos = [4.83, -12.21, -60.9, -10.98, 3.51, -39.81]

        self.pos_A = [62.4, -12.65, -64.95, -15.82, -1.14, -10.81]  # 苹果投放点
        self.pos_B = [39.55, -49.3, -21.79, -15.29, 5.36, -10.81]   # 橙子投放点
        self.pos_C = [-25.13, -39.28, -27.42, -33.75, -2.19, -9.05]  # 香蕉投放点
        self.pos_D = [-16.61, -49.65, -27.42, -5.09, 1.31, -9.05]  # 葡萄投放点

        self.speed = 50
        self.coords_speed = 80

        self.x_offset = 66
        self.y_offset = -65

        self.last_task_done_time = time.time()

        if self.mc.get_fresh_mode() == 1:
            self.mc.set_fresh_mode(0)

        self.mc.send_angles(self.init_pos, self.speed)  # 回到初始位置
        self.check_position(self.init_pos, 0)

    def check_position(self, data, ids, max_same_data_count=50):
        """阻塞等待直到机械臂到达指定位置（防止提前执行下一步）"""
        try:
            same_data_count = 0
            last_data = None
            while True:
                res = self.mc.is_in_position(data, ids)
                if data == last_data:
                    same_data_count += 1
                else:
                    same_data_count = 0
                last_data = data
                if res == 1 or same_data_count >= max_same_data_count:
                    break
                time.sleep(0.1)
        except Exception:
            print(traceback.format_exc())


    # 开启吸泵
    def pump_on(self):
        GPIO.output(16, 0)  # 开启吸泵（低电平有效）
        time.sleep(0.05)

    # 停止吸泵
    def pump_off(self):
        GPIO.output(16, 1)  # 关闭吸泵
        time.sleep(0.05)

    def convert_to_real_coordinates(self, x_pixel, y_pixel, target_id):
        if not self.task_completed:
            return
        self.task_completed = False
        # 将像素坐标换算为实际坐标偏移量（单位：mm）
        x = round(y_pixel * (60 / 170), 2)
        y = round(-x_pixel * (60 / 170), 2)

        # 更新目标坐标（机械臂将移动到这里进行抓取）
        self.cam_coords[0] = 198.4 + x - self.x_offset
        self.cam_coords[1] = -46.3 - y + self.y_offset
        self.cam_coords[2] = 170  # Z 高度初始为安全高度

        print(f"移动到新的坐标: {self.cam_coords} id--------->: {target_id}")

        def move_robot():
            try:
                self.mc.send_coords(self.cam_coords, self.coords_speed, 1)  # 降到物体上方
                self.check_position(self.cam_coords, 1, 20)

                self.cam_coords[2] = 120
                self.mc.send_coords(self.cam_coords, self.coords_speed, 1)  # 降下来
                self.check_position(self.cam_coords, 1, 20)

                self.pump_on()  # 吸取物体

                self.cam_coords[2] = 230
                self.mc.send_coords(self.cam_coords, self.coords_speed, 1)  # 抬起物体
                self.check_position(self.cam_coords, 1, 20)

                # 移动到目标位置（A/B/C/D）
                if target_id == 1:
                    self.mc.send_angles(self.pos_A, self.speed)
                    self.check_position(self.pos_A, 0)
                elif target_id == 2:
                    self.mc.send_angles(self.pos_B, self.speed)
                    self.check_position(self.pos_B, 0)
                elif target_id == 3:
                    self.mc.send_angles(self.pos_C, self.speed)
                    self.check_position(self.pos_C, 0)
                elif target_id == 4:
                    self.mc.send_angles(self.pos_D, self.speed)
                    self.check_position(self.pos_D, 0)

                self.pump_off()  # 释放

                self.mc.send_angles(self.init_pos, self.speed)  # 回到初始位
                self.check_position(self.init_pos, 0)
                self.last_task_done_time = time.time()
                self.task_completed = True
                self.cam_coords = None
                while self.cam_coords is None:
                    self.cam_coords = self.mc.get_coords()
            except Exception:
                print(traceback.format_exc())

        threading.Thread(target=move_robot).start()

def main():
    detector = ElephantDetection("best.pt")
    motion_control = ElephantMotionControl()
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    last_result_image = None

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        if motion_control.task_completed and time.time() - motion_control.last_task_done_time > 2.0:
            result_img, rects, classnames = detector.infer(frame)
            print(f"检测到 {len(rects)} 个目标，类别：{classnames}")

            for rect in rects:
                (x1, y1), w, h, label, conf = rect
                center_x = x1 + w // 2
                center_y = y1 + h // 2
                print(f"{label} @ ({center_x}, {center_y})")

                # 物品分类：apple/orange/banana1/grape → 对应投放点
                if label in ["apple"]:
                    target_id = 1
                elif label in ["orange"]:
                    target_id = 2
                elif label in ["banana1"]:
                    target_id = 3
                elif label in ["grape"]:
                    target_id = 4
                else:
                    continue
                # 发送坐标给机械臂控制模块进行移动
                motion_control.convert_to_real_coordinates(center_x, center_y, target_id)
                break  # 每次只处理一个目标

            last_result_image = result_img
            cv2.imshow("Result", result_img)
        else:
            if last_result_image is not None:
                cv2.imshow("Result", last_result_image)
            else:
                cv2.imshow("Result", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    
```

## 5 效果展示

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/JetsonXavierNX_Effect.mp4" type='video/mp4' >
</video>
