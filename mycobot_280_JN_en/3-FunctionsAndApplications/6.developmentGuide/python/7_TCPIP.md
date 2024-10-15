## TCP/IP

TCP/IP transmission protocol, namely transmission control/network protocol, is also called network communication protocol. It is the most basic communication protocol in the use of the network, and stipulates the standards and methods for communication between various parts of the Internet. Users can connect to the robot arm through the IP address of the robot arm, so that the robot arm can be remotely operated without connecting to the USB port.

### myCobot JN system remote connection

- When using Raspberry Pi remote connection, please note the following points
1. Raspberry Pi and control end need to be in the same network
2. The server file(change to Server_280.py) needs to be executed in Raspberry Pi first (see the gif operation diagram below for specific operations)
3. After the server file is executed, the prompts "Binding succeeded" and "waiting connect" indicate that the start is successful. The control end can refer to **Case** for control

![Server](../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\TCPorIP/Server.gif)

*Specific operations:*

*Clone our project library:*`git clone https://github.com/elephantrobotics/pymycobot.git`

*Found in the demo folder [Server_280.py](https://github.com/elephantrobotics/pymycobot/blob/main/demo/Server.py) file*

Please change the parameters passed in the last line of MyCobotServer in the Server.py file according to your machine model.The serial port number of myCobot 280 JetsonNano is `/dev/ttyTHS1`, and the baud rate is `1000000`.

- The default model is 280PI.
- The default parameters are:
- serial_num: /dev/ttyAMA0
- baud: 1000000

Use python to execute

### Case

Run on the PC:

```python
from pymycobot import MyCobot280Socket
# Default port is 9000
#"172.20.10.14" is the IP of the robot arm, please enter your own IP of the robot arm
mc = MyCobot280Socket("172.20.10.14",9000)

#If the connection is normal, you can control the robot arm
mc.send_angles([0,0,0,0,0,0],20)
res = mc.get_angles()
print(res)

...

```