# 机械臂的控制

### 1 滑块控制

- mecharm 270-M5版本：

打开一个命令行，运行：

```bash
# mechArm版本默认串口名为"/dev/ttyUSB0"，波特率为115200".
ros2 launch mecharm slider_control.launch.py
```

- mecharm 270-PI版本：
  
点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
ros2 launch mecharm_pi slider_control.launch.py
```

它将**打开 rviz 和一个滑块组件**，你将看到如下画面（树莓派版本画面略有差异，不影响使用）：

<img src =../../../resourse/12-ApplicationBaseROS/slider_control.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动**。真实的 mechArm 将跟着一起运动。



**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以**让模型跟随真实的机械臂运动**。打开一个命令行运行：

- mecharm 270-M5版本：

```bash
# mechArm版本默认串口名为"/dev/ttyUSB0"，波特率为115200".
ros2 launch mecharm mycobot_follow.launch.py
```

- mecharm 270-PI版本：

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
# mechArm PI版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
ros2 launch mecharm_pi mycobot_follow.launch.py
```

它将**打开 rviz 展示模型跟随效果**。



### 3 GUI 控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 mecharm。

- mecharm 270-M5版本：

打开命令行：

```bash
# mechArm M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200".
ros2 launch mecharm simple_gui.launch.py
```

- mecharm 270-PI版本：

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
# mechArm PI版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
ros2 launch mecharm_pi simple_gui.launch.py
```

运行效果：

<img src =../../../resourse/12-ApplicationBaseROS/mecharm_gui.png
width ="500"  align = "center">

### 4 键盘控制

在 `mechArm` 的包中添加了键盘控制的功能，并在 rviz 中实时同步。本功能依赖 pythonAPI，所以确保与真实机械臂连接。

- mecharm 270-M5版本：

打开一个命令行，运行：

```bash
# mechArm M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200".
ros2 launch mecharm teleop_keyboard.launch.py
```

- mecharm 270-PI版本：

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
# mechArm PI版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
ros2 launch mecharm teleop_keyboard.launch.py
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/mecharm_teleop.png
width ="500"  align = "center">

命令行中将会输出 mechArm 信息，如下：
```bash
[INFO] [launch]: All log files can be found below /home/u20/.ros/log/2022-08-01-14-53-35-880311-u20-VirtualBox-5591
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [robot_state_publisher-1]: process started with pid [5594]
[INFO] [rviz2-2]: process started with pid [5596]
[INFO] [follow_display-3]: process started with pid [5598]
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link link1 had 1 children
[robot_state_publisher-1] Link link2 had 1 children
[robot_state_publisher-1] Link link3 had 1 children
[robot_state_publisher-1] Link link4 had 1 children
[robot_state_publisher-1] Link link5 had 0 children
[robot_state_publisher-1] [INFO] [1659336816.100317312] [robot_state_publisher]: got segment base
[robot_state_publisher-1] [INFO] [1659336816.100434612] [robot_state_publisher]: got segment link1
[robot_state_publisher-1] [INFO] [1659336816.100443491] [robot_state_publisher]: got segment link2
[robot_state_publisher-1] [INFO] [1659336816.100451008] [robot_state_publisher]: got segment link3
[robot_state_publisher-1] [INFO] [1659336816.100457862] [robot_state_publisher]: got segment link4
[robot_state_publisher-1] [INFO] [1659336816.100464597] [robot_state_publisher]: got segment link5
[rviz2-2] [INFO] [1659336816.529758865] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-2] [INFO] [1659336816.530082788] [rviz2]: OpenGl version: 3.1 (GLSL 1.4)
[rviz2-2] [INFO] [1659336816.620671305] [rviz2]: Stereo is NOT SUPPORTED
[follow_display-3] [INFO] [1659336816.635957580] [follow_display]: port:/dev/ttyUSB0, baud:115200
[rviz2-2] Parsing robot urdf xml string.
```


接着，打开另一个命令行，运行：

- mecharm 270-M5版本：
  
```bash
ros2 run mecharm teleop_keyboard
```

- mecharm 270-PI版本：

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
ros2 run mecharm_pi teleop_keyboard
```

你会在命令行中看到如下输出：
```bash
mecharm Teleop Keyboard Controller
---------------------------
Movimg options(control coordinations [x,y,z,rx,ry,rz]):
              w(x+)

    a(y-)     s(x-)     d(y+)

        z(z-)       x(z+)

u(rx+)      i(ry+)      o(rz+)
j(rx-)      k(ry-)      l(rz-)

Gripper control:
    g - open
    h - close

Other:
    1 - Go to init pose
    2 - Go to home pose
    3 - Resave home pose
    q - Quit

currently:	speed: 40	change percent: 5  
```
该脚本支持的参数：

+ _speed：机械臂移动速度。
+ _change_percent：移动距离百分比。
