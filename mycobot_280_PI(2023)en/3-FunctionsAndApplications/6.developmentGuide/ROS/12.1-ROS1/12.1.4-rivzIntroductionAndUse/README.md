# A brief introduction and use of rviz

rviz is a 3D visualization platform in ROS. On the one hand, it can realize the graphical display of external information. On the other hand, it can also release control information to objects through rviz, thereby realizing the monitoring and control of robots.

## Introduction to the installation and interface of rviz

When installing ros, if you perform a complete installation, rviz has been installed, and you can try to run it directly; if it is not fully installed, you can install rviz separately:

```bash
# Ubuntu16.04
sudo apt-get install ros-kinetic-rviz
```
``` bash
# Ubuntu18.04
sudo apt-get install ros-melodic-rviz
```
```bash
# Ubuntu20.04
sudo apt-get install ros-noetic-rviz
```

After the installation is complete, please open a new terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>) and enter the following command:
```bash
roscore
```

Then open a new terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>) and enter the command to open rviz

```bash
rosrun rviz rviz
# or
rviz
```

Open rviz and the following interface will be displayed:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/rviz-1.png
width ="500" align = "center">

### Introduction to each area

+ On the left is the display list. A display is something that draws something in the 3D world and may have some options available in the display list.

+ On the top is the toolbar, which allows users to select multiple functions with various function keys

+ In the middle is the 3D view: it is the main screen that allows users to view various data in three dimensions. The background color, fixed frame, grid, etc. of the 3D view can be set in detail in the Global Options and Grid items displayed on the left.

+ Below is the time display area, including system time and ROS time.

+ On the right is the observation angle setting area, which can set different observation angles.

In this section, we will only give a rough introduction. If you want to know more details, you can go to the [User Guide](http://wiki.ros.org/rviz/UserGuide) to check it out.

## mycobot_ros installation and update

- **PI version (Ubuntu 20.04): **

`mycobot_ros` is a ROS package launched by ElephantRobotics that is compatible with various types of desktop robotic arms.

Project address: https://github.com/elephantrobotics/mycobot_ros

The official default workspace is `catkin_ws`.

Click the `ROS1 Shell` icon on the desktop or the corresponding icon in the bar below the desktop to open the ROS1 environment terminal:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/1040.jpg
align = "center">

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/1041.jpg
align = "center">

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/rviz-4.png
align = "center">

Then enter the following command:

```bash
cd ~/catkin_ws/src # Enter the src folder in the workspace
# Clone the code on github
git clone https://github.com/elephantrobotics/mycobot_ros.git
cd .. # Return to the workspace
catkin_make # Build the code in the workspace
source devel/setup.bash # Add environment variables
```

Note: If the `mycobot_ros` folder already exists in the `/home/er/catkin_ws/src (equivalent to ~/catkin_ws/src)` directory, you need to delete the original `mycobot_ros` first, and then execute the above command. Among them, `er` in the directory path is the user name of the virtual machine. If it is inconsistent, please modify it.

## Simple use

**Start through the launch file**

This example is based on the premise that you have completed [Environment Construction](../12.1.2-Environment Construction.md) and successfully copied the company's code from GitHub.

Open a console terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)
Enter the following command to **ROS environment configuration**.

```bash
cd ~/catkin_ws/
source devel/setup.bash
```

Enter again:

- mycobot 280-Pi version:

```bash
roslaunch mycobot_280pi test.launch
```

Open rviz and get the following result:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/rviz-5.png
width ="500" align = "center">

If you want to learn more about rviz, you can go to the [official document](http://wiki.ros.org/rviz) to view it

# 280 series rviz user guide

## Robot arm control

>>**Note:** For better motion effects, the Atom firmware version of the end arm is 6.5, and the python driver library pymycobot version is 3.5.3

### 1 Slider control

Open a command line and run:

- mycobot 280-Pi version:

```bash
# The default serial port name of mycobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
roslaunch mycobot_280pi slider_control.launch port:=/dev/ttyAMA0 baud:=1000000
```

It will **open rviz and a slider component**, you will see the following screen:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/caf-1.png
width ="500" align = "center">

Then you can **control the movement of the model in rviz by dragging the slider**. If you want the real mycobot to move with you, you need to open another command line and run:

- mycobot 280-Pi version:

```bash
# The default serial port name of mycobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
rosrun mycobot_280pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```

**Please note: due to the commandThe robot arm will move to the current position of the model while inputting. Before you use the command, please make sure that the model in rviz does not have any penetration**
**Do not drag the slider quickly after connecting the robot arm to prevent damage to the robot arm**

### 2 Model following

In addition to the above controls, we can also **let the model follow the real robot arm movement**. Open a command line and run:
- mycobot 280-pi version:

```bash
# The default serial port name of mycobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
rosrun mycobot_280pi follow_display.py _port:=/dev/ttyAMA0 _baud:=1000000
```

Then open another command line and run:
- mycobot 280-Pi version:
```bash
roslaunch mycobot_280pi mycobot_follow.launch
```
It will **open rviz to show the model following effect**.

### 3 GUI control

Based on the previous, this package also **provides a simple Gui control interface**. This method is intended for real robotic arms to interact with each other, please connect mycobot.

Open the command line:
- mycobot 280-Pi version:
```bash
# The default serial port name of mycobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
roslaunch mycobot_280pi simple_gui.launch port:=/dev/ttyAMA0 baud:=1000000
```
<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/gui-1.png
width ="500" align = "center">

### 4 Keyboard control

**Added the keyboard control function** in the `mycobot_280` package, and synchronized it in real time in rviz. This function depends on pythonApi, so make sure it is connected to the real robot arm.

Open a command line and run:

- mycobot 280-Pi version:

```bash
# The default serial port name of mycobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
roslaunch mycobot_280pi teleop_keyboard.launch port:=/dev/ttyAMA0 baud:=1000000
```

The running effect is as follows:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/kb-1.png
width ="500" align = "center">

The command line will output mycobot information as follows:

```bash
SUMMARY
========

PARAMETERS
    * /mycobot_services/baud: 1000000
    * /mycobot_services/port: /dev/ttyAMA0
    * /robot_description: <?xml version="1....
    * /rosdistro: noetic
    * /rosversion: 1.16.0

NODES
  /
    mycobot_services (mycobot_communication/mycobot_topics.py)
    real_listener (mycobot_280/listen_real_of_topic.py)
    robot_state_publisher (robot_state_publisher/robot_state_publisher)
    rviz (rviz/rviz)

auto-starting new master
process[master]: started with pid [217714]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to 01e863c8-5642-11f0-a2da-335dad9016e7
process[rosout-1]: started with pid [217728]
started core service [/rosout]
process[robot_state_publisher-2]: started with pid [217731]
process[rviz-3]: started with pid [217733]
process[mycobot_services-4]: started with pid [217738]
process[real_listener-5]: started with pid [217740]
current pymycobot library version: 3.9.9
pymycobot library version meets the requirements!
ls: cannot access '/dev/ttyUSB*': No such file or directory
[INFO] [1751350196.024298]: /dev/ttyAMA0,1000000

MyCobot Status
--------------------------------
Joint Limit:
    joint 1: -168 ~ +168
    joint 2: -135 ~ +135
    joint 3: -150 ~ +150
    joint 4: -145 ~ +145
    joint 5: -165 ~ +165
    joint 6: -180 ~ +180

Connect Status: True

Servo Infomation: all connected

Servo Temperature: unknown

Atom Version: 7.2
```

Next, open another command line and run:

- mycobot 280-Pi version:

```bash
rosrun mycobot_280pi teleop_keyboard.py
#or
rosrun mycobot_280pi teleop_keyboard.py _speed:=70
```

You will see the following output in the command line:
```bash
[INFO] [1751342043.889285]: Waiting to receive current coordinates...
Mycobot Teleop Keyboard Controller (ROS1 - Topic Version)
---------------------------------------------------------
Movement (Cartesian):
              w (x+)
    a (y-)    s (x-)    d (y+)
              z (z-)    x (z+)

Rotation (Euler angles):
    u (rx+)  i (ry+)  o (rz+)
    j (rx-)  k (ry-)  l (rz-)

Movement Step:
    + : Increase movement step size
    - : Decrease movement step size

Gripper:
    g - open    h - close

Pump:
    b - open    m - close

Other:
    1 - Go to init pose
    2 - Go to home pose
    3 - Save current pose as home
    q - Quit

currently:	speed: 50	change percent: 5  
[INFO] [1751342044.199244]: Current moving step: position 12.5 mm, angle attitude 9.0°
```

In this terminal, you can control the state of the robot and move the robot through the keys in the command line.

Parameters supported by this script:

+ _speed: robot movement speed.

+ _change_percent: movement distance percentage.

### 5 End effector

- **Supported end effectors:** myCobot Adaptive Gripper, myCobot Vertical Suction Pump V2.0, Camera Flange

- **Applicable devices:** myCobot 280 M5, myCobot 280 PI

> Note: myCobot Adaptive Gripper only supports myCobot 280 M5 devices

#### 5.1 myCobot vertical pump V2.0

##### 1 Load the model

Open a command line and run:

- myCobot 280-PI version:

```bash
roslaunch mycobot_280pi test_pump.launch
```

It will **open rviz** and you will see the following screen:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/12.1.4-13.png
width ="500" align = "center">

##### 2 Slider control

> **Note: This function only supports the control of the robot**

Open a command line and run:

- myCobot 280-PI version:

```bash
### The default serial port name of myCobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
roslaunch mycobot_280pi slider_control_pump.launch port:=/dev/ttyAMA0 baud:=1000000
```

It will **open rviz and a slider component**, and you will see the following screen:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/12.1.4-16.png
width ="500" align = "center">

Then you can **control the movement of the model in rviz by dragging the slider. ** If you want the real myCobot to move with you, you need to **open another command line** and run:

- myCobot 280-PI version:

```bash
### The default serial port name of myCobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
rosrun mycobot_280pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```

**Please note: Since the robot will move to the current position of the model when the command is input, please make sure that the model in rviz does not have any penetration before you use the command**.
**Do not drag the slider quickly after connecting the robot to prevent damage to the robot**.

#### 5.2 Camera Flange

##### 1 Load the model

Open a command line and run:

- myCobot 280-PI version:

```bash
roslaunch mycobot_280pi test_camera_flange.launch
```

It will **open rviz** and you will see the following screen:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/12.1.4-15.png
width ="500" align = "center">

##### 2 Slider Control

> **Note: This function only supports the control of the robot**

Open a command line and run:

- myCobot 280-PI version:

```bash
# The default serial port name of myCobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
roslaunch mycobot_280pi slider_control_camera_flange.launch port:=/dev/ttyAMA0 baud:=1000000
```

It will **open rviz and a slider component**, and you will see the following screen:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/12.1.4-17.png
width ="500" align = "center">

Then you can **control the movement of the model in rviz by dragging the slider. ** If you want the real myCobot to move with you, you need to **open another command line** and run:

- myCobot 280-PI version:

```bash
# The default serial port name of myCobot 280-Pi version is "/dev/ttyAMA0" and the baud rate is 1000000.
rosrun mycobot_280pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```

**Please note: Since the robot will move to the current position of the model when the command is input, please make sure that the model in rviz does not have any penetration before you use the command**.
**Do not drag the slider quickly after connecting the robot to prevent damage to the robot**.

#### 5.3 Camera Flange && Pump

##### 1 Load the model

Open a command line and run:

- myCobot 280-PI version:

```bash
roslaunch mycobot_280pi test_camera_flange_pump.launch
```

It will **open rviz** and you will see the following:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.4-rivzIntroductionAndUse/12.1.4-18.png
width ="500" align = "center">

#### 5.4 URDF model address

##### 1 myCobot vertical suction pump V2.0

- [myCobot 280-PI version](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot_pi/mycobot_with_pump.urdf)

##### 2 Camera flange

- [myCobot 280-PI version](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot_pi/mycobot_with_camera_flange.urdf)

##### 3 Camera flange && suction pump

[myCobot 280-PI version](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot_pi/mycobot_with_camera_flange_pump.urdf)