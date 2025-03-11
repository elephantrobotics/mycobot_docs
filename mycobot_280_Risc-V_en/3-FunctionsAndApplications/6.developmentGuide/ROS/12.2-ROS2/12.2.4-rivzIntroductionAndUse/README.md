# A brief introduction and use of rviz2

rviz2 is a three-dimensional visualization platform in ROS2. On the one hand, it can realize the graphical display of external information. On the other hand, it can also release control information to objects through rviz2, thereby realizing the monitoring and control of robots.

## Introduction to rviz2

The successful installation of ros2 indicates that rviz2 is also successfully installed, because the installation of ros2 includes rviz2.

Open a new terminal (shortcut <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>) and enter the command to open rviz2

```bash
rviz2
```

Open rviz2 and the following interface will be displayed:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/rviz-1.png
width ="900" align = "center">

## Introduction to each area

+ On the left is the display list. The display is something that draws something in the 3D world and may have some options available in the display list.

+ Above is the toolbar, which allows the user to select multiple functions with various function keys

+ The middle part is the 3D view: it is the main screen for viewing various data in three dimensions. The background color, fixed frame, grid, etc. of the 3D view can be set in detail in the Global Options and Grid items displayed on the left.
+ Below is the time display area, including system time and ROS time.
+ On the right is the observation angle setting area, where different observation angles can be set.

In this section, we only give a rough introduction. If you want to know more details, you can go to the [User Guide](http://wiki.ros.org/rviz/UserGuide) to check it out.

## mycobot_ros2 installation and update

`mycobot_ros2` is a ROS package launched by ElephantRobotics that is compatible with various types of desktop robotic arms.

Project address: https://github.com/elephantrobotics/mycobot_ros2

The official default workspace is `colcon_ws`.

Open a new terminal (shortcut <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>), then enter the following command:

```bash
cd ~/colcon_ws/src # Enter the src folder in the workspace
# Clone the code on github
git clone https://github.com/elephantrobotics/mycobot_ros2.git
cd .. # Return to the workspace
colcon build --symlink-install # Build the code in the workspace, --symlink-install: Avoid recompiling every time you adjust the python script
source install/setup.bash # Add environment variables
```

To save compilation time, you can choose to compile a certain package separately:

```bash
colcon build --packages-select package name
```

For example, only compile the `mycobot_280_risc_v` package:

```bash
cd ~/colcon_ws
colcon build --packages-select mycobot_280_risc_v
source install/setup.bash
```

**Note:** If `/home/elephant/colcon_ws/src (equivalent to ~/colcon_ws/src)` directory, you need to delete the original `mycobot_ros2` first, and then execute the above command.

## Simple use

**Start through the launch.py ​​file**

Open a console terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)
Enter the following command:

```bash
cd ~/colcon_ws
colcon build --symlink-install
source install/setup.bash
```

Enter again:

```bash
ros2 launch mycobot_280_risc_v test.launch.py
```

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.1.png
width ="900"  align = "center">

Open rviz2 and get the following result:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.2.png
width ="900"  align = "center">

If you want to learn more about rviz, you can go to the [official document](http://wiki.ros.org/rviz2) to view it

## Robot arm control

### 1 Slider control

Open a console terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>), then run the command:

```bash
# The default serial port name of mycobot 280 RISC-V version is "/dev/ttyAMA0" and the baud rate is 1000000.
ros2 launch mycobot_280_risc_v slider_control.launch.py
```

It will **open rviz and a slider component**, and you will see the following screen:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.3.png
width ="900" align = "center">

Then you can **control the movement of the model in rviz by dragging the slider**. The real mycobot will move with it.

**Please note: Since the robot arm will move to the current position of the model when the command is entered, please make sure that the model in rviz does not appear to be through the model before you use the command**
**Do not drag the slider quickly after connecting the robot arm to prevent damage to the robot arm**

### 2 Model following

In addition to the above control, we can also **let the model follow the movement of the real robot arm**. Open a console terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>), then run the command:

```bash
# The default serial port name of mycobot 280 RISC-V version is "/dev/ttyAMA0" and the baud rate is 1000000.
ros2 launch mycobot_280_risc_v mycobot_follow.launch.py
```

It will **open rviz to show the model following.**

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.4.png
width ="900" align = "center">

### 3 GUI control

Based on the previous, this package also **provides a simple Gui control interface**. This method is intended to allow real robotic arms to interact with each other. Please connect mycobot.

Open a console terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>), then run the command:

```bash
# The default serial port name of mycobot 280 RISC-V version is "/dev/ttyAMA0" and the baud rate is 1000000.
ros2 launch mycobot_280_risc_v simple_gui.launch.py
```

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.5.png
width ="900" align = "center">

### 4 Keyboard control

**Keyboard control function has been added to the `mycobot_280` package**, and it is synchronized in real time in rviz. This function relies on pythonApi, so make sure it is connected to the real robot arm.

Open a console terminal (shortcut key <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>), then run the command:

```bash
# The default serial port name of mycobot 280 RISC-V version is "/dev/ttyAMA0" and the baud rate is 1000000.
ros2 launch mycobot_280_risc_v teleop_keyboard.launch.py ​​
```

The running effect is as follows:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.6.png
width ="900" align = "center">

 Mycobot information will be output on the command line, as follows: 

```bash 
[INFO] [launch]: All log files can be found below /home/elephant/.ros/log/2025-03-11-16-25-45-949761-spacemit-k1-x-MUSE-Pi-board-19111
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [robot_state_publisher-1]: process started with pid [19114]
[INFO] [rviz2-2]: process started with pid [19116]
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link joint2 had 1 children
[robot_state_publisher-1] Link joint3 had 1 children
[robot_state_publisher-1] Link joint4 had 1 children
[robot_state_publisher-1] Link joint5 had 1 children
[robot_state_publisher-1] Link joint6 had 1 children
[robot_state_publisher-1] Link joint6_flange had 0 children
[robot_state_publisher-1] [INFO] [1737443676.433771864] [robot_state_publisher]: got segment joint1
[robot_state_publisher-1] [INFO] [1737443676.433899995] [robot_state_publisher]: got segment joint2
[robot_state_publisher-1] [INFO] [1737443676.433912168] [robot_state_publisher]: got segment joint3
[robot_state_publisher-1] [INFO] [1737443676.433921515] [robot_state_publisher]: got segment joint4
[robot_state_publisher-1] [INFO] [1737443676.433930673] [robot_state_publisher]: got segment joint5
[robot_state_publisher-1] [INFO] [1737443676.433939720] [robot_state_publisher]: got segment joint6
[robot_state_publisher-1] [INFO] [1737443676.433948907] [robot_state_publisher]: got segment joint6_flange
[rviz2-2] [INFO] [1737443677.010176632] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-2] [INFO] [1737443677.010780016] [rviz2]: OpenGl version: 3.1 (GLSL 1.4)
[rviz2-2] [INFO] [1737443677.134247803] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-2] Parsing robot urdf xml string.
[listen_real-3] [INFO] [1737443677.525803631] [listen_real]: port:/dev/ttyAMA0, baud:1000000
```

Next, **open another console terminal** and run:

```bash
ros2 run mycobot_280_risc_v teleop_keyboard
```

You will see the following output in the command line:

```bash
Mycobot Teleop Keyboard Controller
---------------------------
Movimg options(control coordinations [x,y,z,rx,ry,rz]):
w(x+)

a(y-) s(x-) d(y+)

z(z-) x(z+)

u(rx+) i(ry+) o(rz+)

j(rx-) k(ry-) l(rz-)

Gripper control:
g - open
h - close

Other:
1 - Go to init pose
2 - Go to home pose
3 - Resave home pose
q - Quit

currently: speed: 50 change percent: 5
```

In this terminal, you can control the state of the robot and move the robot by pressing keys in the command line.
