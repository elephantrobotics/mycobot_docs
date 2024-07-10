# 机械臂的控制

## 1 网络连接部分

确保PC与myCobot Pro 600处于同一局域网下，以我的wifi热点：ElephantWIFI-5G为例。

* myCobot Pro 600端：

<img src =../../../resourse/12-ApplicationBaseROS/pro600-1.png
width ="500"  align = "center">

* PC端：

<img src =../../../resourse/12-ApplicationBaseROS/pro600-2.png
width ="500"  align = "center">

## 2 Pro600端操作部分

* 确保myCobot Pro 600在Roboflow中处于正常启动状态。

<img src =../../../resourse/12-ApplicationBaseROS/pro600-3.png
width ="500"  align = "center">

* 使用终端指令：`ifconfig` ，获取树莓派的实际ip，本案例中的树莓派ip是`192.168.10.172`。

<img src =../../../resourse/12-ApplicationBaseROS/pro600-4.png
width ="500"  align = "center">

## 3 PC端操作

### 3.1 环境配置

下载大象提供的虚拟机及虚拟机文件，里面有配置好的虚拟机。

ROS1虚拟机文件: http://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/system_images/ubuntu20.04_ROS1_V20230731.ova.zip	

导入虚拟机文件的操作视频：https://drive.google.com/file/d/1KeYk_CUgDE46rVn7zbd0EhraIbgt3qZt/view?usp=sharing


### 3.2 修改脚本文件

打开虚拟机，找到slider_600.py文件

<img src =../../../resourse/12-ApplicationBaseROS/pro600-5.png
width ="500"  align = "center">

从下面链接中获取最新的slider_600.py源码，替换系统中原文件中的旧源码

https://github.com/elephantrobotics/mycobot_ros/blob/noetic/mycobot_pro/mycobot_600/scripts/slider_600.py

更改slider_600.py文件中的ip地址，本案例树莓派ip是192.168.10.172，在用户使用过程中需根据用户机器的实际ip填写，更改结束记得保存。

<img src =../../../resourse/12-ApplicationBaseROS/pro600-6.png
width ="500"  align = "center">

### 3.3 启动仿真滑块控制

在PC的虚拟机中启动滑块控制仿真模型的进程，步骤如下：

在终端中，使用下面的指令加载源码：

```bash
source catkin_ws/devel/setup.bash
```

<img src =../../../resourse/12-ApplicationBaseROS/pro600-7.png
width ="500"  align = "center">

在终端中，使用下面的指令启动滑块控制：

```bash
roslaunch mycobot_600 mycobot_600_slider.launch
```

<img src =../../../resourse/12-ApplicationBaseROS/pro600-8.png
width ="500"  align = "center">

启动成功后，你可以看到机械臂仿真模型及一个滑块控制的UI界面，可以通过拖动滑块的方式对机械臂模型进行控制。
其中，滑块中所示意的数值,其单位是弧度，如下图所示的joint2_to_joint1的弧度3.14，即为关节角度为180°。


<img src =../../../resourse/12-ApplicationBaseROS/pro600-9.png
width ="500"  align = "center">

### 3.4 启动真机滑块控制

在启动真机跟随之前，需要确认2点，避免在异常姿态下启动真机跟随后，机械臂打到其他周围物品及人。

- 让机械臂真机周围无障碍物且处于零位姿态，即零点标签对齐的竖直姿态
- 在rviz的仿真软件中，将6个关节滑块归零，如下图所示，即可看到模型姿态处于零位竖直姿态

<img src =../../../resourse/12-ApplicationBaseROS/pro600-10.png
width ="500"  align = "center">

新开一个终端，启动真机跟对进程，启动指令如下：

```bash
rosrun mycobot_600 slider_600.py
```

<img src =../../../resourse/12-ApplicationBaseROS/pro600-11.png
width ="500"  align = "center">

启动成功后，你可以通过拖动滑块来控制 rviz 中的模型移动且同时控制p600真机移动，请在控制时注意速度不要太快，以免造成机械臂损坏。

**注意**: 如果在新开的终端中，启动滑块控制真机进程时，出现找不到文件的报错信息，可以使用下面的质量重新加载源码。

```bash
source catkin_ws/devel/setup.bash
```
