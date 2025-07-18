# Robot gripper carrying wood block example

## 1 Equipment description

myCobot 280 Arduino + MEGA 2560 development board + myCobot adaptive gripper

## 2 Functional description

The robot will use the gripper to carry the wood block from point A to point B. The LED light board will light up after the grip is successful

## 3 Hardware installation

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
<source src="./img/MEGA2560_Hardware_Installation.mp4" type='video/mp4' >
</video>

## 4 Gripper test

Run the following program, the gripper will repeat closing and opening twice

```python
from pymycobot import MyCobot280,utils
import time

arm=MyCobot280(utils.get_port_list()[0], 115200) # The baud rate is 115200 by default, and some boards are 1000000, please modify according to the actual situation
time.sleep(2)

for i in range(2):
arm.set_gripper_state(0,100)
time.sleep(2)
arm.set_gripper_state(1,100)
time.sleep(2)
```

## 5 Principle description

Use MEGA 2560 development board to control a MyCobot 280 Arduino robot arm, and complete the following operation process with the gripper:

1. **Initialization and return to zero:**

   - Connect to the serial port;

   - Move to the initial position;

   - Open the gripper (make sure nothing is clamped);

2. **Grasping phase (point A):**

   - Move to point A Point coordinates;

   - The gripper closes and grabs the block;

   - Return to the initial position;

   - The yellow light turns on (indicating successful grabbing);

3. **Transport and release (point B):**

   - The robot moves to the top of point B;

   - Descends to the coordinates of point B;

   - The gripper opens and releases the block;

   - Returns to the top of point B and then returns to the initial position;

- The green light turns on (indicating successful transport).

## 6 Composite Application

```python
import time
from pymycobot import * # Import MyCobot control library
from pymycobot.utils import get_port_list # Get serial port list tool

# Get all available serial ports
plist = get_port_list()

# Initialize MyCobot 280 robot arm, connect serial port, baud rate is 115200, some boards are 1000000, please modify according to the actual situation
mc = MyCobot280(plist[0], 115200)
time.sleep(0.5)

# Set common variables
speed = 60 # Movement speed
wait_time = 2.5 # Waiting time (seconds)
go_home = [0, 0, 0, 0, 0, 0] # Robot arm home position (joint angle)

# Initial posture angle (avoid object area)
init_pos = [5.44, -13.88, -73.82, 3.42, 0.43, -30.84]

# A point coordinates (grasp point)
A_coords = [203.6, -46.9, 100.6, -176.88, -1.29, -55.39]

# B point upper joint angle
B_up_angles = [89.12, -15.55, -75.32, 2.02, 0.87, -30.23]

# B point coordinates (release point)
B_coords = [64.1, 198.2, 112.4, -177.53, -0.82, 29.78]

# Open the gripper (open)
def gripper_on():
    mc.set_gripper_state(0, 100) # 0 =Open
    time.sleep(0.05)

# Close the gripper (clamp)
def gripper_off():
    mc.set_gripper_state(1, 100) # 1 means closed
    time.sleep(0.05)

# Main process function
def main():
    # Return to the initial zero position
    mc.send_angles(go_home, speed)
    time.sleep(wait_time)

    # Move to the initial safe position
    mc.send_angles(init_pos, speed)
    time.sleep(wait_time)

    # Open the gripper and prepare to grab
    gripper_on()

    # Move to point A to grab the wood block
    mc.send_coords(A_coords, speed, 1)
    time.sleep(wait_time)

    # Clamp the wood block
    gripper_off()

    # Return to the initial position
    mc.send_angles(init_pos, speed)
    time.sleep(wait_time)

    # Grasp successfully, turn on the yellow light as a prompt
    mc.set_color(255, 255, 0) # Yellow light (R=255, G=255, B=0)

    # Move to the top of point B to prepare for placement
    mc.send_angles(B_up_angles, speed)
    time.sleep(wait_time)

    # Drop to the coordinates of point B for placement
    mc.send_coords(B_coords, speed, 1)
    time.sleep(2)

    # Release the gripper and release the block
    gripper_on()

    # Lift the robot arm back to the top of point B
    mc.send_angles(B_up_angles, speed)
    time.sleep(wait_time)

    # Return to the initial position
    mc.send_angles(init_pos, speed)
    time.sleep(wait_time)
    # Transport completed, turn on the green light as a reminder
    mc.set_color(0, 255, 0) # Green light (R=0, G=255, B=0)

if __name__ == '__main__':
    main()

```

## 7 Effect display

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/MEGA2560_Effect.mp4" type='video/mp4' >
</video>