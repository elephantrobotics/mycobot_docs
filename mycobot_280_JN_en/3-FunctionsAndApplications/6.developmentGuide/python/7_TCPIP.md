# TCP/IP

TCP/IP transmission protocol, namely transmission control/network protocol, is also called network communication protocol. It is the most basic communication protocol in the use of the network, and stipulates the standards and methods for communication between various parts of the Internet. Users can connect to the robot arm through the IP address of the robot arm, so that the robot arm can be remotely operated without connecting to the USB port.

## myCobot

### myCobot Raspberry Pi system remote connection

- When using Raspberry Pi remote connection, please note the following points
1. Raspberry Pi and control end need to be in the same network
2. The server file needs to be executed in Raspberry Pi first (see the gif operation diagram below for specific operations)
3. After the server file is executed, the prompts "Binding succeeded" and "waiting connect" indicate that the start is successful. The control end can refer to **2 Case** for control

![Server](../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\TCPorIP/Server.gif)

*Specific operations:*

*Clone our project library:*`git clone https://github.com/elephantrobotics/pymycobot.git`

*Found in the demo folder [Server.py](https://github.com/elephantrobotics/pymycobot/blob/main/demo/Server.py) file

Please change the parameters passed in the last line of MyCobotServer in the Server.py file according to your machine model.

- The default model is 280PI.
- The default parameters are:
- serial_num: /dev/ttyAMA0
- baud: 1000000

Use python to execute、