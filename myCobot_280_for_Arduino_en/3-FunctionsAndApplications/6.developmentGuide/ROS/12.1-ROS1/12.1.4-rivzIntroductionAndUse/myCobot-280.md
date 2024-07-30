## 机械臂的控制

### 1 滑块控制

打开一个命令行，运行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 slider_control.launch port:=/dev/ttyUSB0 baud:=115200
```
- mycobot 280-Pi版本：
  
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
roslaunch mycobot_280pi slider_control.launch port:=/dev/ttyAMA0 baud:=1000000
```

- mycobot 280-JetsonNano版本：
  
```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
roslaunch mycobot_280jn slider_control.launch port:=/dev/ttyTHS1 baud:=1000000
```

- mycobot 280-Arduino版本：
  
```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
roslaunch mycobot_280arduino slider_control.launch port:=/dev/ttyACM0 baud:=115200
```

它将**打开 rviz 和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/caf-1.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动**。如果你想让真实的 mycobot 跟着一起运动，需要再打开一个命令行，运行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280 slider_control.py _port:=/dev/ttyUSB0 _baud:=115200
```

- mycobot 280-Pi版本：
  
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
rosrun mycobot_280pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```

- mycobot 280-JetsonNano版本：
  
```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
rosrun mycobot_280jn slider_control.py _port:=/dev/ttyTHS1 _baud:=1000000
```

- mycobot 280-Arduino版本：
  
```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
rosrun mycobot_280arduino slider_control.py _port:=/dev/ttyACM0 _baud:=115200
```


**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以**让模型跟随真实的机械臂运动**。打开一个命令行运行：
- mycobot 280-M5版本：
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280 follow_display.py _port:=/dev/ttyUSB0 _baud:=115200
```

- mycobot 280-pi版本：
  
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
rosrun mycobot_280pi follow_display.py _port:=/dev/ttyAMA0 _baud:=1000000
```

- mycobot 280-JetsonNano版本：
  
```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
rosrun mycobot_280jn follow_display.py _port:=/dev/ttyTHS1 _baud:=1000000
```

- mycobot 280-Arduino版本：
  
```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
rosrun mycobot_280arduino follow_display.py _port:=/dev/ttyACM0 _baud:=115200
```


然后打开另一个命令行，运行：
- mycobot 280-M5版本：
```bash
roslaunch mycobot_280 mycobot_follow.launch
```
- mycobot 280-Pi版本：
```bash
roslaunch mycobot_280pi mycobot_follow.launch
```

- mycobot 280-JetsonNano版本：
```bash
roslaunch mycobot_280jn mycobot_follow.launch
```

- mycobot 280-Arduino版本：
```bash
roslaunch mycobot_280arduino mycobot_follow.launch
```
它将**打开 rviz 展示模型跟随效果**。

### 3 GUI 控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 mycobot。

打开命令行：
- mycobot 280-M5版本：
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 simple_gui.launch port:=/dev/ttyUSB0 baud:=115200
```
- mycobot 280-Pi版本：
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
roslaunch mycobot_280pi simple_gui.launch port:=/dev/ttyAMA0 baud:=1000000
```
- mycobot 280-JetsonNano版本：
  
```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
roslaunch mycobot_280jn simple_gui.launch port:=/dev/ttyTHS1 baud:=1000000
```

- mycobot 280-Arduino版本：
  
```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
roslaunch mycobot_280arduino simple_gui.launch port:=/dev/ttyACM0 baud:=115200
```

<img src =../../../resourse/12-ApplicationBaseROS/gui-1.png
width ="500"  align = "center">

### 4 键盘控制

在 `mycobot_280` 的包中**添加了键盘控制的功能**，并在 rviz 中实时同步。本功能依赖 pythonApi，所以确保与真实机械臂连接。

打开一个命令行，运行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 teleop_keyboard.launch port:=/dev/ttyUSB0 baud:=115200
```

- mycobot 280-Pi版本：
  
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
roslaunch mycobot_280pi teleop_keyboard.launch port:=/dev/ttyAMA0 baud:=1000000
```

- mycobot 280-JetsonNano版本：
  
```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
roslaunch mycobot_280jn teleop_keyboard.launch port:=/dev/ttyTHS1 baud:=1000000
```

- mycobot 280-Arduino版本：
  
```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
roslaunch mycobot_280arduino teleop_keyboard.launch port:=/dev/ttyACM0 baud:=115200
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/kb-1.png
width ="500"  align = "center">

命令行中将会输出 mycobot 信息，如下：
```bash
SUMMARY
========

PARAMETERS
 * /mycobot_services/baud: 115200
 * /mycobot_services/port: /dev/ttyUSB0
 * /robot_description: <?xml version="1....
 * /rosdistro: kinetic
 * /rosversion: 1.12.1.17

NODES
  /
    mycobot_services (mycobot_280/mycobot_services.py)
    real_listener (mycobot_280/listen_real.py)
    robot_state_publisher (robot_state_publisher/state_publisher)
    rviz (rviz/rviz)

auto-starting new master
process[master]: started with pid [1333]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to f977b3f4-b3a9-11eb-b0c8-d0c63728b379
process[rosout-1]: started with pid [1349]
started core service [/rosout]
process[robot_state_publisher-2]: started with pid [1357]
process[rviz-3]: started with pid [1367]
process[mycobot_services-4]: started with pid [1380]
process[real_listener-5]: started with pid [1395]
[INFO] [1620882819.196217]: start ...
[INFO] [1620882819.205050]: /dev/ttyUSB0,115200

MyCobot Status
--------------------------------
Joint Limit:
    joint 1: -170 ~ +170
    joint 2: -170 ~ +170
    joint 3: -170 ~ +170
    joint 4: -170 ~ +170
    joint 5: -170 ~ +170
    joint 6: -180 ~ +180

Connect Status: True

Servo Infomation: all connected

Servo Temperature: unknown

Atom Version: unknown

[INFO] [1620882819.435778]: ready
```


接着，打开另一个命令行，运行：


- mycobot 280-M5版本：

```bash
rosrun mycobot_280 teleop_keyboard.py
#或者
rosrun mycobot_280 teleop_keyboard.py _speed:=70
```

- mycobot 280-Pi版本：

```bash
rosrun mycobot_280 teleop_keyboard.py
#或者
rosrun mycobot_280pi teleop_keyboard.py _speed:=70
```

- mycobot 280-JetsonNano版本：

```bash
rosrun mycobot_280jn teleop_keyboard.py
#或者
rosrun mycobot_280jn teleop_keyboard.py _speed:=70
```

- mycobot 280-Arduino版本：

```bash
rosrun mycobot_280arduino teleop_keyboard.py
#或者
rosrun mycobot_280arduino teleop_keyboard.py _speed:=70
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

currently:      speed: 50       change percent 5
```

在该终端中，您可以通过命令行中的按键控制机械臂的状态和对机械臂进行移动操作。

该脚本支持的参数：

+ _speed：机械臂移动速度。

+ _change_percent：移动距离百分比。

### 5 视觉
>将相机安装在 mycobot 的末端。 本视觉部分使用 eye-in-hand 的方式。

<img src =../../../resourse/13-AdvancedKit/camera_connect-1.jpg
width ="500"  align = "center">

#### 5.1识别并显示
命令行运行：
- mycobot 280-M5版本：
```bash
roslaunch mycobot_280 detect_marker.launch
```
- mycobot 280-Pi版本：
```bash
roslaunch mycobot_280pi detect_marker.launch
```

- mycobot 280-JetsonNano版本：
```bash
roslaunch mycobot_280jn detect_marker.launch
```

- mycobot 280-Arduino版本：
```bash
roslaunch mycobot_280arduino detect_marker.launch
```
可选择参数：
+ num：相机id， 默认为 0.

启动后效果图：

<img src =../../../resourse/12-ApplicationBaseROS/vision-1.png
width ="500"  align = "center">

识别二维码，获取与相机的相对位置关系。根据 rviz 中mycobot的末端位置，进行坐标转换，最后显示在 rviz 中。

可以参考 [滑块控制](##1421-滑块控制),使用 `slider_control.py` 来控制机械臂

#### 5.2视觉追踪与抓取
>本部分需要使用垂直吸泵。

命令行运行：
- mycobot 280-M5版本：
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 detect_marker_with_topic.launch port:=/dev/ttyUSB0 baud:=115200
```
- mycobot 280-Pi版本：
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
roslaunch mycobot_280pi detect_marker_with_topic.launch port:=/dev/ttyAMA0 baud:=1000000
```

- mycobot 280-JetsonNano版本：
  
```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
roslaunch mycobot_280jn detect_marker_with_topic.launch port:=/dev/ttyTHS1 baud:=1000000
```

- mycobot 280-Arduino版本：
  
```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
roslaunch mycobot_280arduino detect_marker_with_topic.launch port:=/dev/ttyACM0 baud:=115200
```

可选择参数：

+ num： 相机id， 默认为 0.
+ port： 串口字符串
+ baud： 波特率


启动后效果图：

将实时显示 mycobot 的状态。

<img src =../../../resourse/12-ApplicationBaseROS/vision-2.gif
width ="500"  align = "center">

紧接着运行，追踪和抓取的脚本。打开新的命令行：

- mycobot 280-M5版本：
```bash
rosrun mycobot_280 follow_and_pump.py
```

- mycobot 280-Pi版本：
```bash
rosrun mycobot_280pi follow_and_pump.py
```

- mycobot 280-JetsonNano版本：
```bash
rosrun mycobot_280jn follow_and_pump.py
```

- mycobot 280-Arduino版本：
```bash
rosrun mycobot_280arduino follow_and_pump.py
```
启动后，mycobot 会去到它的初始位置

<img src =../../../resourse/12-ApplicationBaseROS/vision-3.gif
width ="500"  align = "center">

当识别到 marker 后，跟随一段时间，然后尝试去吸取并结束程序。

<img src =../../../resourse/12-ApplicationBaseROS/vision-4.png
width ="500"  align = "center">

### 6 末端执行器

- **支持的末端执行器：** myCobot自适应夹爪、myCobot垂直吸泵V2.0、摄像头法兰
- **适用设备：** myCobot 280 M5、myCobot 280 PI

> 注意：myCobot自适应夹爪仅支持 myCobot 280 M5 设备

#### 6.1 myCobot自适应夹爪

##### 1 加载模型

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
roslaunch mycobot_280 test_gripper.launch
```

它将**打开rviz**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-10.png
width ="500"  align = "center">

##### 2 滑块控制

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
# myCobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 slider_control_gripper.launch port:=/dev/ttyUSB0 baud:=115200
```

它将**打开rviz和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-11.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动。** 如果你想让真实的 myCobot 跟着一起运动，需要**再打开一个命令行**，运行：

- myCobot 280-M5版本：

```bash
# myCobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280 slider_control_gripper.py _port:=/dev/ttyUSB0 _baud:=115200
```

**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**。
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**。

##### 3 模型跟随

除了上面的控制，我们也可以**让模型跟随真实的机械臂运动**。打开一个命令行运行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280 follow_display_gripper.py _port:=/dev/ttyUSB0 _baud:=115200
```

然后打开另一个命令行，运行：

- mycobot 280-M5版本：
  
```bash
roslaunch mycobot_280 mycobot_follow_gripper.launch
```

它将**打开 rviz 展示模型跟随效果**。

##### 4 GUI控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 myCobot。

打开命令行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 simple_gui_gripper.launch port:=/dev/ttyUSB0 baud:=115200
```

它将**打开rviz和一个GUI界面**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-12.png
width ="500"  align = "center">

##### 5 键盘控制

在 `mycobot_280` 的包中**添加了键盘控制的功能**，并在 rviz 中实时同步。本功能依赖 pythonApi，所以确保与真实机械臂连接。

打开一个命令行，运行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 teleop_keyboard_gripper.launch port:=/dev/ttyUSB0 baud:=115200
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-10.png
width ="500"  align = "center">

命令行中将会输出 mycobot 信息，如下：

```bash
SUMMARY
========

PARAMETERS
 * /mycobot_services/baud: 115200
 * /mycobot_services/port: /dev/ttyUSB0
 * /robot_description: <?xml version="1....
 * /rosdistro: kinetic
 * /rosversion: 1.12.1.17

NODES
  /
    mycobot_services (mycobot_280/mycobot_services.py)
    real_listener (mycobot_280/listen_real.py)
    robot_state_publisher (robot_state_publisher/state_publisher)
    rviz (rviz/rviz)

auto-starting new master
process[master]: started with pid [1333]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to f977b3f4-b3a9-11eb-b0c8-d0c63728b379
process[rosout-1]: started with pid [1349]
started core service [/rosout]
process[robot_state_publisher-2]: started with pid [1357]
process[rviz-3]: started with pid [1367]
process[mycobot_services-4]: started with pid [1380]
process[real_listener-5]: started with pid [1395]
[INFO] [1620882819.196217]: start ...
[INFO] [1620882819.205050]: /dev/ttyUSB0,115200

MyCobot Status
--------------------------------
Joint Limit:
    joint 1: -170 ~ +170
    joint 2: -135 ~ +140
    joint 3: -150 ~ +150
    joint 4: -145 ~ +135
    joint 5: -170 ~ +170
    joint 6: -180 ~ +180

Connect Status: True

Servo Infomation: all connected

Servo Temperature: unknown

Atom Version: unknown

[INFO] [1620882819.435778]: ready
```

接着，打开另一个命令行，运行：

- mycobot 280-M5版本：

```bash
rosrun mycobot_280 teleop_keyboard.py
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

Pump control:
    b - open
    m - close
    
Other:
    1 - Go to init pose
    2 - Go to home pose
    3 - Resave home pose
    q - Quit

currently:      speed: 50       change percent 5
```

在该终端中，您可以通过命令行中的按键控制机械臂的状态和对机械臂进行移动操作。

该脚本支持的参数：

+ _speed：机械臂移动速度。
+ _change_percent：移动距离百分比。

#### 6.2 myCobot垂直吸泵V2.0

##### 1 加载模型

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
roslaunch mycobot_280 test_pump.launch
```

- myCobot 280-PI版本：

```bash
roslaunch mycobot_280pi test_pump.launch
```

它将**打开rviz**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-13.png
width ="500"  align = "center">

##### 2 滑块控制

> **注意：该功能仅支持对机械臂的控制**

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
# myCobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 slider_control_pump.launch port:=/dev/ttyUSB0 baud:=115200
```

- myCobot 280-PI版本：

```bash
# myCobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
roslaunch mycobot_280pi slider_control_pump.launch port:=/dev/ttyAMA0 baud:=1000000
```

它将**打开rviz和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-16.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动。** 如果你想让真实的 myCobot 跟着一起运动，需要**再打开一个命令行**，运行：

- myCobot 280-M5版本：

```bash
# myCobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280 slider_control.py _port:=/dev/ttyUSB0 _baud:=115200
```

- myCobot 280-PI版本：

```bash
# myCobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
rosrun mycobot_280pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```

**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**。
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**。

##### 3 GUI控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 myCobot。

打开命令行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 simple_gui_pump.launch port:=/dev/ttyUSB0 baud:=115200
```

它将**打开rviz和一个GUI界面**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-14.png
width ="500"  align = "center">

##### 4 键盘控制

在 `mycobot_280` 的包中**添加了键盘控制的功能**，并在 rviz 中实时同步。本功能依赖 python API，所以确保与真实机械臂连接。

打开一个命令行，运行：

- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 teleop_keyboard_pump.launch port:=/dev/ttyUSB0 baud:=115200
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-13.png
width ="500"  align = "center">

接着，打开另一个命令行，运行：

- mycobot 280-M5版本：

```bash
rosrun mycobot_280 teleop_keyboard.py
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

Pump control:
    b - open
    m - close
    
Other:
    1 - Go to init pose
    2 - Go to home pose
    3 - Resave home pose
    q - Quit

currently:      speed: 50       change percent 5
```

在该终端中，您可以通过命令行中的按键控制机械臂的状态和对机械臂进行移动操作。

该脚本支持的参数：

+ _speed：机械臂移动速度。
+ _change_percent：移动距离百分比。

#### 6.3 摄像头法兰

##### 1 加载模型

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
roslaunch mycobot_280 test_camera_flange.launch
```

- myCobot 280-PI版本：

```bash
roslaunch mycobot_280pi test_camera_flange.launch
```

它将**打开rviz**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-15.png
width ="500"  align = "center">

##### 2 滑块控制

> **注意：该功能仅支持对机械臂的控制**

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
# myCobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mycobot_280 slider_control_camera_flange.launch port:=/dev/ttyUSB0 baud:=115200
```

- myCobot 280-PI版本：

```bash
# myCobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
roslaunch mycobot_280pi slider_control_camera_flange.launch port:=/dev/ttyAMA0 baud:=1000000
```

它将**打开rviz和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-17.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动。** 如果你想让真实的 myCobot 跟着一起运动，需要**再打开一个命令行**，运行：

- myCobot 280-M5版本：

```bash
# myCobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280 slider_control.py _port:=/dev/ttyUSB0 _baud:=115200
```

- myCobot 280-PI版本：

```bash
# myCobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
rosrun mycobot_280pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```

**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**。
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**。

#### 6.4 摄像头法兰 && 吸泵

##### 1 加载模型

打开一个命令行，运行：

- myCobot 280-M5版本：

```bash
roslaunch mycobot_280 test_camera_flange_pump.launch
```

- myCobot 280-PI版本：

```bash
roslaunch mycobot_280pi test_camera_flange_pump.launch
```

它将**打开rviz**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-18.png
width ="500"  align = "center">

#### 6.5 URDF模型地址

##### 1 myCobot 自适应夹爪

- [myCobot 280-M5 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot/mycobot_with_gripper_parallel.urdf)

##### 2 myCobot 垂直吸泵V2.0

- [myCobot 280-M5 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot/mycobot_with_pump.urdf)

- [myCobot 280-PI 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot_pi/mycobot_with_pump.urdf)
  
##### 3 摄像头法兰

- [myCobot 280-M5 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot/mycobot_with_camera_flange.urdf)

- [myCobot 280-PI 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot_pi/mycobot_with_camera_flange.urdf)

##### 4 摄像头法兰 && 吸泵

- [myCobot 280-M5 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot/mycobot_with_camera_flange_pump.urdf)

- [myCobot 280-PI 版本](https://github.com/elephantrobotics/mycobot_ros/tree/noetic/mycobot_description/urdf/mycobot_pi/mycobot_with_camera_flange_pump.urdf)