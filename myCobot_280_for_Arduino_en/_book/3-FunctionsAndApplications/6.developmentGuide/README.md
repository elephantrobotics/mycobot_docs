# Chapter 6 Software Development Guide

## 1 Usage Environment

The myCobot 280 for Arduino version is developed and used based on PC and development board. There is no built-in system inside the robot arm, so the robot arm, PC and development board need to be combined during use. Please prepare a PC and development board before use. At the same time, the myCobot 280 for Arduino version does not have a built-in development environment, so you need to use a PC to install the development environment for the robot arm.

## 2 Development Environment

In order to meet the diverse application needs of robots in different scenarios, we have adapted the robot to multiple programming languages. So far, we have adapted the following mainstream programming languages, and we believe that you can use any of the following languages ​​for development. Please be sure to follow the instructions strictly. Any omitted steps may cause the corresponding language to fail to run successfully. I wish you a smooth use of the robot.

[6.1 Arduino](Arduino/README.md)<br>
Arduino is an easy-to-use, open-source electronic prototyping platform. Users can use the Arduino IDE to easily download the BSP and required function libraries related to the development board you have to write your program. MyCobotBasic library is an Arduino open-source robot control library developed by our company. This library can be used to control our robot through Bluetooth, WiFi, serial port, etc. <br>
[6.2 Python](python/README.md)<br>
Our robot supports Python, and the development of Python API library is becoming more and more perfect. The robot's joint angles, coordinates, grippers and other aspects can be controlled by Python. <br>
[6.3 ROS1](ROS/12.1-ROS1/12.1.1-Introduction.md)<br>ROS (Robot Operating System), as an open-source robot operating system, provides unlimited possibilities for the development and control of robots. Our robot can be controlled in a modular way through the rich control functions of ROS. Whether it is joint control, path planning or sensor feedback, ROS provides corresponding tools and libraries to make the control process more flexible and efficient. </br>
[6.4 ROS2](ROS/12.2-ROS2/12.2.3-ROS2Introduction.md)<br>
ROS 2 (Robot Operating System 2) is a flexible software framework designed for robot software development. Our robot can make application development more efficient and modular through a series of services and functions such as hardware abstraction, device drivers, library functions, visualization tools, messaging, and package management. </br>
[6.5 Blockly](myBlocklyAndUlFlow/myblocklyTutorials/README.md)<br>
myBlockly is a puzzle-style programming software developed by the R&D team of Shenzhen Elephant Robot Company based on the python environment and the pymycobot dependency library, which allows users to program and control the mycobot robot in a building block-like way. <br>
[6.6 Serial Communication](CommunicationProtocolPackage/18-communication.md)<br>
If you have a certain understanding of information theory, coding, and robot communication functions, then you should understand that all communications originate from data transmission. In order to facilitate users to operate the robot, we have opened a communication protocol based on serial communication. You can use the serial assistant or encapsulate it into any programming language you are familiar with to control the robot.

---

[← Previous Chapter](../5.BasicFunction/README.md) | [Next Chapter →](../7.SuccessfulCase/7-SuccessfulCases.md)