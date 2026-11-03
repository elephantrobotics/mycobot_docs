# yolov8 Item Classification Case

## 1 Equipment Description

myCobot 280 Arduino + Jetson Xavier NX Development Board + myCobot Vertical Suction Pump 2.0 + myCobot Camera Module

## 2 Hardware Installation

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/JetsonXavierNX_Hardware_Installation.mp4" type='video/mp4' >
</video>

## 3 Principle description

This program combines:

- YOLOv8 target recognition model (classification of objects such as "apple", "banana")

- MyCobot robotic arm (with suction pump)

- Camera image acquisition

- GPIO control of suction pump solenoid valve

The implementation process is as follows:

```bash
Camera captures images → YOLOv8 recognizes objects → Gets pixel coordinates of the center point of the object → Converts pixel coordinates to real robotic arm coordinates → Controls the robotic arm to move and absorb → Moves to classification delivery points A/B/C/D → Releases the object → Returns to the initial position
```

The start and stop of the suction pump is controlled by Jetson GPIO, and the control pin is BOARD 16.

## 4 Program running

**YOLOv8 model file download:** [best.pt](https://download.elephantrobotics.com/software/drivers/best.pt)

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
        self.model = YOLO(model_path)  # Loading the YOLOv8 model

    def infer(self, frame):
        results = self.model(frame)[0]  # Performing Reasoning on Images
        result_image = frame.copy()
        rect_list = []
        classnames = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
            w, h = x2 - x1, y2 - y1
            label = int(box.cls[0]) # Get category index
            conf = float(box.conf[0]) # Get confidence
            name = self.model.names[label] # Get category name


            # Add rectangles and category labels to images
            cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(result_image, f'{name} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            rect_list.append(((x1, y1), w, h, name, conf))
            classnames.append(name)

        return result_image, rect_list, classnames

class ElephantMotionControl:
    def __init__(self):
        self.task_completed = True
        self.mc = MyCobot280('/dev/ttyTHS0', 1000000)  # Initialize the robot arm
        time.sleep(1.5)

        self.cam_coords = [197.8, -47.2, 236.2, -174.25, -0.66, -49.3]  # The center point coordinates of the camera's view
        self.init_pos = [4.83, -12.21, -60.9, -10.98, 3.51, -39.81]

        self.pos_A = [62.4, -12.65, -64.95, -15.82, -1.14, -10.81]  # Apple delivery point
        self.pos_B = [39.55, -49.3, -21.79, -15.29, 5.36, -10.81]   # Orange delivery point
        self.pos_C = [-25.13, -39.28, -27.42, -33.75, -2.19, -9.05]  # Banana drop point
        self.pos_D = [-16.61, -49.65, -27.42, -5.09, 1.31, -9.05]  # Grape placement

        self.speed = 50
        self.coords_speed = 80

        self.x_offset = 66
        self.y_offset = -65

        self.last_task_done_time = time.time()

        if self.mc.get_fresh_mode() == 1:
            self.mc.set_fresh_mode(0)

        self.mc.send_angles(self.init_pos, self.speed)  # Return to the initial position
        self.check_position(self.init_pos, 0)

    def check_position(self, data, ids, max_same_data_count=50):
        """Block and wait until the robot reaches the specified position (preventing the next step from being executed early)"""
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


    # Start the suction pump
    def pump_on(self):
        GPIO.output(16, 0)  # Start the suction pump (low level is effective)
        time.sleep(0.05)

    # Stop the suction pump
    def pump_off(self):
        GPIO.output(16, 1)  # Stop the suction pump
        time.sleep(0.05)

    def convert_to_real_coordinates(self, x_pixel, y_pixel, target_id):
        if not self.task_completed:
            return
        self.task_completed = False
        # Convert pixel coordinates to actual coordinate offset (unit: mm）
        x = round(y_pixel * (60 / 170), 2)
        y = round(-x_pixel * (60 / 170), 2)

        # Update target coordinates (where the robot will move to for grabbing)
        self.cam_coords[0] = 198.4 + x - self.x_offset
        self.cam_coords[1] = -46.3 - y + self.y_offset
        self.cam_coords[2] = 170  # Z height is initially set to safe height

        print(f"移动到新的坐标: {self.cam_coords} id--------->: {target_id}")

        def move_robot():
            try:
                self.mc.send_coords(self.cam_coords, self.coords_speed, 1)  # Drop onto the object
                self.check_position(self.cam_coords, 1, 20)

                self.cam_coords[2] = 120
                self.mc.send_coords(self.cam_coords, self.coords_speed, 1)  # Come down
                self.check_position(self.cam_coords, 1, 20)

                self.pump_on()  # Suction Object

                self.cam_coords[2] = 230
                self.mc.send_coords(self.cam_coords, self.coords_speed, 1)  # Lifting an object
                self.check_position(self.cam_coords, 1, 20)

                # Move to target position (A/B/C/D)
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

                self.pump_off()  # release pump

                self.mc.send_angles(self.init_pos, self.speed)  # Return to the initial position
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

                # Item classification: apple/orange/banana1/grape → corresponding drop-off point
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
                # Send coordinates to the robot control module to move
                motion_control.convert_to_real_coordinates(center_x, center_y, target_id)
                break  # Process only one target at a time

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

## 5 Effect display

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/JetsonXavierNX_Effect.mp4" type='video/mp4' >
</video>

