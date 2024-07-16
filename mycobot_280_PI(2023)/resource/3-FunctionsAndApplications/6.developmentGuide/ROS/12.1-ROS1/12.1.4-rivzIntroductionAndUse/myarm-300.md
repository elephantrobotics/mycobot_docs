# 机械臂的控制

### 1 滑块控制

点击桌面上的`ROS1 Shell`图标或者桌面下方栏的对应图标，打开ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
# myarm默认串口名为"/dev/ttyAMA0"，波特率为115200".
roslaunch myarm slider_control.launch _port:=/dev/ttyAMA0 _baud:=115200
```

它将打开 rviz 和一个滑块组件，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/myarm_slider_control.png
width ="500"  align = "center">

接着你可以通过拖动滑块来控制 rviz 中的模型移动。如果你想让真实的 myarm 跟着一起运动，需要再打开一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
# myarm默认串口名为"/dev/ttyAMA0"，波特率为115200".
rosrun myarm slider_control.py _port:=/dev/ttyAMA0 _baud:=115200
```


**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以让模型跟随真实的机械臂运动。打开一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
# myarm默认串口名为"/dev/ttyAMA0"，波特率为115200".
rosrun myarm follow_display.py _port:=/dev/ttyAMA0 _baud:=115200
```

然后打开另一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
roslaunch myarm mycobot_follow.launch
```

它将打开 rviz 展示模型跟随效果。

<img src =../../../resourse/12-ApplicationBaseROS/myarm_follow.png
width ="500"  align = "center">



### 3 GUI 控制

在前面的基础上，本包还提供了简单的 Gui 控制界面。 该方式意在于真实机械臂相互联动，请连接 myarm。

打开一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
# myarm默认串口名为"/dev/ttyAMA0"，波特率为115200".
roslaunch myarm simple_gui.launch port:=/dev/ttyAMA0 baud:=115200
```

运行效果：

<img src =../../../resourse/12-ApplicationBaseROS/myarm_gui.png
width ="500"  align = "center">

### 4 键盘控制

在 `myarm` 的包中添加了键盘控制的功能，并在 rviz 中实时同步。本功能依赖 pythonAPI，所以确保与真实机械臂连接。

打开一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
# myarm默认串口名为"/dev/ttyAMA0"，波特率为115200".
roslaunch myarm teleop_keyboard.launch port:=/dev/ttyAMA0 baud:=115200
```


运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/myarm_follow.png
width ="500"  align = "center">

命令行中将会输出 myarm 信息，如下：
```bash
SUMMARY
========

PARAMETERS
 * /myarm_services/baud: 115200
 * /myarm_services/port: /dev/ttyAMA0
 * /robot_description: <?xml version="1....
 * /rosdistro: noetic
 * /rosversion: 1.15.14

NODES
  /
    myarm_services (myarm_communication/myarm_services.py)
    real_listener (myarm/listen_real.py)
    robot_state_publisher (robot_state_publisher/robot_state_publisher)
    rviz (rviz/rviz)

ROS_MASTER_URI=http://localhost:11311

process[robot_state_publisher-1]: started with pid [14764]
process[rviz-2]: started with pid [14765]
process[mecharm_services-3]: started with pid [14766]
process[real_listener-4]: started with pid [14782]
[INFO] [1646649869.148017]: start ...
[INFO] [1646649869.156531]: /dev/ttyAMA0,115200

Mycobot Status
--------------------------------
Joint Limit:
    joint 1: -160 ~ +160
    joint 2: -80 ~ +80
    joint 3: -175 ~ +175
    joint 4: -100 ~ +80
    joint 5: -165 ~ +165
    joint 6: -110 ~ +110
    joint 7: -165 ~ +165

Connect Status: True

Servo Infomation: unknown

Servo Temperature: unknown

Atom Version: unknown

[INFO] [1646649869.427899]: ready
```

然后打开另一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
rosrun myarm teleop_keyboard.py
```

你会在命令行中看到如下输出：

```bash
myarm Teleop Keyboard Controller
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

currently:	speed: 50	change percent: 5  
```
该脚本支持的参数：

+ _speed：机械臂移动速度。
+ _change_percent：移动距离百分比。
