## 机械臂的控制

### 1 滑块控制

打开一个命令行，运行：
  
点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
# myArm-300 版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
ros2 launch myarm_300 slider_control.launch.py
```

它将**打开 rviz 和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/myarm_ros2_slider_control.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动**。真实的 myArm-300 将跟着一起运动。


**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以**让模型跟随真实的机械臂运动**。打开一个命令行运行：

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
# myArm-300 版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
ros2 launch myarm_300 mycobot_follow.launch.py 
```

它将**打开 rviz 展示模型跟随效果**。

<img src =../../../resourse/12-ApplicationBaseROS/myarm_ros2_follow.png
width ="500"  align = "center">


### 3 GUI 控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 myArm-300。

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
# myArm-300 版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
ros2 launch myarm_300 simple_gui.launch.py
```

<img src =../../../resourse/12-ApplicationBaseROS/myarm_ros2_gui.png
width ="500"  align = "center">

### 4 键盘控制

在 `myarm_300` 的包中**添加了键盘控制的功能**，并在 rviz 中实时同步。本功能依赖 pythonApi，所以确保与真实机械臂连接。

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：
  
```bash
# myArm-300 版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
ros2 launch myarm_300 teleop_keyboard.launch.py 
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/myarm_ros2_follow.png
width ="500"  align = "center">

命令行中将会输出 mycobot 信息，如下：
```bash
[INFO] [launch]: All log files can be found below /home/er/.ros/log/2023-09-05-10-43-12-301971-u20-VirtualBox-6290
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [robot_state_publisher-1]: process started with pid [6293]
[INFO] [rviz2-2]: process started with pid [6295]
[INFO] [follow_display-3]: process started with pid [6297]
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link link1 had 1 children
[robot_state_publisher-1] Link link2 had 1 children
[robot_state_publisher-1] Link link3 had 1 children
[robot_state_publisher-1] Link link4 had 1 children
[robot_state_publisher-1] Link link5 had 1 children
[robot_state_publisher-1] Link link6 had 1 children
[robot_state_publisher-1] Link link7 had 0 children
[robot_state_publisher-1] [INFO] [1659667392.703132973] [robot_state_publisher]: got segment base
[robot_state_publisher-1] [INFO] [1659667392.703485410] [robot_state_publisher]: got segment link1
[robot_state_publisher-1] [INFO] [1659667392.703545198] [robot_state_publisher]: got segment link2
[robot_state_publisher-1] [INFO] [1659667392.703571119] [robot_state_publisher]: got segment link3
[robot_state_publisher-1] [INFO] [1659667392.703587512] [robot_state_publisher]: got segment link4
[robot_state_publisher-1] [INFO] [1659667392.703603744] [robot_state_publisher]: got segment link5
[robot_state_publisher-1] [INFO] [1659667392.703619685] [robot_state_publisher]: got segment link6
[robot_state_publisher-1] [INFO] [1659667392.703619685] [robot_state_publisher]: got segment link7
[rviz2-2] [INFO] [1659667393.588026632] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-2] [INFO] [1659667393.588472253] [rviz2]: OpenGl version: 3.1 (GLSL 1.4)
[rviz2-2] [INFO] [1659667393.766777360] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-2] Parsing robot urdf xml string.
[follow_display-3] [INFO] [1659667394.310152595] [follow_display]: port:/dev/ttyAMA0, baud:115200
```

接着，打开另一个命令行：

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后运行命令：

```bash
ros2 run myarm_300 teleop_keyboard
```

你会在命令行中看到如下输出：

```bash
myArm Teleop Keyboard Controller
---------------------------
Movimg options(control coordinations [x,y,z,rx,ry,rz]):
              w(x+)

    a(y-)     s(x-)     d(y+)

    z(z-) x(z+)

u(rx+)   i(ry+)   o(rz+)
j(rx-)   k(ry-)   l(rz-)

Gripper control:
    g - open
    h - close

Other:
    1 - Go to init pose
    2 - Go to home pose
    3 - Resave home pose
    q - Quit

currently:	speed: 80	change percent: 10  
```

在该终端中，您可以通过命令行中的按键控制机械臂的状态和对机械臂进行移动操作。

**注意：** 需要执行`2`指令后，方可进行坐标控制操作。
