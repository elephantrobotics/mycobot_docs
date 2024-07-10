
# 关节控制

对于串联式多关节机器人，关节空间的控制是针对机器人各个关节的变量进行的控制，目标是让机器人各个关节按照一定速度达到目标位置。

> **注意：**在设置角度时，不同系列的机械臂限位有所不同，具体可查看对应型号的参数介绍。

## mechArm

### 单关节控制

**send_angle(id, degree, speed)**

- **功能：** 发送指定的单个关节运动至指定的角度
- **参数说明：**
  - `id`: 代表机械臂的关节，六轴有六个关节，四轴有四个关节，有特定的表示方法
    关节一的表示法：`Angle.J1.value`（也可以用数字1-6来表示）
  - `degree`: 表示关节的角度
  - `speed`：表示机械臂运动的速度，范围0~100
- **返回值：** 无

**set_encoder(joint_id, encoder)**

- **功能：** 发送指定的单个关节运动至指定的电位值
- **参数说明：**

  - `joint_id`: 代表机械臂的关节，六轴有六个关节，四轴有四个关节，有特定的表示方法
    关节一的表示法：`Angle.J1.value`(也可以用数字1-6来表示）
  - `encoder`:表示机械臂的电位值，取值范围是 0 ~ 4096
- **返回值：** 无

### 多关节控制

**get_angles()** 

- **功能：** 获取所有关节角度

- **返回值：** `list`一个浮点值的列表代，表所有关节的角度

**send_angles(degrees, speed)**

- **功能：**  发送所有角度给机械臂所有关节
- **参数说明：**
  - `degrees`: `(List[float])`包含所有关节的角度 , 六轴机器人有六个关节所以长度为 6，四轴长度为4，如6轴的表示方法为：`[20,20,20,20,20,20]`
  - `speed`: 表示机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**set_encoders(encoders, sp)**

- **功能：** 发送电位值给机械臂所有关节
- **参数说明：**
  - `encoder`:表示机械臂的电位值，取值范围是 0 ~ 4096，六轴长度为6，四轴长度为4，如6轴的表示方法为：`[2048,2048,2048,2048,2048,2048]`
  - `sp`: 表示机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**sync_send_angles(degrees, speed, timeout=7)**

- **功能：** 同步发送角度，到达目标点返回
- **参数说明：**
  - `degrees`: 每个关节的角度值列表 `List[float]`
  - `speed`: ( `int`)机械臂运动的速度，取值范围是0-100
  - `timeout`：时间默认7s

**get_radians()**

- **功能：** 获取所有关节的弧度
- **返回值：** `list`包含所有关节弧度值的列表

**send_radians(radians, speed)**

- **功能：** 发送弧度值给机械臂所有关节
- **参数说明：**
  - `radians`：表示机械臂的弧度值，取值范围是 -5~5
- **返回值：** `list`包含所有关节弧度值的列表

### 案例使用


```python
from pymycobot.mecharm import MechArm
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的MechArm时，可以引用这两个变量进行MechArm初始化
import time

# MechArm 类初始化需要两个参数：
#   第一个是串口字符串， 如：
#       linux： "/dev/ttyAMA0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#    如:
#       mecharm-M5:
#           linux:
#              mc = MechArm("/dev/ttyAMA0", 1000000)
#           windows:
#              mc = MechArm("COM3", 115200)
#       mecharm-raspi:
#           mc = MechArm(PI_PORT, PI_BAUD)
#
# 初始化一个MechArm对象
# 这里为 windows版本创建对象代码
mc = MechArm("COM3", 115200)

# 通过传递角度参数，让机械臂每个关节移动到对应[0, 0, 0, 0, 0, 0]的位置
mc.send_angles([0, 0, 0, 0, 0, 0], 50)

# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2.5)

# 让关节1移动到90这个位置
mc.send_angle(Angle.J1.value, 90, 50)
# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2)

# 以下代码可以让机械臂左右摇摆
# 设置循环次数
num=5
while num > 0:
    # 让关节2移动到50这个位置
    mc.send_angle(Angle.J2.value, 50, 50)

    # 设置等待时间，确保机械臂已经到达指定位置
    time.sleep(1.5)

    # 让关节2移动到-50这个位置
    mc.send_angle(Angle.J2.value, -50, 50)

    # 设置等待时间，确保机械臂已经到达指定位置
    time.sleep(1.5)

    num -= 1

# 让机械臂缩起来。你可以手动摆动机械臂，然后使用get_angles()函数获得坐标数列，
# 通过该函数让机械臂到达你所想的位置。
mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)

# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2.5)

# 让机械臂放松，可以手动摆动机械臂
mc.release_all_servos()
```

## myCobot

### 单关节控制

**send_angle(id, degree, speed)**

- **功能：** 发送指定的单个关节运动至指定的角度
- **参数说明：**
  - `id`: 代表机械臂的关节，六轴有六个关节，四轴有四个关节，有特定的表示方法
    关节一的表示法：`Angle.J1.value`（也可以用数字1-6来表示）
  - `degree`: 表示关节的角度
  - `speed`：表示机械臂运动的速度，范围0~100
- **返回值：** 无

**set_encoder(joint_id, encoder)**

- **功能：** 发送指定的单个关节运动至指定的电位值
- **参数说明：**
  
  - `joint_id`: 代表机械臂的关节，六轴有六个关节，四轴有四个关节，有特定的表示方法
    关节一的表示法：`Angle.J1.value`(也可以用数字1-6来表示）
  - `encoder`:表示机械臂的电位值，取值范围是 0 ~ 4096
- **返回值：** 无

### 多关节控制

**get_angles()** 

- **功能：** 获取所有关节角度

- **返回值：** `list`一个浮点值的列表代，表所有关节的角度

**send_angles(degrees, speed)**

- **功能：**  发送所有角度给机械臂所有关节
- **参数说明：**
  - `degrees`: `(List[float])`包含所有关节的角度 , 六轴机器人有六个关节所以长度为 6，四轴长度为4，如6轴的表示方法为：`[20,20,20,20,20,20]`
  - `speed`: 表示机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**set_encoders(encoders, sp)**

- **功能：** 发送电位值给机械臂所有关节
- **参数说明：**
  - `encoder`:表示机械臂的电位值，取值范围是 0 ~ 4096，六轴长度为6，四轴长度为4，如6轴的表示方法为：`[2048,2048,2048,2048,2048,2048]`
  - `sp`: 表示机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**sync_send_angles(degrees, speed, timeout=7)**

- **功能：** 同步发送角度，到达目标点返回
- **参数说明：**
  - `degrees`: 每个关节的角度值列表 `List[float]`
  - `speed`: ( `int`)机械臂运动的速度，取值范围是0-100
  - `timeout`：时间默认7s

**get_radians()**

- **功能：** 获取所有关节的弧度
- **返回值：** `list`包含所有关节弧度值的列表

**send_radians(radians, speed)**

- **功能：** 发送弧度值给机械臂所有关节
- **参数说明：**
  - `radians`：表示机械臂的弧度值，取值范围是 -5~5
- **返回值：** `list`包含所有关节弧度值的列表

### 案例使用


```python
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time

# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串， 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#    如:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 这里为 windows版本创建对象代码
mc = MyCobot("COM3", 115200)

# 通过传递角度参数，让机械臂每个关节移动到对应[0, 0, 0, 0, 0, 0]的位置
mc.send_angles([0, 0, 0, 0, 0, 0], 50)

# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2.5)

# 让关节1移动到90这个位置
mc.send_angle(Angle.J1.value, 90, 50)
# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2)

# 以下代码可以让机械臂左右摇摆
# 设置循环次数
num=5
while num > 0:
    # 让关节2移动到50这个位置
    mc.send_angle(Angle.J2.value, 50, 50)

    # 设置等待时间，确保机械臂已经到达指定位置
    time.sleep(1.5)

    # 让关节2移动到-50这个位置
    mc.send_angle(Angle.J2.value, -50, 50)

    # 设置等待时间，确保机械臂已经到达指定位置
    time.sleep(1.5)

    num -= 1

# 让机械臂缩起来。你可以手动摆动机械臂，然后使用get_angles()函数获得坐标数列，
# 通过该函数让机械臂到达你所想的位置。
mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)

# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2.5)

# 让机械臂放松，可以手动摆动机械臂
mc.release_all_servos()
```


## myBuddy

### 单关节控制

**send_angle(id, joint, angle, speed)**

- **功能:** 向机械臂发送单关节角度。

- **参数：**

  - `id`: 1/2/3 (左臂/右臂/腰部)

  - `joint`:   1 ~ 6

  - `angle`:   角度值

  - `speed`:   1 ~ 100

- **返回值:**
  - 无

**get_angle(id, joint_id)**

- **功能：** 获取单个关节的角度

- **参数：**

  - **id** (_int_) – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** (_int_) – 1 - 7（7 是夹爪）

**set_encoder（id，joint_id，encoder，speed)**

- **功能：** 发送单关节的encoder值

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** - 1 - 6。

  - **encoder** – 设置编码器的值。



### 多关节控制

**get_angles(id)**

- **功能:** 获取指定臂所有关节的度数。

- **参数**

    **id** – 1/2（左/右）

- **返回**

    长度为6的列表。

- **返回类型**

    列表

**send_angles（id，degrees，speed)**

- **功能:** 将所有角度发送到指定的机械臂

- **参数**

  - **id** – 1/2（左/右）。

  - **degrees** - [angle_list] len 6

  - **speed** - 1 - 100

**set_encoders（id，encoder，speed)**

- **功能:** 设置指定机械臂的六个关节同步执行到指定encoder位置。

- **参数**

  - **id** – 1/2（左/右）。

  - **encoders** - 编码器列表，长度为 6。

  - **speed** – 速度 1 ~ 100

**get_radians(id)**

- **功能:** 获取指定机械臂所有关节的弧度

- **参数**

    **id** – 1/2（左/右）

- **返回**

    浮动弧度列表 [radian1, ...]

- **返回类型**

    列表

**send_radians(id, radians, speed)**

- **功能:** 将指定机械臂所有关节的弧度发送给机械臂

- **参数**

  - **id** – 1/2（左/右）。

  - **radians** – 弧度值列表（List[float]），长度为 6

  - **speed** - (int)0 ~ 100



### 案例使用
```python
from pymycobot.mybuddy import MyBuddy
import time
mc = MyBuddy("/dev/ttyACM0", 115200)

# Send angles to the six joints of the left arm
mc.send_angles(1, [0, 0, 0, 0, 0, 0], 50)
time.sleep(3)

# Send the angle to the first joint of the left arm
mc.send_angle(1, 1, 90, 50)
time.sleep(2)

# Get the joint angle of the left arm
angles = mc.get_angles(1)
print("left angles: ",angles)

# Relax all joints of the left arm. Before running this command, please support the left arm with your hand to prevent it from falling suddenly
mc.release_all_servos(1)
```




## myPalletizer

### 案例使用

```python
from pymycobot.mypalletizer import MyPalletizer
from pymycobot.genre import Angle
import time
# 输入以上代码导入工程所需要的包

# 初始化一个myPalletizer对象，这里为Windows版本创建对象代码
mc = MyPalletizer("COM3",115200)
# 通过传递角度参数，让机械臂每个关节移动到对应[0, 0, 0, 0]的位置
mc.send_angles([0, 0, 0, 0,], 50)
# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2)

# 让关节1移动到20这个位置
mc.send_angle(1,20,50)
# 设置等待时间，确保机械臂已经到达指定位置
time.sleep(2)
# 设置变量num
num = 2
# 设置循环次数
while num > 0:
    mc.send_angle(2,20,50)
    time.sleep(2)
    mc.send_angle(2,(-20),50)
    time.sleep(2)
    num -= 1

# 让机械臂到达你所想的位置
mc.send_angles([-0.87, 41.66, -12.13, -0.17], 50)
# 让机械臂放松，可以手动摆动机械臂
mc.release_all_servos()
```

## myArm

### 案例使用

```python
from pymycobot.myarm import MyArm
from pymycobot.genre import Angle
import time
# 输入以上代码导入工程所需要的包

# 初始化一个myArm对象，这里为windows版本创建对象代码
mc = MyArm("/dev/ttyAMA0", 115200)


# 通过传递角度参数，让机械臂每个关节移动到对应[0, 0, 0, 0, 0, 0, 0]的位置 
mc.send_angles([0, 0, 0, 0, 0, 0, 0], 50)
# 设置等待时间，确保机械臂到达指定位置
time.sleep(2)

# 让关节1移动到90的位置
mc.send_angle(1,90,50)
# 设置等待时间，确保机械臂到达指定位置
time.sleep(2)

# 设置变量num
num=2
# 设置循环次数
while num>0:
  # 让关节2移动到40的位置
  mc.send_angle(2,40,50)
  time.sleep(2)
  # 让关节2移动到-40的位置
  mc.send_angle(2,(-40),50)
  time.sleep(2)
  num-=1

# 让机械臂到达指定的位置
mc.send_angles([-5.25,-30,-20,-12,-10,-10,10],50)
# 让机械臂放松，可手动摆动机械臂
mc.release_all_servos()
```

