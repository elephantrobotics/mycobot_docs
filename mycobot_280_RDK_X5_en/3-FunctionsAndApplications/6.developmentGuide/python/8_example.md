# Demonstration code 

The following are various use cases and operation result videos. You can copy the code for use or modification (the robot arm model used in the following cases is MyCobot280RDKX5 280. The parameters of different series of robot arms are different. Please pay attention to the modification).

**Note:** The corresponding baud rates of various devices are different. Please refer to the information to understand their baud rates when using them. myCobot RDK X5 serial is `/dev/ttyS1`.

## 1 Control RGB light board

```python
from pymycobot import MyCobot280RDKX5

import time
#The above needs to be written at the beginning of the code, which means importing the project package

# MyCobot280RDKX5 class initialization requires two parameters: serial port and baud rate
mc = MyCobot280RDKX5("/dev/ttyS1", 1000000)

i = 7
# Loop 7 times
while i > 0:
mc.set_color(0,0,255) #Blue light on
time.sleep(2) #Wait 2 seconds
mc.set_color(255,0,0) #Red light on
time.sleep(2) #Wait 2 seconds
mc.set_color(0,255,0) #Green light on
time.sleep(2) #Wait 2 seconds
i -= 1
```

## 2 Control the machine to return to the origin

```python
from pymycobot import MyCobot280RDKX5
# MyCobot280RDKX5 class initialization requires two parameters: serial and baud rate

# Initialize a MyCobot280RDKX5 object
# The following is the object code for PI version
mc = MyCobot280RDKX5("/dev/ttyS1", 1000000)

# Check if the robot can be programmed

if mc.is_controller_connected() != 1:

print("Please connect the robot correctly to write the program")

exit(0)

# Fine-tune the robot to ensure that all the ports are aligned

# The alignment of the robot port is the standard. This is just an example

mc.send_angles([0, 0, 0, 0, 0, 0], 30)

# Calibrate the position at this time. The calibrated angle position is [0,0,0,0,0,0] and the potential value is [2048,2048,2048,2048,2048,2048]

# This for loop is equivalent to the set_gripper_ini() method

#for i in range(1, 7):

#mc.set_servo_calibration(i)
```

## 3 Single joint movement

```python
from pymycobot import MyCobot280RDKX5
import time

# The MyCobot280RDKX5 class requires two parameters to be initialized: serial and baud rate
# Create object code for PI version
mc=MyCobot280RDKX5('/dev/ttyS1',1000000)

# Robot arm recovery
mc.send_angles([0, 0, 0, 0, 0, 0], 40)
time.sleep(3)

# Control joint 3 to move 70°
mc.send_angle(Angle.J3.value,70,40)
time.sleep(3)

# Control joint 4 to move -70°
mc.send_angle(Angle.J4.value,-70,40)
time.sleep(3)

# Control joint 1 to move 90°
mc.send_angle(Angle.J1.value,90,40)
time.sleep(3)

# Control joint 5 to move -90°
mc.send_angle(Angle.J5.value,-90,40)
time.sleep(3)

# Control joint 5 to move 90°
mc.send_angle(Angle.J5.value,90,40)
time.sleep(3)
```



## 4 Multi-joint exercise

```python
import time
from pymycobot import MyCobot280RDKX5
# The MyCobot280RDKX5 class requires two parameters to be initialized: serial and baud rate
# Initialize a MyCobot280RDKX5 object
# 280-PI version object code
mc=MyCobot280RDKX5('/dev/ttyS1',1000000)
# Robot arm reset to zero
mc.send_angles([0,0,0,0,0,0],50)
time.sleep(2.5)
# Control the different angles of rotation of multiple joints
mc.send_angles([90,45,-90,90,-90,90],50)
time.sleep(2.5)
# Robot arm reset to zero
mc.send_angles([0,0,0,0,0,0],50)
time.sleep(2.5)
# Control the different angles of rotation of multiple joints
mc.send_angles([-90,-45,90,-90,90,-90],50)
time.sleep(2.5)

```

##  5 Control the robot arm to swing left and right

```python
from pymycobot import MyCobot280RDKX5
import time

# PI version
mc = MyCobot280RDKX5("/dev/ttyS1", 1000000)
# Get the coordinates of the current position
angle_datas = mc.get_angles()
print(angle_datas)

# Use a sequence to pass coordinate parameters to move the robot to the specified position
mc.send_angles([0, 0, 0, 0, 0, 0], 50)
print(mc.is_paused())
# Set the waiting time to ensure that the robot has reached the specified position
# while not mc.is_paused():
time.sleep(2.5)

# Move joint 1 to position 90
mc.send_angle(Angle.J1.value, 90, 50)

# Set the waiting time to ensure that the robot has reached the specified position
time.sleep(2)

# Set the number of loops
num = 5

# Let the robot swing left and right
while num > 0:
    # Move joint 2 to position 50
    mc.send_angle(2, 50, 50)
    # Set the waiting time to ensure that the robot has reached the specified position
    time.sleep(1.5)
    # Move joint 2 to position -50
    mc.send_angle(2, -50, 50)
    # Set the waiting time to ensure that the robot has reached the specified position
    time.sleep(1.5)
    num -= 1
# Retract the robot arm. You can swing the robot arm manually, and then use the get_angles() function to get the coordinate sequence.
# Use this function to make the robot arm reach the position you want.
mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)

# Set the waiting time to ensure that the robot arm has reached the specified position
time.sleep(2.5)
# Relax the robot arm and swing it manually
mc.release_all_servos()

```

## 6 Gripper control

```python
from pymycobot import MyCobot280RDKX5
import time

def gripper_test(mc):
    print("Start check IO part of api\n")
    # Check if the gripper is moving
    flag = mc.is_gripper_moving()
    print("Is gripper moving: {}".format(flag))
    time.sleep(1)

    # Set the current position to (2048).
    # Use it when you are sure you need it.
    # Gripper has been initialized for a long time. Generally, there
    # is no need to change the method.
    # mc.set_gripper_ini()
    # Set joint point 1 to rotate to position 2048, speed 20
    mc.set_encoder(1, 2048, 20)
    time.sleep(2)
    # Set six joint positions and let the robot arm rotate to the position at a speed of 20

    mc.set_encoders([1024, 1024, 1024, 1024, 1024, 1024], 20)
    # mc.set_encoders([2048, 2900, 2048, 2048, 2048, 2048], 20)
    # mc.set_encoders([2048, 3000,3000, 3000, 2048, 2048], 50)
    time.sleep(3)
    # Get the position information of joint point 1
    print(mc.get_encoder(1))
    # Set the gripper to rotate to the position of 2048
    mc.set_encoder(7, 2048, 20)
    time.sleep(3)
    # Set the gripper to rotate to the position of 1300
    mc.set_encoder(7, 1300, 20)
    time.sleep(3)

    # Let the gripper reach the state of 2048 at a speed of 70. 2048 will report an error, so change it to 255
    mc.set_gripper_value(255, 70, 20)
    time.sleep(3)
    # Let the gripper reach the state of 1500 at a speed of 70. 1500 will report an error, so change it to 255
    mc.set_gripper_value(255, 70)
    time.sleep(3)

    num=5
    while num>0:
        # Set the state of the gripper to open the claws quickly at a speed of 70
        mc.set_gripper_state(0, 70)
        time.sleep(3)
        # Set the state of the gripper to close the claws quickly at a speed of 70
        mc.set_gripper_state(1, 70)
        time.sleep(3)
        num-=1

    # Get the value of the gripper
    print("")
    print(mc.get_gripper_value())
    # mc.release_all_servos()

if __name__ == "__main__":
# MyCobot280RDKX5 class initialization requires two parameters: serial and baud rate

# Initialize a MyCobot280RDKX5 object
mc = MyCobot280RDKX5('/dev/ttyS1', 1000000)
# Move it to zero position
mc.set_encoders([2048, 2048, 2048, 2048, 2048, 2048], 20)
time.sleep(3)
gripper_test(mc)
```

## 7 Suction pump control


```python
from pymycobot import MyCobot280RDKX5
import time
import Hobot.GPIO as GPIO

# The MyCobot280RDKX5 class requires two parameters to initialize: serial and baud rate

# Initialize a MyCobot280RDKX5 object
# The following is the object code for the PI version
mc = MyCobot280RDKX5('/dev/ttyS1',1000000)
# The position of the robot arm movement
angles = [
[92.9, -10.1, -60, 5.8, -2.02, -37.7],
[92.9, -53.7, -83.05, 50.09, -0.43, -38.75],
[92.9, -10.1, -87.27, 5.8, -2.02, -37.7]
]

# Initialization
GPIO.setmode(GPIO.BCM)
# Pin 20/21 controls the solenoid valve and the exhaust valve respectively
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
# Turn on the suction pump
def pump_on():
    # Open the solenoid valve
    GPIO.output(20,0)

# Stop the suction pump
def pump_off():
    # Close the solenoid valve
    GPIO.output(20,1)
    time.sleep(0.05)
    # Open the exhaust valve
    GPIO.output(21,0)
    time.sleep(1)
    GPIO.output(21,1)
    time.sleep(0.05)

# Robot arm recovery
mc.send_angles([0, 0, 0, 0, 0, 0], 30)
time.sleep(3)

# Turn on the suction pump
pump_on()
mc.send_angles(angles[2], 30)
time.sleep(2)

# Suction small objects
mc.send_angles(angles[1], 30) 
time.sleep(2) 
mc.send_angles(angles[0], 30) 
time.sleep(2)
mc.send_angles(angles[1], 30)
time.sleep(2) 
#Turn off the suction pump 
pump_off() 
mc.send_angles(angles[0], 40) 
time.sleep(1.5)
```

