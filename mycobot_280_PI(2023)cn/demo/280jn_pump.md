# 机器人吸泵搬运木块案例

## 1 功能说明
机器人会使用吸泵将木块从A点搬运到B点

## 2 硬件安装
将乐高连接件插入吸泵上预留的插孔中
![](./img/p0.jpg)

将插好连接件的吸泵对准机械臂末端插孔插入
![](./img/p1.jpg)

选出公-母杜邦线，母头端插入吸泵方盒上标有引脚的插口
![](./img/p2.jpg)

![](./img/p3.jpg)

然后将线接到机械臂的底座IO
![](./img/JN.jpg)
> 左侧为吸泵引脚，右侧为机械臂引脚  
> GND -> GND  
> 5V -> 5V  
> G2 -> 21  
> G5 -> 20

## 3 吸泵测试
运行下面程序，吸泵会重复2次打开关闭的动作
```python
from pymycobot import MyCobot280
import time
import Jetson.GPIO as GPIO

arm = MyCobot280("/dev/ttyTHS1", 1000000)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
# 开启吸泵
def pump_on():
    GPIO.output(20, 0)
    time.sleep(0.05)

# 停止吸泵
def pump_off():
    GPIO.output(20, 1)
    time.sleep(0.05)
    GPIO.output(21, 0)
    time.sleep(1)
    GPIO.output(21, 1)
    time.sleep(0.05)

for i in range(2):
    pump_on()
    time.sleep(2)
    pump_off()
    time.sleep(2)
```

## 4 软件使用
利用myblockly的快速移动功能，对木块的抓取点和放置点进行示教，并且记录下位置信息,示教完后，需要断开串口的连接，否则会在运行python脚本时，报串口被占用的错误
![](./img/blockly.png)

## 5 复合应用
```python
from pymycobot import MyCobot280
import time
import Jetson.GPIO as GPIO
init_angles=[18.36, 6.5, -124.45, 26.54, -1.84, -110.47]#初始位置的6个关节角度
grab_point=[158.4, -66.9, 77.9, 179.01, 0.88, 52.41]#抓取点的坐标
place_point=[158.4, 36.9, 77.9, 179.01, 0.88, 52.41]#放置点的坐标

arm = MyCobot280("/dev/ttyTHS1", 1000000)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# 开启吸泵
def pump_on():
    GPIO.output(20, 0)
    time.sleep(0.05)

# 停止吸泵
def pump_off():
    GPIO.output(20, 1)
    time.sleep(0.05)
    GPIO.output(21, 0)
    time.sleep(1)
    GPIO.output(21, 1)
    time.sleep(0.05)

if __name__=="__main__":
    pump_off()#先关闭吸泵 
    time.sleep(1)  
    arm.send_angles(init_angles,100)#运动初始位置
    time.sleep(2)
    arm.send_coords([grab_point[0],grab_point[1],grab_point[2]+70,grab_point[3],grab_point[4],grab_point[5]],100,1)#运动到抓取点上方70mm
    time.sleep(2)
    arm.send_coords([grab_point[0],grab_point[1],grab_point[2],grab_point[3],grab_point[4],grab_point[5]],100,1)#运动到抓取点
    time.sleep(2)
    pump_on() #打开吸泵
    time.sleep(1)
    arm.send_coords([grab_point[0],grab_point[1],grab_point[2]+70,grab_point[3],grab_point[4],grab_point[5]],100,1)#运动到抓取点上方70mm
    time.sleep(2)

    arm.send_coords([place_point[0],place_point[1],place_point[2]+70,place_point[3],place_point[4],place_point[5]],100,1)#运动到放置点上方70mm
    time.sleep(2)
    arm.send_coords([place_point[0],place_point[1],place_point[2],place_point[3],place_point[4],place_point[5]],100,1)#运动到放置点
    time.sleep(2)
    pump_off() #关闭吸泵
    time.sleep(1)
    arm.send_coords([place_point[0],place_point[1],place_point[2]+70,place_point[3],place_point[4],place_point[5]],100,1)#运动到放置点上方70mm
    time.sleep(2)
    
```

## 6 效果展示
![](./img/jn_pump.gif)