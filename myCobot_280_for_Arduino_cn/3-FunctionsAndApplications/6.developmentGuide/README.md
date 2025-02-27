# 第六章 软件开发指南

## 1 使用环境

myCobot 280 for Arduino版本是基于PC和开发板进行开发和使用的，机械臂内部无任何内置系统，所以在使用过程中是需要机械臂、PC以及开发板相结合，所以在使用之前请准备好一台PC以及开发板。同时myCobot 280 for Arduino版本无内置开发环境，所以需要你使用PC为机械臂安装开发环境。

**280arduino的控制方式**

目前如果使用uno板子的话，确实是需要arduino去控制。同时uno板子是通过杜邦线连接到arduino板子上的，不能直接插。mkrwifi1010 mega2560这两个板子的话可以用python或ros。

## 2 开发环境

为了满足机器人在不同场景下的多样化应用需求，我们对机器人进行了多种编程语言的适配。到目前为止，我们已经适配了以下主流编程语言，我们认为您可以使用以下任何一种语言进行开发。请务必严格按照说明进行操作。任何遗漏的步骤都可能导致相应语言无法成功运行。祝您顺利使用机器人。

[6.1 Arduino](Arduino/README.md)<br>
Arduino 是一款简单易用、便于上手的开源电子原型平台，使用者可以借由 Arduino IDE 轻松地下载你所持有的开发板相关的BSP和需要的函数库，用于编写你的程序。MyCobotBasic库是我们公司开发的一款 Arduino开源机器人控制库，使用该库可以通过蓝牙、WiFi、串口等方式控制我们的机器人。<br>
[6.2 Python](python/README.md)<br>
我们的机器人支持 Python，Python API 库的开发也日趋完善。机器人的关节角度、坐标、抓手和其他方面都可以通过 Python 进行控制。<br>
[6.3 ROS1](ROS/12.1-ROS1/12.1.1-Introduction.md)<br>ROS（Robot Operating System）作为一个开源的机器人操作系统，为机器人的开发和控制提供了无限的可能性。我们的机器人可以通过ROS丰富的控制功能，通过模块化的方式对机器人进行控制。无论是关节控制、路径规划还是感知反馈，ROS都提供了相应的工具和库，使得控制过程更加灵活和高效。</br>
[6.4 ROS2](ROS/12.2-ROS2/12.2.3-ROS2Introduction.md)<br>
  ROS 2（Robot Operating System 2）是一个灵活的软件框架，专为机器人软件开发而设计。我们的机器人可以通过它提供的硬件抽象、设备驱动、库函数、可视化工具、消息传递以及包管理等一系列服务和功能，使得应用程序的开发变得更为高效和模块化。</br>
[6.5 Blockly](myBlocklyAndUlFlow/myblocklyTutorials/README.md)<br>
  myBlockly是一款由深圳市大象机器人公司研发团队开发完成的，基于python环境以及pymycobot依赖库的拼图式编程软件，可以让用户以搭积木式的方法进行编程控制mycobot机器人。<br>
[6.6 串口通信](CommunicationProtocolPackage/18-communication.md)<br>
  如果您对信息论、编码和机器人通信功能有一定的了解，那么您就应该明白，所有的通信都源于数据传输。为了方便用户操作机器人，我们开放了基于串口通信的通信协议。您可以使用串口助手或将其封装到您熟悉的任何编程语言中来控制机器人。


---

[← 上一章](../5.BasicFunction/README.md) | [下一章 →](../7.SuccessfulCase/7-SuccessfulCases.md)