# Chapter 6 Software Development Guide

## 1 Usage Environment

The mycobot 280 pi version does not require a PC, laptop or other devices. You can connect a monitor to develop applications (**Tip⚠: Please use the HDMI cable shipped with the robot to connect the monitor and use the built-in system for development**.

## 2 Development Environment

In order to meet the diverse application needs of robots in different scenarios, we have adapted the robot to multiple programming languages. So far, we have adapted the following mainstream programming languages, and we believe that you can use any of the following languages ​​for development. Please be sure to follow the instructions strictly. Any omitted steps may cause the corresponding language to fail to run successfully. I wish you a smooth use of the robot.

[6.1 Python](6.developmentGuide/python/README.md)<br>
Our robots support Python, and the development of the Python API library is also becoming more and more perfect. The robot's joint angles, coordinates, grippers and other aspects can be controlled by Python.<br>
[6.2 ROS1](6.developmentGuide/ROS/12.1-ROS1/12.1.1-Introduction.md)<br>ROS (Robot Operating System) is an open source robot operating system that provides unlimited possibilities for robot development and control. Our robot can control the robot in a modular way through the rich control functions of ROS. Whether it is joint control, path planning or perception feedback, ROS provides corresponding tools and libraries to make the control process more flexible and efficient. </br>
[6.3 ROS2](6.developmentGuide/ROS/12.2-ROS2/12.2.3-ROS2Introduction.md)<br>
ROS 2 (Robot Operating System 2) is a flexible software framework designed for robot software development. Our robot can make application development more efficient and modular through a series of services and functions such as hardware abstraction, device drivers, library functions, visualization tools, messaging, and package management. </br>
[6.4 Serial communication](6.developmentGuide/CommunicationProtocolPackage/18-communication.md)<br>
If you have a certain understanding of information theory, coding and robot communication functions, then you should understand that all communications are derived from data transmission. In order to facilitate users to operate the robot, we have opened a communication protocol based on serial communication. You can use the serial assistant or encapsulate it into any programming language you are familiar with to control the robot. <br>
[6.5 Blockly](6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/README.md)
myBlockly is a puzzle-style programming software developed by the R&D team of Shenzhen Elephant Robot Company, based on the python environment and the pymycobot dependency library, which allows users to program and control the mycobot robot in a building block-style way.

---

[← Previous Chapter](../5.BasicFunction/README.md) | [Next Chapter →](../7.SuccessfulCase/7-SuccessfulCases.md)