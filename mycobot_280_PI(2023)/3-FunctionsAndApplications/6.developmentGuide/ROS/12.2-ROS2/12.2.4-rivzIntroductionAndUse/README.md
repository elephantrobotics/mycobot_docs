# rviz2的简单介绍及使用

rviz是ROS中一款三维可视化平台，一方面能够实现对外部信息的图形化显示，另外还可以通过 rviz 给对象发布控制信息，从而实现对机器人的监测与控制。

## 1 rviz2的简介

ros2安装成功表明rviz2也一起安装成功了，因为ros2的安装包含了rviz2。

打开一个一个新的终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)输入命令打开rviz2

```bash
rviz2
```

打开rviz2,显示如下界面：

<img src =../../../resourse/12-ApplicationBaseROS/rviz-1.png
width ="500"  align = "center">

## 2 各个区域介绍

+ 左侧为显示器列表，显示器是在3D世界中绘制某些内容的东西，并且可能在显示列表中具有一些可用的选项。
+ 上方是工具栏，允许用户用各种功能按键选择多种功能的工具
+ 中间部分为3D视图: 它是可以用三维方式查看各种数据的主屏幕。3D视图的背景颜色、固定框架、网格等可以在左侧显示的全局选项（Global Options）和网格（Grid）项目中进行详细设置。
+ 下方为时间显示区域，包括系统时间和ROS时间等。
+ 右侧为观测视角设置区域，可以设置不同的观测视角。

本部分我们只进行粗略的介绍，如果您想了解更多详细的内容，可以前往[用户指南](http://wiki.ros.org/rviz/UserGuide)进行查看。

## 3 mycobot_ros2安装与更新

- **M5版本：** 请查看 [12.2.1 ROS2的安装](../12.2.1-ROS2的安装.md) 章节末尾。

- **PI版本(Ubuntu 20.04)：**

`mycobot_ros2` 是 ElephantRobotics 推出的，适配旗下各类型桌面型机械臂的 ROS 包。

项目地址：https://github.com/elephantrobotics/mycobot_ros2

官方默认的工作空间是`colcon_ws`。

点击桌面上的`ROS2 Shell`图标或者桌面下方栏的对应图标，打开ROS2环境终端：

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-10.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-11.jpg
width ="500"  align = "center">

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-12.png
width ="500"  align = "center">

然后输入以下指令：

```bash
cd ~/colcon_ws/src  # 进入工作区的src文件夹中
# 克隆github上的代码
git clone https://github.com/elephantrobotics/mycobot_ros2.git
cd ..       # 返回工作区
colcon build --symlink-install # 构建工作区中的代码, --symlink-install：避免每次调整 python 脚本时都需要重新编译
source install/setup.bash # 添加环境变量
```

**注意：** 若`/home/er/colcon_ws/src (等效于 ~/colcon_ws/src)`目录中已经存在`mycobot_ros2`文件夹，则需要先删除原有的 `mycobot_ros2`，再执行以上命令。


## 4 简单使用

**通过launch.py文件启动**

本例子建立在您已经完成[环境搭建](../12.2.1-ROS2的安装.md)，并成功将本公司的代码从GitHub上复制下来的基础上。

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)
输入一下命令进行**ROS2的环境配置**。

```
cd ~/colcon_ws
colcon build --symlink-install
source install/setup.bash
```

再输入：

- mycobot 280-M5版本：

```bash
ros2 launch mycobot_280 test.launch.py
```

![image-20220519154315585](../../../resourse/12-ApplicationBaseROS/ros2_open1.png)

打开rviz2，并得到如下结果：

<img src =../../../resourse/12-ApplicationBaseROS/open-2.png
width ="500"  align = "center">

如果您想了解更多rviz的相关资料信息，您可以前往[官方文档](http://wiki.ros.org/rviz2)进行查看


## 5 M5版本前提条件

- 打开控制台终端（ 快捷键 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> )，打开终端窗口查看设备名称：

```bash
# 查看机械臂的设备名称
ls /dev/ttyUSB* # 旧版本 myCobot280 M5   

# 如果终端没有显示/dev/ttyUSB相关名称，需要使用如下命令
ls /dev/ttyACM* # 新版本 myCobot280 M5
```

- 授予机械臂串口权限：

```bash
# 默认设备名是/dev/ttyUSB0，如果设备名不是默认值，需要修改。
sudo chmod 777 /dev/ttyUSB0 # 旧版本 myCobot280 M5 

sudo chmod 777 /dev/ttyACM0 # 新版本 myCobot280 M5
```

然后输入用户密码（**注意：** 输入密码是不显示的，输入正确即可）。