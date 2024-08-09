# ROS/ROS2 简介

**ROS** 是机器人操作系统（Robot Operating System）的英文缩写。
**ROS** 是用于编写机器人软件程序的一种具有高度灵活性的软件架构。

**注意**：

- 现阶段，**myCobot 280系列** 、 **myCobot 320系列**、**myPalletizer260系列**、**mechArm270系列** 均支持 **ROS** 的使用
- 通过使用 **mystudio** 烧录相应的固件。其中，在basic中烧录minirobot，选择transponder功能，在atom中烧录最新版的atomMain。

**ROS 图标** ：

![ROS图标](../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS/ROSicon.png)

**ROS** 是开源的，是用于机器人控制的一种后操作系统，或者说次级操作系统。它提供类似操作系统所提供的功能，包含硬件抽象描述、底层驱动程序管理、共用功能的执行、程序间的消息传递、程序发行包管理，它也提供一些工具程序和库用于获取、建 立、编写和运行多机整合的程序。

**ROS** 的首要设计目标是在机器人研发领域提高代码复用率。**ROS** 是一个分布式的进程（也就是 “节点” ）框架，这些进程被封装在易于被分享和发布的程序包和功能包中。**ROS** 也支持一种类似于代码储存库的联合系统，这个系统也可以实现工程的协作及发布。这个设计可以使一个工程的开发实现从文件系统到用户接口完全独立决策（不受 **ROS** 限制）。同时，所有的工程都可以被 **ROS** 的基础工具整合在一起。

由于ROS存在以下缺点：

- 有限的实时通信
- 系统稳定性尚未达到工业级要求
- 没有安全措施
- 只支持 Linux(ubuntu)
- 核心机制性能未优化占用资源

因此，**ROS**无法真正进入行业，自然也就无法商业化。 为了解决这个问题，社区提出了**ROS 2**。 它使**ROS**具有产品化的特性，包括实时性、全平台适应性、适用于低性能硬件（MCU+RTOS）、分布式、数据加密和支持现代编程语言。

**ROS2**首先移除**ROS**中存在的主节点。 去掉主节点后，各个节点可以通过DDS节点相互发现，各个节点是平等的，可以实现一对一、一对多、多对多的通信。 使用DDS进行通信后，可靠性和稳定性得到了增强。

与仅支持Linux系统的**ROS**相比，**ROS2**还支持windows、mac甚至RTOS平台。

**适用设备：**

- myCobot 280
  - myCobot 280 M5
  - myCobot 280 PI
  - **myCobot 280 Jetson Nano**
  - myCobot 280 for Arduino <br>

**使用前提：**

- **Pi \ jetsonnano** 系列，**ATOM** 烧录最新版的 **atomMain** (出厂默认已烧录)

**设备说明：**

- 以上使用设备中，myCobot 280-Pi、**myCobot 280-JetsonNano**、myCobot 320-Pi、mechArm-270 PI等版本自带Ubuntu（V-18.04）系统，已经内置了开发环境，所以无需搭建管理，直接使用即可。

# MoveIt 简介

**MoveIt** 是目前针对机械臂移动操作的最先进的软件，已在 100 多个机器人上使用。它综合了运动规划、控制、3D 感知、运控学、控制和导航的最新成果，提供了开发先进机器人应用的易用平台，为工业、商业和研发等领域的机器人新产品的设计和集成体用评估提供了一个集成化软件平台。

**MoveIt 图标** :

![moveit图标](../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS/moveiticon.png)

**适用设备：**

- myCobot 280
  - myCobot 280 M5
  - myCobot 280 PI
  - myCobot 280 Jetson Nano
  - myCobot 280 for Arduino <br>

**使用前提：**

- **Pi \ jetsonnano** 系列，**ATOM** 烧录最新版的 **atomMain** (出厂默认已烧录)
