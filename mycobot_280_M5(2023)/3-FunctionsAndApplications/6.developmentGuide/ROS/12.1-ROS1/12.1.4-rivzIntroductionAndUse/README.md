# rviz的简单介绍及使用

rviz是ROS中一款三维可视化平台，一方面能够实现对外部信息的图形化显示，另外还可以通过 rviz 给对象发布控制信息，从而实现对机器人的监测与控制。

## 1 rviz的安装及界面简介

在安装ros时，如果执行的完全安装，rviz已经安装好了,您可以直接尝试运行；如果没有完全安装，可单独安装rviz:

```bash
# Ubuntu16.04
sudo apt-get install ros-kinetic-rviz  
```
``` bash
# Ubuntu18.04
sudo apt-get install ros-melodic-rviz   
```
```bash
# Ubuntu20.04
sudo apt-get install ros-noetic-rviz    
```

安装完成后，请先打开一个新的终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>),输入如下指令：
```bash
roscore
```

然后再打开一个一个新的终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)输入命令打开rviz

```bash
rosrun rviz rviz
# 或
rviz
```

打开rviz,显示如下界面：

<img src =../../../resourse/12-ApplicationBaseROS/rviz-1.png
width ="500"  align = "center">

### 1.1 各个区域介绍

+ 左侧为显示器列表，显示器是在3D世界中绘制某些内容的东西，并且可能在显示列表中具有一些可用的选项。
+ 上方是工具栏，允许用户用各种功能按键选择多种功能的工具
+ 中间部分为3D视图: 它是可以用三维方式查看各种数据的主屏幕。3D视图的背景颜色、固定框架、网格等可以在左侧显示的全局选项（Global Options）和网格（Grid）项目中进行详细设置。
+ 下方为时间显示区域，包括系统时间和ROS时间等。
+ 右侧为观测视角设置区域，可以设置不同的观测视角。

本部分我们只进行粗略的介绍，如果您想了解更多详细的内容，可以前往[用户指南](http://wiki.ros.org/rviz/UserGuide)进行查看。

## 2 mycobot_ros安装与更新

- **M5版本：** 请查看 [13.1.2 环境搭建](../12.2.1-ROS2的安装.md) 章节末尾。

- **PI版本(Ubuntu 20.04)：**

`mycobot_ros` 是 ElephantRobotics 推出的，适配旗下各类型桌面型机械臂的 ROS 包。

项目地址：https://github.com/elephantrobotics/mycobot_ros

官方默认的工作空间是`catkin_ws`。

点击桌面上的`ROS1 Shell`图标或者桌面下方栏的对应图标，打开ROS1环境终端：

 <img src =../../../resourse/12-ApplicationBaseROS/12.1.4-1.jpg
 align = "center">

 <img src =../../../resourse/12-ApplicationBaseROS/12.1.4-2.jpg
 align = "center">

 <img src =../../../resourse/12-ApplicationBaseROS/12.1.4-3.jpg
 align = "center">

 然后输入以下指令：

```bash
cd ~/catkin_ws/src  # 进入工作区的src文件夹中
# 克隆github上的代码
git clone https://github.com/elephantrobotics/mycobot_ros.git
cd ..       # 返回工作区
catkin_make # 构建工作区中的代码
source devel/setup.bash # 添加环境变量
```

注意： 若`/home/er/catkin_ws/src (等效于 ~/catkin_ws/src)`目录中已经存在`mycobot_ros`文件夹，则需要先删除原有的 `mycobot_ros`，再执行以上命令。其中，目录路径中的`er`为虚拟机的用户名，若不一致请修改。

## 3 简单使用

**通过launch文件启动**

本例子建立在您已经完成[环境搭建](../12.1.2-环境搭建.md)，并成功将本公司的代码从GitHub上复制下来的基础上。

打开一个控制台终端(快捷键<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>)
输入一下命令进行**ROS的环境配置**。

```bash
cd ~/catkin_ws/
source devel/setup.bash
```

再输入：

- mycobot 280-M5版本：

```bash
roslaunch mycobot_280 test.launch
```

- mycobot 280-Pi版本：

```bash
roslaunch mycobot_280pi test.launch
```

- mycobot 280-JetsonNano版本：
  
```bash
roslaunch mycobot_280jn test.launch
```



打开rviz，并得到如下结果：

<img src =../../../resourse/12-ApplicationBaseROS/open-2.png
width ="500"  align = "center">

如果您想了解更多rviz的相关资料信息，您可以前往[官方文档](http://wiki.ros.org/rviz)进行查看


## 4 M5版本前提条件

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
