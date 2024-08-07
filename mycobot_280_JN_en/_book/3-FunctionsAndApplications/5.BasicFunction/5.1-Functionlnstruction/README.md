# Development Environment Introduction

## 1. Introduction to Ubuntu Mate 20.04 System

**What is Ubuntu**

Ubuntu is the most widely used Linux operating system in personal desktop operating systems. For beginners, being familiar with the Linux environment or some embedded hardware operating systems is a good choice.

![img](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction/system.png)

### 1.1 Introduction to basic system functions

#### 1.1.1 Differences between the system and the official release version

**Compared with the official version, we have made the following changes:**

- Integrate python/Ros1/Ros2 and other environments, users can directly use the built-in software provided by our company without setting up other environments

- Our operating software (myStudio, myBlockly) has been installed, no need to install it yourself

- Configure VNC screen sharing, it will have its own hotspot after startup, you can connect to the screen through the remote connection tool: VNC, without connecting to the display

#### 1.1.2 Introduction to basic system functions

**Because the myCobot 280 Jetson nano version has a built-in development environment, the software introduced below can be used directly. **

![img](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction/2.1.5.4-1-002.png)

1 System folder and recycle bin

2 Test tool to test whether myCobot is working properly

3 myStudio: It can burn firmware to the robot arm

4 myBlockly: Visual modular programming software

5 Ros1/Ros2: It is a highly flexible software architecture for writing robot software programs.

6 browser and link: can jump to our official website and Gitbook (need to connect to the Internet)

##### 2 Toolbar

![img](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction/2.1.5.4-1-003.png)

1 Terminal: Command line interface

2 File manager: can view the system's storage resources

3 Notepad: also used to open some script files and view code

4 Vim: text editor For more information, please check [introduction](https://zh.wikipedia.org/zh-hans/Vim)

5 Show desktop: click to directly display the desktop

6 Used to view CPU usage and memory usage

7 Recycle Bin: It is used to store documents temporarily deleted by users, and files stored in the Recycle Bin can be restored

### 1.3 How to reset the system

When the system is damaged due to improper operation or the settings are wrong and cannot be changed, we can re-burn the system image and restore the initial settings (you need an SD card reader). For details, please refer to the following chapters: TF card replacement tutorial and burning image

![img](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction/systemup3.png)

## 2. Introduction to the development environment included in the system

**Ros1/Ros2**

ROS is open source and is a post-operating system, or secondary operating system, for robot control. Through ROS, we can achieve simulated control of the robot arm in a virtual environment. We will use the rviz platform to visualize the robot arm and use a variety of methods to operate our robot arm; through the moveit platform, the robot arm's motion path is planned and executed to achieve the effect of free control of the robot arm. After installing the ROS development environment, you can refer to the ROS related chapters for details.

![img](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction//open-2.png)

**Python**

![2.1.5.4-1-006](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction/2.4.png)

Developed and used based on Python. Our robots support Python, and the development of Python API libraries is becoming more and more complete. You can control the robot's joint angles, coordinates, grippers, etc. through Python. Refer to the **Install Python environment** section for more information.

**Blockly development and use**

myBlockly is a fully visual modular programming software, which belongs to a graphical programming language. It allows users to program and control mycobot in a building block-like way. It is especially suitable for beginners to learn programming and exercise programming thinking.

![blockly](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.1-Functionlnstruction/E.png)