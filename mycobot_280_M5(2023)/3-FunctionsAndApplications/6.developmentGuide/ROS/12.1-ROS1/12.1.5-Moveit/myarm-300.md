# myArm-300 Moveit

`mycobot_ros` 现已集成了 MoveIt 部分。

点击桌面上的`ROS1 Shell`图标或者桌面下方栏的对应图标，打开ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
roslaunch myarm_moveit demo.launch
``` 

运行效果如下：  

<img src =../../../resourse/12-ApplicationBaseROS/myarm_moveit.png
width ="500"  align = "center">

可以计划并执行，演示效果：

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="../../../resourse/12-ApplicationBaseROS/myarm_moveit.mp4" type='video/mp4' >
</video>


如果需要让真实的机械臂同步执行计划，需要再打开一个ROS1环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-7.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-8.jpg
width ="500"  align = "center">
<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-9.jpg
width ="500"  align = "center">

然后运行命令：

```bash
# myarm默认串口名为"/dev/ttyAMA0"，波特率为115200".
rosrun myarm_moveit sync_plan.py _port:=/dev/ttyAMA0 _baud:=115200
```

然后再次计划并执行，演示效果：

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="../../../resourse/12-ApplicationBaseROS/myarm_moveit.mp4" type='video/mp4' >
</video>