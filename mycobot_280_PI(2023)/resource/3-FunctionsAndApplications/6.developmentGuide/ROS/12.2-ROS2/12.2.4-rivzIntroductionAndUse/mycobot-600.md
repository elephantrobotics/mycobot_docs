## 机械臂的控制

### 1 滑块控制

打开一个命令行，运行：

```bash
# mycobot pro 600 默认IP为"192.168.10.159"，端口号为5001.具体IP以实际机械臂连接的网络为准.
ros2 launch mycobot_600 slider_control.launch.py ip:=192.168.10.159 port:=5001
```

它将**打开 rviz 和一个滑块组件**，你将看到如下画面：

<img src =../../../resourse/12-ApplicationBaseROS/600_ros2_slider.png
width ="500"  align = "center">

接着你可以**通过拖动滑块来控制 rviz 中的模型移动**。真实的 mycobot Pro 600 将跟着一起运动。

**请注意：由于在命令输入的同时机械臂会移动到模型目前的位置，在您使用命令之前请确保rviz中的模型没有出现穿模现象**
**不要在连接机械臂后做出快速拖动滑块的行为，防止机械臂损坏**
