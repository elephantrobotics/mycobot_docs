# IO控制
IO即数据的输入与输出，在我们的机械臂的Basic和Atom上有多个pin脚，通过以下函数接口可以对其设置其输入输出模式。

* **myCobot：**

<img src="../../../resources\3-FunctionsAndApplications\6.developmentGuide\python\io/mycobotIO.jpg" style="zoom: 67%;" />

## myCobot


###  Basic IO

**get_basic_input(pin_no)**

- **功能：** 获取底部引脚号的工作状态
- **参数说明:** `pin_no`：表示机器人底部的具体引脚号
- **返回值：** `pin_signal`( `int`) 当返回的值为0表示在工作状态运行，1表示停止状态

**set_basic_output(pin_no, pin_signal)**

- **功能：** 设置底部引脚号的工作状态
- **参数说明：**
  - `pin_no`( `int`) 设备底部标注的编号仅取数字部分
  - `pin_signal`( `int`)：输入0表示设置为运行状态，输入1表示停止状态
- **返回值：** 无

**get_tof_distance()**

- **功能：** 获取检测到的距离（需要外部距离检测器）
- **返回值：** 检测到的距离值，单位为mm



### Atom IO

**set_pin_mode(pin_no, pin_mode)**

- **功能：** 设置 atom 中指定引脚的状态模式
- **参数说明：**
  - `pin_no` (int)：机器人顶部的具体引脚号
  - `pin_mode` (int)： 限定0~2
    - 0设置为运行状态
    - 1设置为停止状态
    - 2设置为上拉模式
- **返回值：** 无

**set_digital_output(pin_no, pin_signa)**

- **功能：** 设置末端引脚号的工作状态

- **参数说明：**
  - `pin_no`( `int`) 设备末端标注的编号仅取数字部分
  - `pin_signal`( `int`): 输入0表示设置为运行状态，输入1表示停止状态
  
- **返回值：** 无

  **get_digital_input(self, pin_no)**

- **功能：** 获取末端引脚号的工作状态

- **参数说明:** `pin_no`：表示机器人末端的具体引脚号

- **返回值：** `pin_signal`( `int`) 当返回的值为0表示在工作状态运行，1表示停止状态



### 树莓派——GPIO

当您的机械臂为树莓派版本时，您可以用到以下API

**用法：**

文件开头输入代码导入：

```python
from pymycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD  
import RPi.GPIO as GPIO
```

**gpio_init()**

- **功能：** 初始化 GPIO 模块，设置 BCM 模式
- **返回值：** 无

**set_gpio_mode**

- **功能：** 设置树莓派GPIO针脚模式
- **参数**
  - `mode` (`str`) 输入："BCM" 或者 "BOARD" 进入相应模式

**set_gpio_output(pin_no, state)**

- **功能：** 将引脚设置为高，低电平
- **参数说明:** 
  - `pin`( `int`) 引脚编号
  - `state`：0设置为低电平    1设置为高电平 (吸泵低电平开启工作，高电平停止工作)
- **返回值：**  无

**get_gpio_in(pin_no)**

- **功能：** 获取引脚电平状态
- **参数说明:** 
  - `pin_no`( `int`) 引脚编号
- **返回值：**  0为低电平    1为高电平



### 案例使用

* **MyCobot 280-M5版本：**

```python
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD  #当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time
#输入以上代码导入工程所需要的包

# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串， 如：
#       linux： "/dev/ttyAMA0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#   如:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyAMA0", 1000000)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 下面为 windows版本创建对象代码
mc = MyCobot("COM3", 115200)
    
for count in range(5):
# 设置一个循环
    mc.set_basic_output(2,0)
    # 让basic2号位进入工作状态
    mc.set_basic_output(5,0)
    # 让basic5号位进入工作状态
    time.sleep(2)
    #等待两秒
    mc.set_basic_output(2,1)
    #让basic 2号位停止工作
    mc.set_basic_output(5,1)
    #让basic 2号位停止工作
```



* **MyCobot 280-Pi版本：**

```python
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD  #当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time
#输入以上代码导入工程所需要的包

# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串， 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#   如:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 下面为 树莓派版本创建对象代码
mc = MyCobot(PI_PORT, PI_BAUD)
    
# 初始化
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
# 开吸泵
GPIO.output(20, 0)
GPIO.output(21, 0)
# 等待2秒
time.sleep(2)
# 关吸泵
GPIO.output(20, 1)
GPIO.output(21, 1)
```