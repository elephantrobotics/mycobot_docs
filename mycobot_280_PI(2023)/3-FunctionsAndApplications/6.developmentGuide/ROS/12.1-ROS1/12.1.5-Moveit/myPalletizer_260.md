# Mypalletizer 260 Moveit
`mycobot_ros` 现已集成了 MoveIt 部分。

打开命令行运行：

- mypalletizer 260-M5版本：

```bash
roslaunch mypalletizer_260_moveit mypal_moveit.launch
```

- mypalletizer 260-Pi版本：

```bash
roslaunch mypalletizer_260_pi_moveit mypal_moveit.launch
```

运行效果如下：  

<img src =../../../resourse/12-ApplicationBaseROS/mypal260/260moveit.png
width ="500"  align = "center">

如果需要让真实的机械臂同步执行计划，需要再打开一个命令行，运行：

- mypalletizer 260-M5版本：

```bash
# mypalletizer 260版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun mypalletizer_260_moveit sync_plan.py _port:=/dev/ttyUSB0 _baud:=115200
```

- mypalletizer 260-Pi版本：

```bash
# mypalletizer 260-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为1000000".
rosrun mypalletizer_260_pi_moveit sync_plan.py _port:=/dev/ttyAMA0 _baud:=1000000
```
