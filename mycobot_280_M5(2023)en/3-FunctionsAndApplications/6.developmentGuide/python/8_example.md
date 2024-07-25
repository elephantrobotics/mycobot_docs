# Demonstration code 

The following are various use cases and operation result videos. You can copy the code for use or modification (the robot arm model used in the following cases is MyCobot 280. The parameters of different series of robot arms are different. Please pay attention to the modification).

**Note: ** The corresponding baud rates of various devices are different. Please refer to the information to understand their baud rates when using them. The serial port number can be viewed through [Calculator Device Manager](https://docs.elephantrobotics.com/docs/gitbook/4-BasicApplication/4.1-myStudio/4.1.1-myStudio_download_driverinstalled.html#4113-%E5%A6%82%E4%BD%95%E5%8C%BA%E5%88%86cp210x%E5%92%8Ccp34x%E8%8A%AF%E7%89%87) or the serial port assistant.

## Control RGB light board

### myCobot

```python
from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD  	# 当使用树莓派版本的mycobot时,可以引用这两个变量进行MyCobot初始化,如不是可不填该行代码
import time
#以上需写在代码开头,意为导入项目包

# MyCobot 类初始化需要两个参数：串口和波特率
#   第一个是串口字符串, 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#   以下为如:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 下面为 windows版本创建对象代码
mc = MyCobot("COM3", 115200)

i = 7
#循环7次
while i > 0:							
    mc.set_color(0,0,255) #蓝灯亮
    time.sleep(2)	#等2秒				
    mc.set_color(255,0,0) #红灯亮
    time.sleep(2)	#等2秒
    mc.set_color(0,255,0) #绿灯亮
    time.sleep(2)	#等2秒
    i -= 1
```

## Control the machine to return to the origin

```python
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时,可以引用这两个变量进行MyCobot初始化

# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串, 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#   Example:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 下面为树莓派版本创建对象代码
mc = MyCobot(PI_PORT, PI_BAUD)

# 检测机械臂是否可烧入程序
if mc.is_controller_connected() != 1:
    print("请正确连接机械臂进行程序写入")
    exit(0)

# 对机械臂进行微调,确保调整后的位置所有卡口都对齐了
# 以机械臂卡口对齐为准,这里给出的仅是个案例
mc.send_angles([0, 0, 0, 0, 0, 0], 30)

# 对此时的位置进行校准,校准后的角度位置表示[0,0,0,0,0,0],电位值表示[2048,2048,2048,2048,2048,2048]
# 该for循环相当于set_gripper_ini()这个方法
#for i in range(1, 7):
	#mc.set_servo_calibration(i)
```

## Single joint movement

```python
from pymycobot import MyCobot

from pymycobot.genre import Angle

import time

# MyCobot 类初始化需要两个参数：

#  第一个是串口字符串, 如：

#    linux： "/dev/ttyUSB0"

#    windows: "COM3"

#  第二个是波特率：

#    M5版本为： 115200

#

#  Example:

#    mycobot-M5:

#      linux:
#        mc = MyCobot("/dev/ttyUSB0", 115200)

#      windows:

#        mc = MyCobot("COM3", 115200)

#    mycobot-raspi:

#      mc = MyCobot(PI_PORT, PI_BAUD)

#

# 初始化一个MyCobot对象

# 下面为树莓派版本创建对象代码

# mc = MyCobot(PI_PORT, PI_BAUD)

# 下面为M5版本创建对象代码

mc=MyCobot('COM3',115200)

# 机械臂复原

mc.send_angles([0, 0, 0, 0, 0, 0], 40)

time.sleep(3)

# 控制关节3运动70°

mc.send_angle(Angle.J3.value,70,40)

time.sleep(3)

# 控制关节4运动-70°

mc.send_angle(Angle.J4.value,-70,40)

time.sleep(3)

# 控制关节1运动90°

mc.send_angle(Angle.J1.value,90,40)

time.sleep(3)

# 控制关节5运动-90°

mc.send_angle(Angle.J5.value,-90,40)

time.sleep(3)

# 控制关节5运动90°

mc.send_angle(Angle.J5.value,90,40)

time.sleep(3)
```



## **Multi-joint exercise**

```python
import time
from pymycobot import MyCobot
# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串, 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#   Example:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 下面为树莓派版本创建对象代码
# mc = MyCobot(PI_PORT, PI_BAUD)

# 280-M5版本创建对象代码
mc=MyCobot('COM3',115200)
# 机械臂复原归零
mc.send_angles([0,0,0,0,0,0],50)
time.sleep(2.5)
# 控制多个关节转动的不同角度
mc.send_angles([90,45,-90,90,-90,90],50)
time.sleep(2.5)
# 机械臂复原归零

mc.send_angles([0,0,0,0,0,0],50)
time.sleep(2.5)
# 控制多个关节转动的不同角度
mc.send_angles([-90,-45,90,-90,90,-90],50)
time.sleep(2.5)

```




##  Control the robot arm to swing left and right

```python
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时,可以引用这两个变量进行MyCobot初始化
import time
# 初始化一个MyCobot对象
# Pi版本
# mc = MyCobot(PI_PORT, PI_BAUD)
# M5版本
mc = MyCobot("COM3", 115200)
# 获得当前位置的坐标
angle_datas = mc.get_angles()
print(angle_datas)

# 用数列传递传递坐标参数,让机械臂移动到指定位置
mc.send_angles([0, 0, 0, 0, 0, 0], 50)
print(mc.is_paused())
# 设置等待时间,确保机械臂已经到达指定位置
# while not mc.is_paused():
time.sleep(2.5)

# 让关节1移动到90这个位置
mc.send_angle(Angle.J1.value, 90, 50)

# 设置等待时间,确保机械臂已经到达指定位置
time.sleep(2)

# 设置循环次数
num = 5

# 让机械臂左右摇摆
while num > 0:
    # 让关节2移动到50这个位置
    mc.send_angle(Angle.J2.value, 50, 50)
    # 设置等待时间,确保机械臂已经到达指定位置
    time.sleep(1.5)
    # 让关节2移动到-50这个位置
    mc.send_angle(Angle.J2.value, -50, 50)
    # 设置等待时间,确保机械臂已经到达指定位置
    time.sleep(1.5)
    num -= 1
# 让机械臂缩起来。你可以手动摆动机械臂,然后使用get_angles()函数获得坐标数列,
# 通过该函数让机械臂到达你所想的位置。
mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)

# 设置等待时间,确保机械臂已经到达指定位置
time.sleep(2.5)
# 让机械臂放松,可以手动摆动机械臂
mc.release_all_servos()


```


## Controlling the robotic arm to dances

```python
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时,可以引用这两个变量进行MyCobot初始化
import time

if __name__ == '__main__':
    # MyCobot 类初始化需要两个参数：
    #   第一个是串口字符串, 如：
    #       linux： "/dev/ttyUSB0"
    #       windows: "COM3"
    #   第二个是波特率：
    #       M5版本为： 115200
    #
    #   Example:
    #       mycobot-M5:
    #           linux:
    #              mc = MyCobot("/dev/ttyUSB0", 115200)
    #           windows:
    #              mc = MyCobot("COM3", 115200)
    #       mycobot-raspi:
    #           mc = MyCobot(PI_PORT, PI_BAUD)
    #
    # 初始化一个MyCobot对象
    # 下面为树莓派版本创建对象代码
    mc = MyCobot(PI_PORT, PI_BAUD)
    # M5版本
    # mc = MyCobot("COM3",115200)

    # 设置开始开始时间
    start = time.time()
    # 让机械臂到达指定位置
    mc.send_angles([-1.49, 115, -153.45, 30, -33.42, 137.9], 80)
    # 判断其是否到达指定位置
    while not mc.is_in_position([-1.49, 115, -153.45, 30, -33.42, 137.9], 0):
        # 让机械臂恢复运动
        mc.resume()
        # 让机械臂移动0.5s
        time.sleep(0.5)
        # 暂停机械臂移动
        mc.pause()
        # 判断移动是否超时
        if time.time() - start > 3:
            break
    # 设置开始时间
    start = time.time()
    # 让运动持续30秒
    while time.time() - start < 30:
        # 让机械臂快速到达该位置
        mc.send_angles([-1.49, 115, -153.45, 30, -33.42, 137.9], 80)
        # 将灯的颜色为[0,0,50]
        mc.set_color(0, 0, 50)
        time.sleep(0.7)
        # 让机械臂快速到达该位置
        mc.send_angles([-1.49, 55, -153.45, 80, 33.42, 137.9], 80)
        # 将灯的颜色为[0,50,0]
        mc.set_color(0, 50, 0)
        time.sleep(0.7)
```


## Gripper control

```python
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时,可以引用这两个变量进行MyCobot初始化
from pymycobot.mycobot import MyCobot
import time
def gripper_test(mc):
    print("Start check IO part of api\n")
    # 检测夹爪是否正在移动
    flag = mc.is_gripper_moving()
    print("Is gripper moving: {}".format(flag))
    time.sleep(1)

    # Set the current position to (2048).
    # Use it when you are sure you need it.
    # Gripper has been initialized for a long time. Generally, there
    # is no need to change the method.
    # mc.set_gripper_ini()
    # 设置关节点1,让其转动到2048这个位置
    mc.set_encoder(1, 2048)
    time.sleep(2)
    # 设置六个关节位,让机械臂以20的速度转动到该位置

    mc.set_encoders([1024, 1024, 1024, 1024, 1024, 1024], 20)
    # mc.set_encoders([2048, 2900, 2048, 2048, 2048, 2048], 20)
    # mc.set_encoders([2048, 3000,3000, 3000, 2048, 2048], 50)
    time.sleep(3)
    # 获取关节点1的位置信息
    print(mc.get_encoder(1))
    # 设置夹爪转动到2048这个位置
    mc.set_encoder(7, 2048)
    time.sleep(3)
    # 设置夹爪让其转到1300这个位置
    mc.set_encoder(7, 1300)
    time.sleep(3)

    # 以70的速度让夹爪到达2048状态,2048会报错,故改成255
    mc.set_gripper_value(255, 70)
    time.sleep(3)
    # 以70的速度让夹爪到达1500状态,1500会报错,故改成255
    mc.set_gripper_value(255, 70)
    time.sleep(3)
   
    num=5
    while num>0:
        # 设置夹爪的状态,让其以70的速度快速打开爪子
        mc.set_gripper_state(0, 70)
        time.sleep(3)
        # 设置夹爪的状态,让其以70的速度快速收拢爪子
        mc.set_gripper_state(1, 70)
        time.sleep(3)
        num-=1

    # 获取夹爪的值
    print("")
    print(mc.get_gripper_value())
    # mc.release_all_servos()

if __name__ == "__main__":
    # MyCobot 类初始化需要两个参数：
    #   第一个是串口字符串, 如：
    #       linux： "/dev/ttyUSB0"
    #       windows: "COM3"
    #   第二个是波特率：
    #       M5版本为： 115200
    #
    #   Example:
    #       mycobot-M5:
    #           linux:
    #              mc = MyCobot("/dev/ttyUSB0", 115200)
    #           windows:
    #              mc = MyCobot("COM3", 115200)
    #       mycobot-raspi:
    #           mc = MyCobot(PI_PORT, PI_BAUD)
    #
    # 初始化一个MyCobot对象
    # 下面为树莓派版本创建对象代码
    # mc = MyCobot(PI_PORT, PI_BAUD)
    # M5版本
    mc = MyCobot('COM3', 115200)
    # 让其移动到零位

    mc.set_encoders([2048, 2048, 2048, 2048, 2048, 2048], 20)
    time.sleep(3)
    gripper_test(mc)

```


## Suction pump control

280-M5版本

```python
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时,可以引用这两个变量进行MyCobot初始化
import time

# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串, 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
#
#   Example:
#       mycobot-M5:
#           linux:
#              mc = MyCobot("/dev/ttyUSB0", 115200)
#           windows:
#              mc = MyCobot("COM3", 115200)
#       mycobot-raspi:
#           mc = MyCobot(PI_PORT, PI_BAUD)
#
# 初始化一个MyCobot对象
# 下面为M5版本创建对象代码
mc =MyCobot('COM3',115200)
# 机械臂运动的位置
angles = [
            [92.9, -10.1, -60, 5.8, -2.02, -37.7],
            [92.9, -53.7, -83.05, 50.09, -0.43, -38.75],
            [92.9, -10.1, -87.27, 5.8, -2.02, -37.7]
        ]


# 开启吸泵
def pump_on():
    # 让2号位工作
    mc.set_basic_output(2, 0)
    # 让5号位工作
    mc.set_basic_output(5, 0)

# 停止吸泵
def pump_off():
    # 让2号位停止工作
    mc.set_basic_output(2, 1)
    # 让5号位停止工作
    mc.set_basic_output(5, 1)


# 机械臂复原
mc.send_angles([0, 0, 0, 0, 0, 0], 30)
time.sleep(3)

#开启吸泵
pump_on()
mc.send_angles(angles[2], 30)
time.sleep(2)

#吸取小物块
mc.send_angles(angles[1], 30)
time.sleep(2)
mc.send_angles(angles[0], 30)
time.sleep(2)
mc.send_angles(angles[1], 30)
time.sleep(2)

#关闭吸泵
pump_off()
mc.send_angles(angles[0], 40)
time.sleep(1.5)

```

