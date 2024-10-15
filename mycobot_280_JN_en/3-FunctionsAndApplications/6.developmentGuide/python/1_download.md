# Environment setup
pymycobot is a Python package for serial communication with myCobot, supporting Python2, Python3.5 and later versions.

Before using pymycobot to control the robot arm, you need to build a Python environment. The following is a detailed description of Python download and installation.

Since the mycobot 280 JN robot arm has a built-in python environment, you can write python code in the Ubuntu system of the 280 JN, or you can write a python program in your own PC, and copy the written python program to the Ubuntu system of the robot arm with a USB flash drive for running.

The python environment of the robot arm can be checked by the following method

**Check the python package:**

Open the terminal, enter
```python
pip list
```
Then press the enter key to view all the packages currently installed in the python environment.

Enter
```python
python --version
```
in the terminal to query the python version currently used by the robot arm.

Enter python in the terminal and press Enter. When `>>>` is displayed, it means that you have entered the python compilation environment. You can now use python to write code.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/4.PNG" style="zoom: 67%;" />

You can also use the nano command to create a python file. First open the terminal, enter
```python
nano demo.py
```
Then press Enter to create a python file named demo. Here demo is the file name of the created python file, you can change it to any name here. After pressing Enter, you will enter the code editing page, where you can write python program code.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/2.PNG" style="zoom: 67%;" />

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/6.PNG" style="zoom: 67%;" />

After writing the Python program, press `ctrl+s` to save the edited program, and then press `ctrl+x` to exit the editor.

In the opened terminal, enter
```python
python demo.py
```
to run the Python program you just wrote.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/3.PNG" style="zoom: 67%;" />

pymycobot is a Python package for serial communication with myCobot, supporting Python2, Python3.5 and later versions.

Before using pymycobot to control the robot arm, you need to build a Python environment. The following is a detailed description of Python download and installation.

## Download and install Python on your PC

This section will guide you to install Python on your PC. You can write Python programs on your PC and then copy them to the Ubuntu system of the robot arm via a USB flash drive.

**Applicable devices:**

* myCobot 280:
* myCobot 280 M5
* myCobot 280 PI
* **myCobot 280 Jetson Nano**
* myCobot 280 for Arduino

Currently, there are two versions of Python, one is `2.x` version and the other is `3.x` version. These two versions are incompatible. As `3.x` version is becoming more and more popular, our tutorial will take the latest `3.10.7` version as an example.

###  Install Python

> **Note: **Before installing, please confirm whether your computer is 64-bit or 32-bit. Right-click `My Computer` and select `Properties`. As shown in the figure below, it is a 64-bit operating system, so select the 64-bit Python installation package.
>
> <img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/operatingsystemchecking1.jpg" style="zoom: 67%;" />
>
> <img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/operatingsystemchecking2.jpg" style="zoom: 67%;" />

* **Python official download address: https://www.python.org/downloads/**

* **Click the `Downloads` option to start downloading Python, click `Add Python 3.10 to PATH`, click `Install Now` to start installing Python**

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pythondownload1.jpg" style="zoom: 33%;" /> 

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pythoninstall2.jpg" style="zoom: 50%;" />

 <img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pythoninstall3.jpg" style="zoom : 50%;" /> 

* **The prompt "Setup was successful" appears, indicating that the installation is complete**

* <img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pythoninstall4.jpg" style="zoom: 50%;" /> 


### Run Python
  After successful installation, open the command prompt window (Win+R, enter cmd and press Enter), and type `python`. Two situations will occur.

**Situation 1:**

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/successfulinstallation.jpg" style="zoom: 50%;" />

The prompt in the picture indicates that Python has been successfully installed.

The prompt `>>>` indicates that we are already in the Python interactive environment. We can enter any Python code and get the execution result immediately after pressing Enter.

**Case 2:**

If the input is wrong (for example, enter pythonn), an error message will appear:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/installerror.jpg" style="zoom: 50%;" />

> **Note:** The error message is generally caused by not configuring the environment variables. You can refer to **1.3 Configure environment variables** to modify the environment variables.

### Configure environment variables
Since Windows will search for python.exe according to the path set by a Path environment variable, if it is not found, an error will be reported. Therefore, if you miss checking `Add Python 3.10 to PATH` during installation, you need to manually add the path where python.exe is located to Path, or reinstall Python and remember to check the `Add Python 3.10 to PATH` option.

The following are the steps to manually add the path where python.exe is located.

* Right-click My Computer –> Select Properties –> Select Advanced System Settings –> Select Environment Variables in the lower right corner:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/environment configuration.jpg" style="zoom: 50%;" />

* Environment variables mainly include user variables and system variables. The environment variables that need to be set are in these two variables. As shown in the figure below:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/user variable1.jpg" style="zoom: 50%;" />

* User variables are used to download programs that can be used in cmd commands. Write the absolute path of the program to the user variable and you can use it, as shown in the figure below:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/user variable2.jpg" style="zoom: 50%;" />

* After completing the above steps, open the command prompt window (Win+R, then enter cmd, press Enter), type Python, and the prompt in the figure below indicates success:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/user variable3.jpg" style="zoom: 50%;" />

## PyCharm installation and use

PyCharm is a powerful Python editor with cross-platform capabilities. First, let's introduce the installation steps of PyCharm in Windows system.

**Download address:** **https://www.jetbrains.com/pycharm/download/#section=windows**

### Download and install

* After entering the website, we will see the following interface:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharm界面.jpg" style="zoom: 40%;" />

Download the file according to the interface introduction. Professional means professional version, and Community means community version. It is recommended to install the community version because it is free to use.

* After downloading, start installing and click `Next`:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharm下载1.jpg" style="zoom: 50%;" />

* Select the corresponding options according to your personal preferences, and then click `Next`:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharm下载2.jpg" style="zoom: 50%;" />

* The following interface appears and continue to click `Next`:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharm下载3.jpg" style="zoom: 50%;" />

* Click `Finish` to complete the installation:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharm下载4.jpg" style="zoom: 50%;" />

### Create a project

After PyCharm is installed, enter the software and create the first program.

* Click the PyCharm icon on the desktop to enter PyCharm, as shown in the figure below, and click `New Project`:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/createproject1.jpg" style="zoom: 33%;" />

* After clicking, find `Interpreter`, start setting the interpreter, and click `Add Interpreter`:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/interpreter1.jpg" style="zoom: 50%;" />

* Click `New`, find the python.exe storage location, and check the `Inherit global site-package` option:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/interpreter3.jpg" style="zoom: 33%;" />

* Set `Location`. Location is where the PyCharm project is stored. You can choose it according to your needs.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/location1.jpg" style="zoom: 33%;" />

* Create a new PyCharm file. Right-click the document icon pointed by the arrow, click `New`, click `Python File`, and the new file is created successfully.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharmfile1.jpg" style="zoom: 33%;" />

* Name Python File:

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pycharmfile2.jpg" style="zoom: 67%;" />

* After the file is successfully created, you will enter the following interface and you can write your own program

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/createproject3.jpg" style="zoom: 33%;" />

### Before use

* Firmware burning. Firmware refers to the device "driver" stored inside the device. Only through firmware can the operating system implement the operation of a specific machine according to the standard device driver. Different versions of the robot arm need to burn different firmware (refer to the **MyStudio**chapter).
* **Pi \ jetsonnano version** The latest version of atomMain is burned in the Atom at the end. It is burned by default at the factory, and there is no need to burn it yourself.
* pymycobot installation. Open a console terminal (shortcut Win+R, enter cmd to enter the terminal), and enter the following command:

```python
pip install pymycobot --upgrade --user
```

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pymycobotinstall.jpg" style="zoom: 67%;" />

* Source code installation. Open a console terminal (shortcut Win+R, enter cmd to enter the terminal), enter the following command to install:

```python
git clone https://github.com/elephantrobotics/pymycobot.git <your-path>
#Where <your-path> fills in your installation address, if not filled in, the current path is used by default

cd <your-path>/pymycobot
#Enter the pymycobot folder of the download package

#Run one of the following commands according to your python version
# Install
python2 setup.py install
# or
python3 setup.py install
```

## Simple use of Python

After the above preparations are completed, start to control the robot arm through Python code. Here, the MyCobot 280 JN version is used as an example for demonstration.

First, open the PyCharm you installed, create a new Python file, enter the following code, and import our library:

```python
from pymycobot.pymycobot280 import MyCobot280
```

**Note:**

1. If you enter `from pymycobot.pymycobot280 import MyCobot280`, there is no red wavy line under the font, which proves that it has been successfully installed and can be used. If a red wavy line appears, you can refer to [**How ​​to install the API library** ](https://www.cnblogs.com/xiaoguan-bky/p/11184740.html), [**How ​​to call the API library**](https://jingyan.baidu.com/article/25648fc1e86917d191fd009d.html).

2. If you do not want to install the API library through the above command, you can download the project to your local computer through the following github.

First, go to the project address: **https://github.com/elephantrobotics/pymycobot**. Then click the Code button on the right side of the webpage, and then click Download ZIP to download it locally. Put the pymycobot folder in the compressed package pymycobot file project into your python dependency library directory, and you can directly import and use it.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pymycobotdownload.jpg" style="zoom: 33%;" />

### Simple Demonstration

Create a new Python file in PyCharm and enter the following code to execute the LED flashing.

> **Note:** The corresponding baud rates of various devices are different. Please refer to the information to understand their baud rates when using them. The serial port number can be viewed through **[Calculator Device Manager](https://docs.elephantrobotics.com/docs/gitbook/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-%E5%A6%82%E4%BD%95%E5%8C%BA%E5%88%86cp210x%E5%92%8Ccp34x%E8%8A%AF%E7%89%87)** or the serial port assistant.

The following are the corresponding codes.

```python
from pymycobot.mycobot280 import MyCobot280
import time
#The above needs to be written at the beginning of the code, which means importing the project package

# MyCobot280 class initialization requires two parameters: serial port and baud rate

# Initialize a MyCobot280 object
# The following is the object code for the JN version
mc = MyCobot280("/dev/ttyTHS1", 1000000)

i = 7
# Loop 7 times
  while i > 0:
  mc.set_color(0,0,255) #Blue light on
  time.sleep(2) #Wait 2 seconds
  mc.set_color(255,0,0) #Red light on
  time.sleep(2) #Wait 2 seconds
  mc.set_color(0,255,0) #Green light on
  time.sleep(2) #Wait 2 seconds
  i -= 1
```