# Chapter 6 Software Development Guide

## Usage Environment

The mycobot 280 pi version does not require a PC, laptop or other devices. You can connect a monitor to develop applications (**Tip⚠: Please use the HDMI cable shipped with the robot to connect the monitor and use the built-in system for development**.

## Development Environment

In order to meet the diverse application needs of robots in different scenarios, we have adapted the robot to multiple programming languages. So far, we have adapted the following mainstream programming languages, and we believe that you can use any of the following languages ​​for development. Please be sure to follow the instructions strictly. Any omitted steps may cause the corresponding language to fail to run successfully. I wish you a smooth use of the robot.

[6.1 Python](python/README.md)<br>
Our robots support Python, and the development of the Python API library is also becoming more and more perfect. The robot's joint angles, coordinates, grippers and other aspects can be controlled by Python.<br>
[6.2 ROS2](ROS/12.2-ROS2/12.2.3-ROS2Introduction.md)<br>
ROS 2 (Robot Operating System 2) is a flexible software framework designed for robot software development. Our robot can make application development more efficient and modular through a series of services and functions such as hardware abstraction, device drivers, library functions, visualization tools, messaging, and package management. </br>
[6.3 Serial communication](CommunicationProtocolPackage/18-communication.md)<br>
If you have a certain understanding of information theory, coding and robot communication functions, then you should understand that all communications are derived from data transmission. In order to facilitate users to operate the robot, we have opened a communication protocol based on serial communication. You can use the serial assistant or encapsulate it into any programming language you are familiar with to control the robot. <br>
[6.4 Blockly](myBlocklyAndUlFlow/myblocklyTutorials/README.md)
myBlockly is a puzzle-style programming software developed by the R&D team of Shenzhen Elephant Robot Company, based on the python environment and the pymycobot dependency library, which allows users to program and control the mycobot robot in a building block-style way.

---

[← Previous Chapter](../5.BasicFunction/README.md) | [Next Chapter →](../7.SuccessfulCase/7-SuccessfulCases.md)