## 机械臂的控制

### 1 滑块控制

打开一个命令行，运行：

- 2022 mycobot 320-M5版本：
  
```bash
# 2022 mycobot 320-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch new_mycobot_320 mycobot_320_slider.launch port:=/dev/ttyUSB0 baud:=115200

# 如果末端装配自适应夹爪，则运行（仅支持M5版本，串口修改同上）：
roslaunch new_mycobot_320 mycobot_320_gripper_slider.launch port:=/dev/ttyUSB0 baud:=115200
```
- 2022 mycobot 320-Pi版本：
  
```bash
# 2022 mycobot 320-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
roslaunch new_mycobot_320_pi mycobot_320_slider.launch port:=/dev/ttyAMA0 baud:=115200
```


它将**打开 rviz 和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-4.jpg
width ="500"  align = "center">

如果末端装配自适应夹爪，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-4.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动**。如果你想让真实的 mycobot 跟着一起运动，需要再打开一个命令行，运行：

- 2022 mycobot 320-M5版本：
  
```bash
# 2022 mycobot 320-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun new_mycobot_320 mycobot_320_slider.py _port:=/dev/ttyUSB0 _baud:=115200

# 如果末端装配自适应夹爪，则运行（仅支持M5版本，串口修改同上）：
rosrun new_mycobot_320 mycobot_320_gripper_slider.py _port:=/dev/ttyUSB0 _baud:=115200
```

- 2022 mycobot 320-Pi版本：
  
```bash
# 2022 mycobot 320-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
rosrun new_mycobot_320_pi mycobot_320_slider.py _port:=/dev/ttyAMA0 _baud:=115200
```


**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以**让模型跟随真实的机械臂运动**。打开一个命令行运行：
- 2022 mycobot 320-M5版本：
```bash
# 2022 mycobot 320-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun new_mycobot_320 mycobot_320_follow_display.py _port:=/dev/ttyUSB0 _baud:=115200
```

- 2022 mycobot 320-pi版本：
  
```bash
# mycobot 320-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
rosrun new_mycobot_320_pi mycobot_320_follow_display.py _port:=/dev/ttyAMA0 _baud:=115200
```


然后打开另一个命令行，运行：
- 2022 mycobot 320-M5版本：
```bash
roslaunch new_mycobot_320 mycobot_320_follow_display.launch
```
- 2022 mycobot 320-Pi版本：
```bash
roslaunch new_mycobot_320_pi mycobot_320_follow_display.launch
```
它将**打开 rviz 展示模型跟随效果**。



### 3 GUI 控制

在前面的基础上，本包还**提供了简单的 Gui 控制界面**。 该方式意在于真实机械臂相互联动，请连接 mycobot。

打开命令行：
- 2022 mycobot 320-M5版本：
```bash
# 2022 mycobot 320-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch new_mycobot_320 mycobot_320_simple_gui.launch port:=/dev/ttyUSB0 baud:=115200
```
- 2022 mycobot 320-Pi版本：
```bash
# 2022 mycobot 320-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
roslaunch new_mycobot_320_pi mycobot_320_simple_gui.launch port:=/dev/ttyAMA0 baud:=115200
```

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-5.jpg
width ="500"  align = "center">

### 4 键盘控制

在 `new_mycobot_320` 的包中**添加了键盘控制的功能**，并在 rviz 中实时同步。本功能依赖 pythonApi，所以确保与真实机械臂连接。

打开一个命令行，运行：

- 2022 mycobot 320-M5版本：
  
```bash
# 2022 mycobot 320-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch new_mycobot_320 mycobot_320_teleop_keyboard.launch port:=/dev/ttyUSB0 baud:=115200
```

- 2022 mycobot 320-Pi版本：
  
```bash
# 2022 mycobot 320-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
roslaunch new_mycobot_320_pi mycobot_320_teleop_keyboard.launch port:=/dev/ttyAMA0 baud:=115200
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-6.jpg
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
    mycobot_services (new_mycobot_320/mycobot_services.py)
    real_listener (new_mycobot_320/listen_real.py)
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
    joint 1: -165 ~ +165
    joint 2: -165 ~ +165
    joint 3: -165 ~ +165
    joint 4: -165 ~ +165
    joint 5: -165 ~ +165
    joint 6: -175 ~ +175

Connect Status: True

Servo Infomation: all connected

Servo Temperature: unknown

Atom Version: unknown

[INFO] [1620882819.435778]: ready
```


接着，打开另一个命令行，运行：


- 2022 mycobot 320-M5版本：

```bash
rosrun new_mycobot_320 mycobot_320_teleop_keyboard.py
#或者
rosrun new_mycobot_320 mycobot_320_teleop_keyboard.py _speed:=70
```

- 2022 mycobot 320-Pi版本：

```bash
rosrun new_mycobot_320_pi mycobot_320_teleop_keyboard.py
#或者
rosrun new_mycobot_320_pi mycobot_320_teleop_keyboard.py _speed:=70
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
