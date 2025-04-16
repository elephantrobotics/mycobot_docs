# Environment setup

The mycobot 280 RDK X5 robot arm has a built-in python environment

You can check the python environment of the robot arm by the following method

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

Enter python in the terminal, then press Enter. When `>>>` is displayed, it means that the python compilation environment has been entered, and you can use python to write code at this time.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/4.png" style="zoom: 70%;" />

You can also use the nano command to create a python file. First open the terminal, enter
```python
nano demo.py
```
Then press Enter to create a python file named demo. Here demo is the file name of the created python file, you can change it to any name here. After pressing Enter, you will enter the code editing page, where you can write python program code.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/2.png" style="zoom: 100%;" />

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/6.png" style="zoom: 100%;" />

After writing the Python program, press `ctrl+s` to save the edited program, and then press `ctrl+x` to exit the editor.

In the open terminal, enter
```python
python demo.py
```
to run the Python program you just wrote.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/3.png" style="zoom: 100%;" />


## Simple use of Python

After the above preparations are completed, start to control the robot arm through Python code. Here, the MyCobot 280 RDK X5 version is used as an example for demonstration.

First, open the PyCharm you installed, create a new Python file, enter the following code, and import our library:

```python
from pymycobot import MyCobot280RDKX5
```

**Note:**

1. If you enter `from pymycobot import MyCobot280RDKX5`, there is no red wavy line under the font, which proves that it has been successfully installed and can be used. If a red wavy line appears, you can refer to [**How ​​to install the API library** ](https://www.cnblogs.com/xiaoguan-bky/p/11184740.html), [**How ​​to call the API library**](https://jingyan.baidu.com/article/25648fc1e86917d191fd009d.html).

2. If you do not want to install the API library through the above command, you can download the project to your local computer through the following github.

First, go to the project address: **https://github.com/elephantrobotics/pymycobot**. Then click the Code button on the right side of the webpage, and then click Download ZIP to download it locally. Put the pymycobot folder in the compressed package pymycobot file project into your python dependency library directory, and you can directly import and use it.

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\build/pymycobotdownload.jpg" style="zoom: 33%;" />

### Simple Demonstration

Create a new Python file in PyCharm and enter the following code to execute the LED flashing.

> **Note:** The corresponding baud rates of various devices are different. Please refer to the information to understand their baud rates when using them. The serial port number can be viewed through **[Calculator Device Manager](https://docs.elephantrobotics.com/docs/gitbook/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-%E5%A6%82%E4%BD%95%E5%8C%BA%E5%88%86cp210x%E5%92%8Ccp34x%E8%8A%AF%E7%89%87)** or the serial port assistant.

The following are the corresponding codes.

```python
from pymycobot import MyCobot280RDKX5
import time
#The above needs to be written at the beginning of the code, which means importing the project package

# MyCobot280 class initialization requires two parameters: serial port and baud rate
# The following is the object code for the Windows version
mc = MyCobot280RDKX5("/dev/ttyS1", 1000000)

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



