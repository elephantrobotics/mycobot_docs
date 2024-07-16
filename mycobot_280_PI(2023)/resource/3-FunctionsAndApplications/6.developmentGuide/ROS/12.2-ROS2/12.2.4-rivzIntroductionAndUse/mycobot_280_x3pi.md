# MyCobot 280 X3Pi远端使用ROS2

## 1 环境搭建

### 1.1 x3pi系统

- 安装tros，打开终端输入安装命令：
  
```bash
apt install tros
```

- 安装tros相关依赖

```bash
pip install xacro
pip install colon-common-extensions
```

**注意：** 若运行ros2程序报错：
```bash
dpkg: error processing archive /var/cache/apt/archives/python3-catkin_pkg-modules_0.5.2-1_all.deb（--unpack）:
trying to overwrite '/usr/lib/python3/dist-packages/catkin_pkg/__init__.py', which is also in package python3-catkin-pkg 0.4.16-1
Errors were encountered whild processing:
/var/cache/apt/archives/python3-catkin-pkg-modules_0.5.2-1_all.deb
E: Sub-process /usr/bin/dpkg returned an error code(1)
```

则运行：

```bash
sudo dpkg -i --force-overwrite /var/cache/apt/archives/python3-catkin_pkg-modules_0.5.2-1_all.deb
```

- 若继续报错，可尝试安装ros2，这里提供鱼香ROS一键安装指令：

```bash
wget http://fishros.com/install -O fishros && . fishros
```

根据提示安装 ros2 foxy 桌面版即可。

- 创建ros2工作空间，终端输入以下命令：

```bash
mkdir -p ~/colcon_ws/src  # 创建文件夹
```

- 添加工作空间的环境

```bash
echo "source ~/colcon_ws/install/setup.bash" >> ~/.bashr
source ~/.bashrc
source /opt/tros/setup.bash
source /opt/tros/local_setup.bash
```

- 安装mycobo_ros2包，官方默认的工作空间是colcon_ws

```bash
cd colcon_ws/src  # 进入工作区的src文件夹中
# 克隆github上的代码
git clone --depth 1 https://github.com/elephantrobotics/mycobot_ros2.git
cd ..       # 返回工作区
colcon build --symlink-install # 构建工作区中的代码，--symlink-install：避免每次调整 python 脚本时都需要重新编译
source install/setup.bash # 添加环境变量
```

### 1.2 PC端

- 远程PC端需搭建Ubuntu20.04 ros2 foxy版本。具体可查看[ROS2搭建章节](../12.2.1-ROS2的安装.md)。
  
- PC端与x3pi系统应连接同一个网络，确保二者同网段。
- 在同网段的前提条件下，在远程PC端的Ubuntu20.04系统里通过ssh远程登录连接x3pi系统，打开一个新终端，输入：

```bash
ssh -X sunrise@192.168.11.46
```

**注意：** 参数 ‘-X’ 是一种转发模式，将x3pi系统的GUI界面转发到ssh连接的远程PC端。sunrise是x3pi系统的用户名，192.168.11.46是x3pi系统的IP地址，可通过ifconfig命令查看实际IP。
  
- 根据提示输入yes，输入x3pi系统的用户密码后即可切换到x3pi的终端（注意：用户密码默认是sunrise，且密码不显示，输入正确即可）。

- 现在你可以在远程PC端操作x3pi了。

### 1.3 简单使用

由于x3pi系统不支持rviz等可视化工具的使用，所以rviz界面将通过远程PC端 Ubuntu20.04显示（需安装ros2 foxy版本）。

- 首先在x3pi端运行：

```bash
source /opt/tros/setup.bash
ros2 launch mycobot_280_x3pi test.launch.py
```

- 然后在PC端虚拟机端修改rviz2配置参数，打开 /$HOME/.rviz2/default.rviz文件，将内容全部替换成x3pi端：/home/sunrise/colcon_ws/src/mycobot_ros2/mycobot_280/mycobot_280_x3pi/config/mycobot_x3pi.rviz 文件的内容后，保存退出。

- 然后在PC虚拟机端运行：

```bash
ros2 run rviz2 rviz2
```

它将显示机器人rviz模型界面。

<img src =../../../resourse/12-ApplicationBaseROS/280-x3pi-1.png
width ="500"  align = "center">

### 1.4 注意事项

若ssh连接不上x3pi，需

- 检查PC和旭日X3派网络能否ping通；
- PC和旭日X3派IP地址是否前三位相同；

## 2 案例使用

>> 注意：所有案例均在远程PC端虚拟机Ubuntu20.04系统操作，并通过ssh远程连接x3pi。

### 2.1 滑块控制

- 通过ssh连接的x3pi端运行：

```bash
ros2 launch mycobot_280_x3pi slider_control.launch.py
```

- 然后在PC虚拟机端运行：
  
```bash
ros2 run rviz2 rviz2
```

它将打开 rviz 和一个滑块组件，接着你可以通过拖动滑块来控制 rviz 中的模型移动。真实的 mycobot 将跟着一起运动。

<img src =../../../resourse/12-ApplicationBaseROS/280-x3pi-2.png
width ="500"  align = "center">

### 2.2 模型跟随

- 通过ssh连接的x3pi端运行：

```bash
ros2 launch mycobot_280_x3pi mycobot_follow.launch.py
```

- 然后在PC虚拟机端运行（如果前面已启动rviz2，则无需再启动）：

```bash
ros2 run rviz2 rviz2
```

它将打开 rviz 展示模型跟随效果，接着你让模型跟随真实的机械臂运动。

### 2.3 GUI控制

- 通过ssh连接的x3pi端运行：

```bash
ros2 launch mycobot_280_x3pi simple_gui.launch.py
```

- 然后在PC虚拟机端运行（如果前面已启动rviz2，则无需再启动）：

```bash
ros2 run rviz2 rviz2
```

它将打开 rviz 展示模型以及打开一个简单的GUI控件界面，与真实机械臂相互联动。

### 2.4 键盘控制

- 通过ssh连接的x3pi端运行：

```bash
ros2 launch mycobot_280_x3pi teleop_keyboard.launch.py
```

- 然后在PC虚拟机端运行（如果前面已启动rviz2，则无需再启动）：

```bash
ros2 run rviz2 rviz2
```

- 再新建一个ssh连接x3pi的终端，运行：

```bash
ros2 run mycobot_280_x3pi teleop_keyboard
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

currently:    speed: 40    change percent: 5
```

在该终端中，您可以通过命令行中的按键控制机械臂的状态和对机械臂进行移动操作。

