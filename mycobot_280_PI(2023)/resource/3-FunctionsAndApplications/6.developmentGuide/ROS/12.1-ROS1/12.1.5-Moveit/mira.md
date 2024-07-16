# mira Moveit
`mycobot_ros` 现已集成了 MoveIt 部分。

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="../../../resourse/12-ApplicationBaseROS/mira_moveit.mp4" type='video/mp4' >
</video>

打开命令行运行：
```bash
roslaunch mira_moveit mira_moveit.launch
```

运行效果如下：  

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-2.png
width ="500"  align = "center">

如果需要让真实的机械臂同步执行计划，需要再打开一个命令行，运行：
```bash
# Mira 版本默认串口名为"/dev/ttyUSB0"，波特率为115200".
rosrun mecharm_pi_moveit sync_plan.py
```
