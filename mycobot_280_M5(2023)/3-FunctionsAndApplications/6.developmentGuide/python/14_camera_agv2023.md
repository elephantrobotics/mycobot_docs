# myAGV JN 2023 摄像头识别aruco码

## 环境搭建

```
JetPack的版本                   "7.2"
Python的版本                    "3.8.10"
opencv-python的版本             "4.6.0.66"
opencv-contrib-python的版本     "4.6.0.66"
相机型号                        "IMX219-160"
```

## 查看是否摄像头正常

终端输入下面指令查看摄像头画面，能看到摄像头的画面，显示到画面说明摄像头功能正常

```bash
nvgstcapture
```

## 使用opencv驱动 CSI摄像头

1. 利用Gstreamer通道打开摄像头，安装Gstreamer

```bash
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo apt-get update
sudo apt-get install gstreamer1.0-tools gstreamer1.0-alsa gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev libgstreamer-plugins-bad1.0-dev
```

2. 新建一个python脚本

```
sudo vim opencv_aruco.py
```

3. 编写python使用opencv识别aruco码

```python
import cv2
import cv2.aruco as aruco

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def show_camera():
    window_title = "CSI Camera"

    print(gstreamer_pipeline(flip_method=0))
    video_capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, frame = video_capture.read()
                aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50)
                corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict)
                if ids is not None:
                    aruco.drawDetectedMarkers(frame, corners, ids)
                    for i in range(len(ids)):
                        cv2.putText(frame, str(ids[i][0]), (corners[i][0, 0, 0], corners[i][0, 0, 1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    cv2.imshow(window_title, frame)
                else:
                    break 
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    show_camera()
```

4. 运行程序

编辑好之后按Esc切换到命令模式，然后输入  :wq   回车就自动保存完成了，然后输入``sudo python3 opencv_aruco.py``  运行程序

![JN_camera](../resourse/20-myAgv2023/JN/JN_camera.png)

# myAGV Pi 2023 摄像头识别aruco码

## 环境搭建

```
Python的版本                    "3.8.10"
opencv-python的版本             "4.6.0.66"
opencv-contrib-python的版本     "4.6.0.66"
相机型号                        "Raspberry Pi Camera Rev1.3"
```

## 查看是否摄像头正常

终端输入下面指令查看摄像头画面，能看到摄像头的画面，显示到画面说明摄像头功能正常

```bash
sudo mplayer tv://
```


## 使用opencv驱动摄像头识别aruco码

1. 新建一个python脚本

```
sudo vim opencv_aruco.py
```

2. 编写python使用opencv识别aruco码

摄像头的内参矩阵和畸变系数可详情请查看 [2.8.2 知识准备章节](../13-AdvancedKit/13.1人工智能/2-知识准备.md) 中的**校准摄像头**部分内容。

```python
import cv2
import numpy as np

# 创建ArUco字典
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)

# 创建ArUco检测器
aruco_params = cv2.aruco.DetectorParameters()

# 打开摄像头
cap = cv2.VideoCapture(0)

# 摄像头的内参矩阵
camera_matrix = np.array([
[781.33379113, 0., 347.53500524],
[0., 783.79074192, 246.67627253],
[0., 0., 1.]])

# 摄像头的畸变系数
dist_coeffs = np.array(([[3.41360787e-01, -2.52114260e+00, -1.28012469e-03,  6.70503562e-03,
             2.57018000e+00]]))
while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 检测ArUco码
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)
    
    if ids is not None:
        # 绘制检测到的ArUco码
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # 估计ArUco码的位姿
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, camera_matrix, dist_coeffs)

        for i in range(len(ids)):
            # 在检测到的ArUco码上绘制坐标轴
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], 0.1)

    # 显示帧
    cv2.imshow('ArUco Detection', frame)

    # 按下ESC键退出循环
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 关闭摄像头和窗口
cap.release()
cv2.destroyAllWindows()
```

3. 运行程序

编辑好之后按Esc切换到命令模式，然后输入  :wq   回车就自动保存完成了，然后输入``sudo python3 opencv_aruco.py``  运行程序

![PI_camera](../resourse/20-myAgv2023/PI/PI_camera.png)