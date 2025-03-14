# rviz2的简单介绍及使用

rviz2是ROS2中一款三维可视化平台，一方面能够实现对外部信息的图形化显示，另外还可以通过 rviz2 给对象发布控制信息，从而实现对机器人的监测与控制。

## rviz2的简介

ros2安装成功表明rviz2也一起安装成功了，因为ros2的安装包含了rviz2。

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)，然后输入命令打开rviz2：

```bash
rviz2
```

打开rviz2,显示如下界面：

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/rviz-1.png
width ="900"  align = "center">

## 各个区域介绍

+ 左侧为显示器列表，显示器是在3D世界中绘制某些内容的东西，并且可能在显示列表中具有一些可用的选项。
+ 上方是工具栏，允许用户用各种功能按键选择多种功能的工具
+ 中间部分为3D视图: 它是可以用三维方式查看各种数据的主屏幕。3D视图的背景颜色、固定框架、网格等可以在左侧显示的全局选项（Global Options）和网格（Grid）项目中进行详细设置。
+ 下方为时间显示区域，包括系统时间和ROS时间等。
+ 右侧为观测视角设置区域，可以设置不同的观测视角。

本部分我们只进行粗略的介绍，如果您想了解更多详细的内容，可以前往[用户指南](http://wiki.ros.org/rviz/UserGuide)进行查看。

## mycobot_ros2安装与更新

`mycobot_ros2` 是 ElephantRobotics 推出的，适配旗下各类型桌面型机械臂的 ROS 包。

项目地址：https://github.com/elephantrobotics/mycobot_ros2

官方默认的工作空间是`colcon_ws`。

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)，然后输入以下指令：

```bash
cd ~/colcon_ws/src  # 进入工作区的src文件夹中
# 克隆github上的代码
git clone --depth 1 https://github.com/elephantrobotics/mycobot_ros2.git
cd ..       # 返回工作区
colcon build
source install/setup.bash # 添加环境变量
```

为节省编译时间，可以选择单独编译某个功能包：

```bash
colcon build --packages-select 包名
```

例如只编译 `mycobot_280_rdkx5`这个功能包：

```bash
cd ~/colcon_ws
colcon build --packages-select mycobot_280_rdkx5
source install/setup.bash
```

**注意：** 若`/home/sunrise/colcon_ws/src (等效于 ~/colcon_ws/src)`目录中已经存在`mycobot_ros2`文件夹，则需要先删除原有的 `mycobot_ros2`，再执行以上命令。

## 简单使用

**通过launch.py文件启动**

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)
输入以下命令：

```bash
ros2 launch mycobot_280_rdkx5 test.launch.py
```

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.1.png
width ="900"  align = "center">

打开rviz2，并得到如下结果：

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.2.png
width ="900"  align = "center">

如果您想了解更多rviz的相关资料信息，您可以前往[官方文档](http://wiki.ros.org/rviz2)进行查看

## 机械臂的控制

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/280_rdkx5_ros2_demo.mp4" type='video/mp4' >
</video>

### 1 滑块控制

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)，然后运行命令：

```bash
# myCobot 280 rdkx5 版本默认串口名为"/dev/ttyS1"，波特率为1000000.
ros2 launch mycobot_280_rdkx5 slider_control.launch.py
```

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.3.png
width ="900"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动**。真实的 mycobot 将跟着一起运动.

**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以**让模型跟随真实的机械臂运动**。打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)，然后运行命令：

```bash
# myCobot 280 rdkx5 版本默认串口名为"/dev/ttyS1"，波特率为1000000.
ros2 launch mycobot_280_rdkx5 mycobot_follow.launch.py 
```

它将**打开 rviz 展示模型跟随效果**。

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.4.png
width ="900"  align = "center">

### 3 GUI 控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 mycobot。

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)，然后运行命令：

```bash
# myCobot 280 rdkx5 版本默认串口名为"/dev/ttyS1"，波特率为1000000.
ros2 launch mycobot_280_rdkx5 simple_gui.launch.py
```

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.5.png
width ="900"  align = "center">

### 4 键盘控制

在 `mycobot_280_rdkx5` 的包中**添加了键盘控制的功能**，并在 rviz 中实时同步。本功能依赖 pythonApi，所以确保与真实机械臂连接。

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)，然后运行命令：

```bash
# myCobot 280 x5_rdkx5版本默认串口名为"/dev/ttyS1"，波特率为1000000.
ros2 launch mycobot_280_rdkx5 teleop_keyboard.launch.py 
```

运行效果如下：

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.2-ROS2\rviz2/12.2.6.png
width ="900"  align = "center">

命令行中将会输出 mycobot 信息，如下：

```bash
[INFO] [launch]: All log files can be found below /home/sunrise/.ros/log/2025-02-25-16-25-45-949761-sunrise-virtual-machine-19111
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
[listen_real-3] [INFO] [1737443677.525803631] [listen_real]: port:/dev/ttyS1, baud:1000000
```

接着，打开另一个控制台终端，运行：

```bash
ros2 run mycobot_280_rdkx5 teleop_keyboard
```

你会在命令行中看到如下输出：

```bash
Mycobot Teleop Keyboard Controller
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

currently:	speed: 50	change percent: 5 
```

在该终端中，您可以通过命令行中的按键控制机械臂的状态和对机械臂进行移动操作。
\
