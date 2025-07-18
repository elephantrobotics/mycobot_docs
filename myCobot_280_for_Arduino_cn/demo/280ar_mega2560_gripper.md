# 机器人夹爪搬运木块案例

## 1 设备说明

myCobot 280 Arduino + MEGA 2560开发板 + myCobot 自适应夹爪

## 2 功能说明

机器人会使用夹爪将木块从A点搬运到B点，夹取成功后LED灯板会点亮

## 3 硬件安装

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/MEGA2560_Hardware_Installation.mp4" type='video/mp4' >
</video>

## 4 夹爪测试

运行下面程序，夹爪会重复2次闭合张

```python
from pymycobot import MyCobot280,utils
import time

arm=MyCobot280(utils.get_port_list()[0], 115200) # 波特率默认是115200，部分板子是1000000，请根据实际进行修改
time.sleep(2)

for i in range(2):
    arm.set_gripper_state(0,100)
    time.sleep(2)
    arm.set_gripper_state(1,100)
    time.sleep(2)
```

## 5 原理说明

使用MEGA 2560开发板控制一个 MyCobot 280 Arduino 机械臂，配合夹爪（Gripper）完成如下操作流程：

1. **初始化和回零：**

    - 连接串口；

    - 移动至初始位置；

    - 打开夹爪（确保未夹东西）；

2. **抓取阶段（A 点）：**

    - 移动至 A 点坐标；

    - 夹爪闭合，抓住木块；

    - 返回初始位置；

    - 点亮黄色灯光（提示抓取成功）；

3. **搬运与释放（B 点）：**

    - 机械臂移动到 B 点上方；

    - 降至 B 点坐标；

    - 打开夹爪释放木块；

    - 回到 B 点上方，再返回初始位置；

    - 点亮绿色灯光（提示搬运成功）。

## 6 复合应用

```python
import time
from pymycobot import *  # 导入 MyCobot 控制库
from pymycobot.utils import get_port_list  # 获取串口列表工具

# 获取所有可用串口
plist = get_port_list()

# 初始化 MyCobot 280 机械臂，连接串口，波特率为 115200, 部分板子是1000000，请根据实际进行修改
mc = MyCobot280(plist[0], 115200)
time.sleep(0.5)

# 设置通用变量
speed = 60             # 移动速度
wait_time = 2.5        # 等待时间（秒）
go_home = [0, 0, 0, 0, 0, 0]  # 机械臂回零位置（关节角度）

# 初始姿态角度（避开物体区域）
init_pos = [5.44, -13.88, -73.82, 3.42, 0.43, -30.84]

# A 点坐标（抓取点）
A_coords = [203.6, -46.9, 100.6, -176.88, -1.29, -55.39]

# B 点上方的关节角度
B_up_angles = [89.12, -15.55, -75.32, 2.02, 0.87, -30.23]

# B 点坐标（释放点）
B_coords = [64.1, 198.2, 112.4, -177.53, -0.82, 29.78]


# 打开夹爪（张开）
def gripper_on():
    mc.set_gripper_state(0, 100)  # 0 表示张开
    time.sleep(0.05)

# 关闭夹爪（夹紧）
def gripper_off():
    mc.set_gripper_state(1, 100)  # 1 表示闭合
    time.sleep(0.05)


# 主流程函数
def main():
    # 回到初始零位
    mc.send_angles(go_home, speed)
    time.sleep(wait_time)

    # 移动到初始安全位置
    mc.send_angles(init_pos, speed)
    time.sleep(wait_time)

    # 打开夹爪准备抓取
    gripper_on()

    # 移动到 A 点抓取木块
    mc.send_coords(A_coords, speed, 1)
    time.sleep(wait_time)

    # 夹紧木块
    gripper_off()

    # 返回初始位置
    mc.send_angles(init_pos, speed)
    time.sleep(wait_time)

    # 抓取成功，点亮黄灯作为提示
    mc.set_color(255, 255, 0)  # 黄色灯光（R=255, G=255, B=0）

    # 移动到 B 点上方准备放置
    mc.send_angles(B_up_angles, speed)
    time.sleep(wait_time)

    # 降到 B 点坐标进行放置
    mc.send_coords(B_coords, speed, 1)
    time.sleep(2)

    # 松开夹爪，释放木块
    gripper_on()

    # 抬起机械臂回到 B 点上方
    mc.send_angles(B_up_angles, speed)
    time.sleep(wait_time)

    # 回到初始位置
    mc.send_angles(init_pos, speed)
    time.sleep(wait_time)

    # 搬运完成，点亮绿灯作为提示
    mc.set_color(0, 255, 0)  # 绿色灯光（R=0, G=255, B=0）


if __name__ == '__main__':
    main()
    
```

## 7 效果展示

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
  <source src="./img/MEGA2560_Effect.mp4" type='video/mp4' >
</video>