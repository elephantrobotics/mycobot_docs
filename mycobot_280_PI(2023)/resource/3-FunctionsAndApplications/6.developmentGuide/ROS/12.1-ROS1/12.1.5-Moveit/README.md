## MoveIt

### 1 MoveIt 简介

MoveIt 是ROS中的一个集成开发平台，由多种用于操纵机械臂的功能包组成，包括：运动规划、操作、控制、逆运动学、3D感知和碰撞检测等。

下图所示为 Moveit 提供的主要节点 **move_group** 的高层结构，它像一个组合器：把所有单独的组件集成在一起，提供一系列的 actions 和 services 供用户使用。

<img src =../../../resourse/12-ApplicationBaseROS/moveit-3.png
width ="500"  align = "center">

### 2 用户界面
用户可以通过三种方式访问move_group提供的操作和服务：

* 在C++ ： 使用move_group_interface包可以方便实用move_group。
* 在 Python ： 使用moveit_commander包。
* 通过 GUI ： 使用 Motion——commander 的 Rviz（ROS可视化工具）。

move_group可以使用ROS参数服务器进行配置，从中还可以获取机器人的URDF和SRDF。

### 3 配置
move_group是一个 ROS 节点。它使用ROS参数服务器来获取三种信息：

1. URDF - move_group在ROS参数服务器上查找robot_description参数，以获取机器人的URDF。

2. SRDF - move_group在 ROS 参数服务器上查找robot_description_semantic参数，以获取机器人的 SRDF。SRDF 通常由用户使用 MoveIt 设置助理创建。

3. MoveIt 配置 - move_group将在 ROS 参数服务器上查找特定于 MoveIt 的其他配置，包括关节限制、运动学、运动规划、感知和其他信息。这些组件的配置文件由MoveIt设置助手自动生成，并存储在机器人的相应MoveIt配置包的配置目录中。

