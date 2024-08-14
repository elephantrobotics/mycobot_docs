# Arduino

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/ard-01.jpg)

## What is Arduino?

**Arduino** is an easy-to-use, easy-to-use open source electronic prototyping platform, which includes hardware (various development boards that meet Arduino specifications) and software (Arduino IDE and related development kits).
The hardware part (or development board) consists of a microcontroller (MCU), flash memory (Flash) and a set of general input/output interfaces (GPIO), etc. You can think of it as a microcomputer motherboard.
The software part mainly consists of the PC-side Arduino IDE and related board support packages (BSP) and rich third-party function libraries. Users can easily download the BSP and required function libraries related to the development board you have through Arduino IDE to write your program.

## What can MyCobotBasic library do?
MyCobotBasic library is an open source robot control library developed by our company. It can only be used with robots developed by our company. With this library, you can control our robots through Bluetooth, WiFi, serial ports, etc., and it also supports external sensors, IIC communication, LED lights and other functions. You can DIY different application scenarios according to your needs, or refer to the MiniRobot sample code or angle, coordinate, gripper and other control cases we provide. The MiniRobot sample code contains control-related content such as Bluetooth, WiFi, drag teaching, and distance sensors.

**Applicable devices:**

- myCobot 280
- myCobot 280 M5
- myCobot 280 for Arduino <br>

## Arduino development guide

You can use it according to the following instructions Arduino develops our robotic arm
1. [Environment setup](10.1-arduino_download.md)
2. [Simple use](10.2-arduino_use.md)
3. [API description](10.3-api.md)

## Arduino development board connection guide
The myCobot 280 for Arduino version is developed and used based on PC and development board. **There is no built-in system inside the robot**, so the robot, PC and development board need to be combined during use, so please prepare a PC and development board before use. **Please connect the PC and development board before development**.

1. Power on the robot first (if the green light is on, it means the robot is powered on)

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/10.png)

myCobot 280 for Arduino connection

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/2141arduino.jpg)

2. Connect the Arduino board (the connection position is shown in the figure below, with the development board Arduino MEGA2560 as an example)

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/2141devcon1.jpg)

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/11.png)

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/12.png)

3. Connect the serial port to the computer (if the green light is on, it means the computer is successfully connected)

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/13.png)

After connecting, you can follow the steps below to view the connection port number

Click this computer --> Right-click to manage --> Click Device Manager --> Click on the port

![arduino](../../../resource\3-FunctionsAndApplications\6.developmentGuide\Arduino/14.png)

If the port number is displayed normally, it means that the development board has been successfully connected to the computer and development can begin. If no port number is displayed, please check whether the connection lines are loose or have other poor connection conditions.