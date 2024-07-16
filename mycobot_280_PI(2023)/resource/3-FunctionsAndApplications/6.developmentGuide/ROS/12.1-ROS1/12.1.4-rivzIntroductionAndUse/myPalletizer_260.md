# 机械臂的控制

### 1 滑块控制

打开一个命令行，运行：

- mypalletizer 260-M5版本：

```bash
# mypalletizer 260-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mypalletizer_260 slider_control.launch port:=/dev/ttyUSB0 baud:=115200
```

- mypalletizer 260-Pi版本：

```bash
# mypalletizer 260-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
roslaunch mypalletizer_260_pi slider_control.launch port:=/dev/ttyAMA0 baud:=1000000
```

它将打开 rviz 和一个滑块组件，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/mypal260/260slider.png
width ="500"  align = "center">

接着你可以通过拖动滑块来控制 rviz 中的模型移动。如果你想让真实的 mypalletizer 跟着一起运动，需要再打开一个命令行，运行：

- mypalletizer 260-M5版本：

```bash
# mypalletizer 260-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mypalletizer_260 slider_control.py _port:=/dev/ttyUSB0 _baud:=115200
```

- mypalletizer 260-Pi版本：

```bash
# mypalletizer 260-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
rosrun mypalletizer_260_pi slider_control.py _port:=/dev/ttyAMA0 _baud:=1000000
```


**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**

### 2 模型跟随

除了上面的控制，我们也可以让模型跟随真实的机械臂运动。打开一个命令行运行：

- mypalletizer 260-M5版本：

```bash
# mypalletizer 260-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mypalletizer_260 follow_display.py _port:=/dev/ttyUSB0 _baud:=115200
```

- mypalletizer 260-Pi版本：

```bash
# mypalletizer 260-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
rosrun mypalletizer_260_pi follow_display.py _port:=/dev/ttyAMA0 _baud:=1000000
```

然后打开另一个命令行，运行：

- mypalletizer 260-M5版本：

```bash
roslaunch mypalletizer_260 follow.launch
```

- mypalletizer 260-Pi版本：
  
```bash
roslaunch mypalletizer_260_pi follow.launch

它将打开 rviz 展示模型跟随效果。
```


### 3 GUI 控制

在前面的基础上，本包还提供了简单的 Gui 控制界面。 该方式意在于真实机械臂相互联动，请连接 mypalletizer。

打开命令行：

- mypalletizer 260-M5版本：

```bash
# mypalletizer 260-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mypalletizer_260 simple_gui.launch port:=/dev/ttyUSB0 baud:=115200
```

- mypalletizer 260-Pi版本：

```bash
# mypalletizer 260-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
roslaunch mypalletizer_260_pi simple_gui.launch _port:=/dev/ttyAMA0 _baud:=1000000
```

运行效果：

<img src =../../../resourse/12-ApplicationBaseROS/mypal260/260GUI.png
width ="500"  align = "center">

### 4 键盘控制

在 `mypalletizer_260` 的包中添加了键盘控制的功能，并在 rviz 中实时同步。本功能依赖 pythonAPI，所以确保与真实机械臂连接。

打开一个命令行，运行：

- mypalletizer 260-M5版本：

```bash
# mypalletizer 260-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
roslaunch mypalletizer_260 teleop_keyboard.launch port:=/dev/ttyUSB0 baud:=115200
```

- mypalletizer 260-Pi版本：

```bash
# mypalletizer 260-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
roslaunch mypalletizer_260_pi teleop_keyboard.launch port:=/dev/ttyAMA0 baud:=1000000
```

运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/mypal260/260teleboard.png
width ="500"  align = "center">

命令行中将会输出 mypalletizer_260 信息，如下：
```bash
SUMMARY
========

PARAMETERS
 * /mypalletizer_services/baud: 12.1.200
 * /mypalletizer_services/port: /dev/ttyUSB0
 * /robot_description: <?xml version="1....
 * /rosdistro: kinetic
 * /rosversion: 1.12.1.17

NODES
  /
    mypalletizer_services (mypalletizer_communication/mypal_services.py)
    real_listener (mypalletizer_260/listen_real.py)
    robot_state_publisher (robot_state_publisher/robot_state_publisher)
    rviz (rviz/rviz)

ROS_MASTER_URI=http://localhost:12.1.12

process[robot_state_publisher-1]: started with pid [14764]
process[rviz-2]: started with pid [14765]
process[mypalletizer_services-3]: started with pid [14766]
process[real_listener-4]: started with pid [14782]
[INFO] [1646649869.148017]: start ...
[INFO] [1646649869.156531]: /dev/ttyUSB0,12.1.200

Mypalletizer Status
--------------------------------
Joint Limit:
    joint 1: -160 ~ +160
    joint 2: -0.87 ~ +100.01
    joint 3: -17.13 ~ +60
    joint 4: simple show
    joint 5: -170 ~ +170

Connect Status: True

Servo Infomation: unknown

Servo Temperature: unknown

Atom Version: unknown

[INFO] [1646649869.427899]: ready
```


接着，打开另一个命令行，运行：

- mypalletizer 260-M5版本：

```bash
rosrun mypalletizer_260 teleop_keyboard.py
#或者
rosrun mypalletizer_260 teleop_keyboard.py _speed:=70
```

- mypalletizer 260-Pi版本：

```bash
rosrun mypalletizer_260_pi teleop_keyboard.py
#或者
rosrun mypalletizer_260_pi teleop_keyboard.py _speed:=70
```


你会在命令行中看到如下输出：
```bash
Mypalletizer Teleop Keyboard Controller
---------------------------
Movimg options(control coordinations [x,y,z,rx]):
              w(x+)

    a(y-)     s(x-)     d(y+)

        z(z-)       x(z+)

        u(rx+)      i(rx-)
   

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
