### 使用MoveIt

`mycobot_ros` 现已集成了 MoveIt 部分。

打开命令行运行：
- mycobot 280-M5版本：
  
```bash
roslaunch mycobot_280_moveit mycobot_moveit.launch
```

- mycobot 280-Pi版本：
  
```bash
roslaunch mycobot_280pi_moveit mycobot_moveit.launch
```

- mycobot 280-JetsonNano版本：

```bash
roslaunch mycobot_280jn_moveit mycobot_moveit.launch
```

- mycobot 280-Arduino版本：

```bash
roslaunch mycobot_280arduino_moveit mycobot_moveit.launch
```


运行效果如下：  

<img src =../../../resourse/12-ApplicationBaseROS/moveit-1.png
width ="500"  align = "center">

可以计划并执行，演示效果：

<img src =../../../resourse/12-ApplicationBaseROS/moveit-2.gif
width ="500"  align = "center">

如果需要让真实的机械臂同步执行计划，需要再打开一个命令行，运行：
- mycobot 280-M5版本：
  
```bash
# mycobot 280-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mycobot_280_moveit sync_plan.py _port:=/dev/ttyUSB0 _baud:=115200
```
- mycobot 280-Pi版本：
  
```bash
# mycobot 280-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000.
rosrun mycobot_280pi_moveit sync_plan.py _port:=/dev/ttyAMA0 _baud:=1000000
```

- mycobot 280-JetsonNano版本：

```bash
# mycobot 280-JetsonNano版本默认串口名为"/dev/ttyTHS1"，波特率为1000000.
rosrun mycobot_280jn_moveit sync_plan.py _port:=/dev/ttyTHS1 _baud:=1000000
```

- mycobot 280-JetsonNano版本：

```bash
# mycobot 280-Arduino版本默认串口名为"/dev/ttyACM0"，波特率为115200.
rosrun mycobot_280arduino_moveit sync_play.py _port:=/dev/ttyACM0 _baud:=115200
```
