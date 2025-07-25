# 一体式吸泵
适配型号：myCobot 280、myPalletizer 260、mechArm 270

![pi](../../resource\4-SupportAndService\Accessories\pump/IP1.png)

**规格说明**

| 名称         | **myCobot 一体式吸泵**                                       |
| ------------ | ------------------------------------------------------------ |
| 型号         | myCobot 体式吸泵                                             |
| 材料         | ABS 注塑                                                     |
| 颜色         | 白色                                                         |
| 尺寸         | 直径 20mm                                                    |
| 吸盘数量     | 1                                                                                                                   |
| 吸取重量     | 50g                                                          |
| 动力源设备   | 吸泵盒                                                       |
| 使用寿命     | 一年                                                         |
| 固定方式     | 乐高连接件                                                   |
| 控制接口     | IO 控制                                                      |
| 使用环境要求 | 常温常压                                                     |
| 适用设备     | ER myCobot 280 系列， ER myPalletizer 260 系列 ，ER mechArm 270 系列 ，ER myBuddy 280 系列 |

**吸泵** : 吸附物体使用

**简介**

- 吸泵，即真空吸附泵，具备一进一出的抽气嘴、排气嘴各一个，它结构简单、体积小巧、使用方便、噪音较低、并有良好的自吸能力等优点。通过控制吸泵套件作为机械臂的末端执行器，执行吸附物体的功能。

- 吸泵配件：电源线 x1、杜邦线 x10、一入两出连接线 x1、乐高科技件 x 若干

**工作原理**

- 吸取物品时：气泵启动抽气吸附物品即可停止，短时不会漏气。
- 放下物品时：电子阀门启动，泄气阀门打开，空气进入真空吸盘脱离被吸物品。

**适用物体**

- 纸片/塑料片
- 平面光滑物体
- 卡片等


**安装使用**

检查配件包东西是否齐全：乐高连接件、杜邦线、双头吸泵
> ![](../../resource\4-SupportAndService\Accessories\pump/IP2.png)

## 吸泵安装
结构安装：

将乐高连接件插入吸泵上预留的插孔中：
![](../../resource\4-SupportAndService\Accessories\pump/IP3.jpg)

1. 将插好连接件的吸泵对准机械臂末端插孔插入：
> 
> ![](../../resource\4-SupportAndService\Accessories\pump/IP4.jpg)

- 电气连接：

  选出公-母杜邦线，母头端插入吸泵方盒上标有引脚的插口：
> 公-母杜邦线：
> ![](../../resource\4-SupportAndService\Accessories\pump/IP5.jpg)
> 注意图中的杜邦线颜色和引脚的对应关系：
> ![](../../resource\4-SupportAndService\Accessories\pump/IP6.jpg)

  公头按给出的对应关系插入机械臂底座引脚：
> ![](../../resource\4-SupportAndService\Accessories\pump/IP7.jpg)
> 左侧为吸泵引脚，右侧为机械臂引脚  
   > GND -> GND  
   > 5V -> 5V  
   > G2 -> 21  
   > G5 -> 20

编程开发：

280-AR 版本：

```python
from pymycobot import MyCobot280
import time

# 初始化一个MyCobot280对象
arm = MyCobot280('COM3', 115200) # 波特率默认是115200，部分板子是1000000，请根据实际进行修改

# 开启吸泵
def pump_on():
  arm.set_digital_output(33, 0)
  time.sleep(0.05)

# 停止吸泵
def pump_off():
  arm.set_digital_output(33, 1)
  time.sleep(0.05)
  arm.set_digital_output(23, 0)
  time.sleep(1)
  arm.set_digital_output(23, 1)
  time.sleep(0.05)

for i in range(2):
  pump_on()
  time.sleep(2)
  pump_off()
  time.sleep(2)
```

- 280-Pi 版本：

```python
from pymycobot import MyCobot280
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot280初始化
import time
import RPi.GPIO as GPIO

# 初始化一个MyCobot280对象
mc = MyCobot280(PI_PORT, PI_BAUD)

# 初始化
GPIO.setmode(GPIO.BCM)
# 引脚20/21分别控制电磁阀和泄气阀门
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# 开启吸泵
def pump_on():
    # 打开电磁阀
    GPIO.output(20，0)

# 停止吸泵
def pump_off():
    # 关闭电磁阀
    GPIO.output(20，1)
    time.sleep(0.05)
    # 打开泄气阀门
    GPIO.output(21，0)
    time.sleep(1)
    GPIO.output(21，1)
    time.sleep(0.05)

pump_off()
time.sleep(3)
pump_on()
time.sleep(3)
pump_off()
time.sleep(3)

GPIO.cleanup() # 释放 pin channel
```



