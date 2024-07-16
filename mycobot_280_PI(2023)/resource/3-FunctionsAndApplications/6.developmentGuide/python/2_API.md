# API说明

API(Application Programming Interface)，即应用程序接口函数，是一些预先定义好的函数。在使用下列函数接口的时候请先在开头导入我们的API库，即输入下方代码，否则无法运行成功：

```python
#适用于myCobot、mechArm系列
from pymycobot.mycobot import MyCobot

#适用于myPalletizer系列
from pymycobot.mypalletizer import MyPalletizer

#适用于myBuddy系列
from pymycobot.mybuddy import MyBuddy

# 适用于myArm
from pymycobot.myarm import MyArm
```

> **注意：**个别函数接口有返回值，但是直接输入代码，返回的结果是没有返回值的，需要使用`print`函数把结果打印出来。比如，想要获取机械臂当前设置的速度值可使用`get_speed()`，但是直接输入该函数是没有结果的，正确写法是：`print(get_speed())`即可把速度值打印出来。下面对API说明部分如果标注**无返回值**，则不需要使用`print`函数，反之则需使用`print`函数打印结果。


## myCobot / myPalletizer / mechArm / myArm

### 1 机械臂整体运行状态

**1.1** `power_on()`

- **功能：** 机械臂上电
- **返回值：** 无

**1.2** `power_off()`

- **功能：** 机械臂断电，所有功能将失效
- **返回值：** 无

**1.3** `is power on()`

* **功能**：判断机械臂是否上电

- **返回值：**	1- 机械臂已通电		 0 - 机械臂已断电		-1- 错误  

**1.4** `release_all_servos`	   

- **功能：** 设置机械臂为自由移动模式(能手动自由摆动机械臂)
- **返回值：** 无

**1.5** `is_controller_connected`			 

- **功能：** 判断是否与 Atom 连接
- **返回值：**	1- 已连接		 0 - 未连接		-1- 错误  

**1.6** `read_next_error()`

- **功能：** 机械臂错误检测
- **返回值：**  0- 无异常    1 - 通讯中断    2 - 通讯不稳定    3 - 舵机异常

**1.7** `set_fresh_mode(mode)`

- **功能：**：设置插补/刷新运动模式
- **参数说明：** mode:  0：按序执行指令   1: 执行第一个指令
- **返回值：**	1- 机械臂已通电		 0 - 机械臂已断电		-1- 错误  

**1.8** `get_fresh_mode()`

- **功能：**：查询插补/刷新运动模式

- **返回值：**	0：按序执行指令   1: 执行第一个指令

### 2 机械臂运行状态和设置

**2.1** `pause()`					    

- **功能：** 让机械臂暂停当前运动
- **返回值：** 无

**2.2** `stop()`						  

- **功能：** 让机械臂停止所有运动
- **返回值：** 无

**2.3** `resume()`					  

- **功能：** 让机械臂恢复之前所设置的运动
- **返回值：** 无

**2.4** `is_paused()`				

- **功能：** 判断机械臂是否为暂停状态
- **返回值：** 	1 - 已经暂停		 	   0 - 没有暂停		      -1 - 错误 

**2.5** `get_speed()`			 

- **功能：** 获取机器人的运动速度
- **返回值：** 机器人当前所设定的运行速度，范围在1-100

**2.6** `set_speed(speed)`

- **功能：** 设置机器人的运动速度
- **参数说明：** speed: 给入你想要设置的速度范围在1-100，单位为mm/s
- **返回值：** 无

**2.7** `get_joint_min_angle(joint_id)`

- **功能：** 获取指定关节最小能运行到的角度
- **参数说明：**`joint_id`: (`int`) 您所指定的关节，mycobot系列范围为1~6，mypalletizer系列范围为1-4，myArm系列范围为1-7
- **返回值：** `angle`: 返回来的度数

**2.8** `get_joint_max_angle(joint_id)`

- **功能：** 获取指定关节最大能运行到的角度
- **参数说明：** `joint_id`: (`int`)您所指定的机械臂关节关节，mycobot系列范围为1~6，mypalletizer系列范围为1-4，myArm系列范围为1-7
- **返回值：** `angle`: (`float`)返回来的度数

**2.9** `is_servo_enable(servo id)`

- **功能：** 判断指定关节是否连通
- **参数说明：** servo id: 你所指定的关节，mycobot系列范围为1~6，mypalletizer系列范围为1-4，myArm系列范围为1-7
- **返回值：** (int)        1 - 连通         0 - 不连通          -1 - 错误

**2.10** `is_all_servo_enable()`

- **功能：** 判断机器人的所有关节是否连通
- **返回值：** (int)         1 - 连通           0 - 不连通          -1 - 错误

**2.11** `release_servo(servo_id)`

- **功能：** 放松指定的关节
- **参数说明：** servo id: (`int`)机械臂的指定关节,mycobot系列范围为1~6，mypalletizer系列范围为1-4，myArm系列范围为1-7
- **返回值：** 无

**2.12** `get_tof_distance()`

- **功能：** 获取检测到的距离(需要外部距离检测器)
- **返回值：** 检测到的距离值，单位为mm。

**2.13** `get_error_information()`

- **功能：** 获取错误信息
- **返回值：** 
  - 0: 无错误信息.
  - 1 ~ 6: 对应的关节超出限位.
  - 16 ~ 19: 碰撞保护.
  - 32: 运动学逆解无解.
  - 33 ~ 34: 直线运动无相邻解.

**2.14** `clear_error_information()`

- **功能：** 清除错误信息

**2.15** `set_joint_min(id, angle)`

- **功能：** 设置指定关节最小能运行到的角度
- **参数说明：** 
  - `id`: (`int`)机械臂的指定关节,范围为1~6
  - `angle`:关节可运行的最小角度
- **返回值：** 无

**2.16** `set_joint_max(id, angle)`

- **功能：** 设置指定关节最大能运行到的角度
- **参数说明：** 
  - `id`: (`int`)机械臂的指定关节,范围为1~6
  - `angle`:关节可运行的最大角度
- **返回值：** 无


**2.17** `get_basic_version()`

- **功能：** 获取固件版本
- **返回值：** 固件版本(`float`)


**2.18** `set_communicate_mode(mode)`

- **功能：** 设置basic通讯模式
- **参数说明：** (`int`) 0 - 关闭   1-打开
- **返回值：** 无


### 3 输入程序控制模式(MDI模式)

  > **注意：**不同系列的机械臂限位有所不同，可设定姿态数值也有所不同具体可查看对应型号的参数介绍

**3.1** `get_angles()`

- **功能：** 获取所有关节角度
- **返回值：** `list`一个浮点值的列表代，表示所有关节的角度

**3.2** `send_angle(id, degree, speed)`

- **功能：** 发送指定的单个关节运动至指定的角度
- **参数说明：**
  - `id`: 代表机械臂的关节，六轴有六个关节，四轴有四个关节，有特定的表示方法
    关节一的表示法：`Angle.J1.value`。(也可以用数字1-6来表示)
  - `degree`: 表示关节的角度
  - `speed`：表示机械臂运动的速度，范围0~100
- **返回值：** 无

**3.3** `send_angles(degrees, speed)`

- **功能：**  发送所有角度给机械臂所有关节
- **参数说明：**
  - `degrees`: (List[float])包含所有关节的角度 ,六轴机器人有六个关节所以长度为 6，四轴长度为4，表示方法为：[20,20,20,20,20,20]
  - `speed`: 表示机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**3.4** `get_coords()`

- **功能：** 获取当前坐标和姿态
- **返回值：** `list`包含坐标和姿态的列表
  - 六轴：长度为 6，依次为 `[x, y, z, rx, ry, rz]`
  - 四轴：长度为 6，依次为 `[x, y, z, rx]`

**3.5** `send_coord(id,coord,speed)`

- **功能：** 发送单个坐标值给机械臂进行移动
- **参数说明：**
  - `id`:代表机械臂的坐标，六轴有六个坐标，四轴有四个坐标，有特定的表示方法
    X坐标的表示法：`Coord.X.value`，也有简易的表示方法：如X轴可以填写1,Y填写2,以此类推
  - `coord`: 输入您想要到达的坐标值
  - `speed`: 表示机械臂运动的速度，范围是0-100
- **返回值：** 无

**3.6** `send_coords(coords, speed, mode)`

- **功能：** 发送整体坐标和姿态,让机械臂头部从原来点移动到您指定点
- **参数说明：**
  - `coords`: 
    - 六轴：[x,y,z,rx,ry,rz]的坐标值，长度为6
    - 四轴：[x,y,z,rx]的坐标值，长度为4
  - `speed`: 表示机械臂运动的速度，范围是0-100
  - `mode`: ( `int`): 取值限定 0 和 1
    - 0 表示机械臂头部移动的路径为非线性，即随机规划路线，只要机械臂头部以保持规定的姿态移动到指定点即可。
    - 1 表示机械臂头部移动的路径为线性的，即智能规划路线让机械臂头部以直线的方式移动到指定点。
- **返回值：** 无

**3.7** `get_encoders()`

- **功能：** 获取机械臂所有关节的电位值
- **返回值：** `list`包含机械臂所有关节电位值的列表

**3.8** `get_encoder(joint_id)`

- **功能：** 获取机械臂指定的单个关节的电位值
- **参数说明：**
  - `joint_id`: 代表机械臂的关节，六轴机器人有六个关节所以长度为 6，四轴长度为4，有特定的表示方法,
    关节一的表示法：`Angle.J1.value`(也可以用数字1-6来表示)
- **返回值：** 您所指定的单个关节电位值

**3.9** `set_encoder(joint_id, encoder)`

- **功能：** 发送指定的单个关节运动至指定的电位值
- **参数说明：**
  - `joint_id`: 代表机械臂的关节，六轴机器人有六个关节所以长度为 6，四轴长度为4，有特定的表示方法,
    关节一的表示法：`Angle.J1.value`(也可以用数字1-6来表示)
  - `encoder`:表示机械臂的电位值，取值范围是 0 ~ 4096
- **返回值：** 无

**3.10** `set_encoders(encoders, sp)`

- **功能：** 发送电位值给机械臂所有关节
- **参数说明：**
  - `encoder`:表示机械臂的电位值，取值范围是 0 ~ 4096，六轴长度为6，四轴长度为4，表示方法为：[2048,2048,2048,2048,2048,2048]
  - `sp`: 表示机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**3.11** `get_radians()`

- **功能：** 获取所有关节的弧度
- **返回值：** `list`包含所有关节弧度值的列表

**3.12** `send_radians(radians, speed)`

- **功能：** 发送弧度值给机械臂所有关节
- **参数说明：**
  - `radians`:表示机械臂的弧度值
- **返回值：** 无

**3.13** `sync_send_angles(degrees, speed, timeout=7)`

- **功能：** 同步发送角度，到达目标点返回
- **参数说明：**
  - `degrees`: 每个关节的角度值列表( `List[float]`)
  - `speed`: ( `int`)机械臂运动的速度，取值范围是0-100。
  - `timeout`：时间默认7s
- **返回值：** 无

**3.14** `sync_send_coords(coords, speed, mode)`

- **功能：** 同步发送坐标，到达目标点返回
- **参数说明：**
  - `coords`: 坐标值列表( `List[float]`)，
    - 六轴：长度为 6，依次为 `[x, y, z, rx, ry, rz]`
    - 四轴：长度为 6，依次为 `[x, y, z, rx]`
  - `speed`: ( `int`)机械臂运动的速度，取值范围是0-100
- **返回值：** 无

**3.15** `is_in_position(data, flag)`		

- **功能：** 判断机器人有没有到达指定的位置
- **参数说明：**
  - `data`: 您给出的一组数据可以是角度也可以是坐标值,如：[10,20,20,10,20,10]
  - `flag`: 数据类型(取值范围0或1)
    - `0`: 表示给入的数值是角度值
    - `1`: 表示给入的数值是坐标值
- **返回值：**  1 - 已到达        0 - 未到达           -1 - 错误

**3.16** `is_moving()`			 

- **功能：** 判断机械臂有没有移动
- **返回值：** 1 - 正在移动		0 - 没有移动		-1 - 错误

**3.17** `set_color(r, g, b)`

- **功能：** 设置机器人手臂顶部的灯光颜色(LED灯光控制)
- **参数说明：** r，g，b表示机器人顶部的灯光颜色值
  - `r`: 0 ~ 255
  - `g`: 0 ~ 255
  - `b`: 0 ~ 255
- **返回值：** 无


**3.18** `set_encoders_drag(encoders, speeds)`

- **功能：** 发送所有的电位值和速度
- **参数说明：**
  - `encoders`：机械臂所有关节的电位值(list)
  - `speed`：机械臂所有关节的速度
- **返回值：** 无


**3.19** `get_solution_angles()`			 

- **功能：** 获得偏转角度值(仅作用于MyArm)
- **返回值：** 无


**3.20** `set_solution_angles(angle, speed)`			 

- **功能：** 设置偏转角度值(仅作用于MyArm)
- **参数说明：**
  - `angle`：第一关节的角度
  - `speed`：速度(0 - 100)
- **返回值：** 无


**3.21** `set_solution_angles(angle, speed)`			 

- **功能：** 设置偏转角度值(仅作用于MyArm)
- **参数说明：**
  - `angle`：第一关节的角度
  - `speed`：速度(0 - 100)
- **返回值：** 无


**3.16** `set_solution_angles(angle, speed)`			 

- **功能：** 设置偏转角度值(仅作用于MyArm)
- **参数说明：**
  - `angle`：第一关节的角度
  - `speed`：速度(0 - 100)
- **返回值：** 无

**3.17** `get_transponder_mode()`			 

- **功能：** 获得串口传输的配置信息(仅作用于MyArm)
- **返回值：** 无
  - `0`：关闭透传
  - `1`：打开透传，检测所有数据
  - `2`：打开透传，只检测通信转发模式的配置信息(默认为0)

**3.18** `set_transponder_mode(mode)`			 

- **功能：** 设置串口传输模式(仅作用于MyArm)
- **参数说明：**
  - `0`：关闭透传
  - `1`：打开透传，检测所有数据
  - `2`：打开透传，只检测通信转发模式的配置信息
- **返回值：** 无

### 4  JOG 模式和操作

**4.1** `jog_angle(joint_id, direction, speed)`

- **功能：** 控制机器人按照指定的角度持续移动
- **参数说明：**
  - `joint_id`: 代表机械臂的关节，按照关节id给入1~6来表示
  - `direction`: 主要控制机器臂移动的方向，给入0 为负值移动，给入1为正值移动
  - `speed`: 速度 0 ~ 100
- **返回值：** 无

**4.2** `jog_coord(coord_id, direction, speed)`

- **功能：** 控制机器人按照指定的坐标或姿态值持续移动
- **参数说明：**
  - `coord_id`：代表机械臂的关节，按照关节id给入1~6来表示
  - `direction`：主要控制机器臂移动的方向，给入0 为负值移动，给入1为正值移动
  - `speed`：速度 0 ~ 100
- **返回值：** 无

**4.3** `jog_stop()`

- **功能：** 停止 jog 控制下的持续移动
- **返回值：** 无

**4.4** `jog_absolute(joint_id, angle, speed)`

- **功能：** 控制机器人的特定关节运动到指定角度
- **参数说明：**
  - `joint_id`：代表机械臂的关节，按照关节id给入1~6来表示
  - `angle`：指定关节运动的角度
  - `speed`：速度 0 ~ 100
- **返回值：** 无

**4.5** `jog_increment(joint_id, angle, speed)`

- **功能：** 步进模式，使运动角度以给定的增量运行
- **参数说明：**
  - `joint_id`：代表机械臂的关节，按照关节id给入1~6来表示
  - `angle`：增量范围
  - `speed`：速度 0 ~ 100
- **返回值：** 无


### 5 舵机控制与操作

<!-- **5.1** `set_servo_data(servo_no, data_id, value)`

- **功能：** 设置舵机指定地址的数据参数
- **参数说明：** 
  - `servo_no`：舵机的序列号，按照关节id给入1 - 6
  - `data_id`：数据地址
  - `value`: 取值范围0 - 4096
- **返回值：** 无

**5.2** `get_servo_data(servo_no, data_id)`

- **功能：** 读取舵机指定地址的数据参数。
- **参数说明：** 
  - `servo_no`：各个舵机的序列号，按照关节id给入1 - 6
  - `data_id`：数据地址
- **返回值：** 数据参数值，范围0-4096 -->

**5.1** `set_servo_calibration(servo_no)`

- **功能：** 校准指定关节，设置当前位置为角度零点，对应电位值为2048
- **参数说明：** servo_no:(`int`)：机械臂的指定关节，mycobot系列范围为1~6，mypalletizer系列范围为1-4，myArm系列范围为1-7
- **返回值：** 无

**5.2** `focus_servo(servo_id)`

- **功能：** 给指定关节上电
- **参数说明：** servo id: (`int`)：机械臂的指定关节,mycobot系列范围为1~6，mypalletizer系列范围为1-4，myArm系列范围为1-7
- **返回值：** 无

**5.3** `joint_brake(joint_id)`

- **功能：** 在关节运动的状态下使其停止运动，缓冲距离与现有速度正相关
- **参数说明：** joint_id: (`int`)：机械臂的指定关节,范围为1~7
- **返回值：** 无

**5.4** `get_servo_speeds()`

- **功能：** 获得关节运行速度
- **返回值：** (`list`)每个关节的运行速度

**5.5** `get_servo_currents()`

- **功能：** 获得关节当前运行速度
- **返回值：** (`list`)每个关节的速度

**5.6** `get_servo_voltages()`

- **功能：** 获得关节电压
- **返回值：** (`list`)每个关节的电压

**5.7** `get_servo_status()`

- **功能：** 获得关节状态
- **返回值：** (`list`)每个关节的状态


**5.8** `get_servo_temps()`

- **功能：** 获得关节的温度
- **返回值：** (`list`)每个关节的温度


### 6 Atom 末端IO控制

**6.1** `set_pin_mode(pin_no, pin_mode)`

- **功能：** 设置 atom 中指定引脚的状态模式
- **参数说明：**
  - `pin_no` (int)：机器人顶部的具体引脚号
  - `pin_mode` (int)： 限定0~2
    - 0设置为运行状态
    - 1设置为停止状态
    - 2设置为上拉模式
- **返回值：** 无

**6.2** `set_digital_output(pin_no, pin_signa)`

- **功能：** 设置末端引脚号的工作状态
- **参数说明：**
  - `pin_no`( `int`) 设备末端标注的编号仅取数字部分
  - `pin_signal`( `int`): 输入0表示设置为运行状态，输入1表示停止状态
- **返回值：** 无

**6.3** `get_digital_input(self, pin_no):`

- **功能：** 获取末端引脚号的工作状态
- **参数说明:** `pin_no`：表示机器人末端的具体引脚号
- **返回值：** `pin_signal`( `int`) 当返回的值为0表示在工作状态运行，1表示停止状态

**6.4** `set_pwm_output(channel, frequency, pin_val):`

- **功能：** 脉宽调制控制
- **参数说明:** 
  - `channel`(`int`)：机器人顶部的具体引脚号
  - `frequency`(`int`):时钟频率
  - `pin_val`(`int`):占空比0~256；128为50%
- **返回值：** 无


### 7 夹爪控制

**7.1** `is_gripper_moving( )`

- **功能：** 判断夹爪是否正在运行
- **返回值：**
  - `0 ` ：表示机械臂的夹爪没有运行
  - `1` ：表示机械臂的夹爪正在运行
  - `-1`：表示出错

**7.2** `set_gripper_value(value, speed, gripper_type=None)`

- **功能：** 让夹爪以指定的速度转动到指定的位置
- **参数说明：**
  - `value`：表示夹爪所要到达的位置，取值范围 0~100
  - `speed`：表示以多少的速度转动，取值范围 0~100
  - `gripper_type`：夹爪类型，默认是自适应夹爪
    - `1`: 自适应夹爪
    - `3`: 平行夹爪
    - `4`: 柔性夹爪
- **返回值：** 无

**7.3** `get_gripper_value(gripper_type=None)`

- **功能：** 获取夹爪的当前位置数据信息
- **参数说明：**
  - `gripper_type`：夹爪类型，默认是自适应夹爪
    - `1`: 自适应夹爪
    - `3`: 平行夹爪
    - `4`: 柔性夹爪
- **返回值：** 夹爪的数据信息

**7.4** `set_gripper_state(flag, speed， _type=None)`

- **功能：** 让夹爪以指定的速度进入到指定的状态
- **参数说明：**
  - `flag`：1 表示夹爪合拢状态，0 表示夹爪打开状态。
  - `speed`：表示以多快的速度达到指定的状态，取值范围 0~100
  - `_type`: 夹爪类型，默认是自适应夹爪
    - `1`: 自适应夹爪
    - `2`: 五指灵巧手
    - `3`: 平行夹爪
    - `4`: 柔性夹爪
- **返回值：** 无

**7.5** `move_round()`

- **功能：** 驱动四子棋舵机逆时针转一圈，走完一圈需要1.5s


**7.6** `set_eletric_gripper(status)`

- **功能：** 设置夹爪模式(仅作用于350)
- **参数说明：**  `status`：1 表示夹爪合拢状态，0 表示夹爪打开状态。
- **返回值：** 无

**7.7** `set_gripper_mode(status)`

- **功能：** 设置夹爪模式
- **参数说明：**  `status`：1 透传模式，0 I/O模式
- **返回值：** 无


**7.8** `get_gripper_mode()`

- **功能：** 获取夹爪状态
- **返回值：** `status(int)`：0 - 透传模式  1 - I/O模式

**7.9** `set_HTS_gripper_torque(torque)`

- **功能：** 设置自适应夹爪力矩
- **参数说明：**
  - `torque`：150 ~ 900
- **返回值：** 0 - 设置失败；1 - 设置成功

**7.10** `get_HTS_gripper_torque()`

- **功能：** 获取自适应夹爪力矩
- **返回值：** 150 ~ 900

**7.11** `get_gripper_protect_current()`

- **功能：** 获取夹爪保护电流
- **返回值：** 1 ~ 500

**7.12** `init_gripper()`

- **功能：** 初始化夹爪
- **返回值：** 0 - 初始化失败；1 -初始化成功

**7.13** `set_gripper_protect_current(current)`

- **功能：** 设置夹爪保护电流
- **参数说明：**
  - `current`：1 ~ 500
- **返回值：** 0 - 初始化失败；1 -初始化成功

### 8 底座BasicIO控制

**8.1** `get_basic_input(pin_no)`

- **功能：** 获取底部引脚号的工作状态
- **参数说明:** `pin_no`：表示机器人底部的具体引脚号。
- **返回值：** `pin_signal`( `int`) 当返回的值为0表示在工作状态运行，1表示停止状态

**8.2** `set_basic_output(pin_no, pin_signal)`

- **功能：** 设置底部引脚号的工作状态。
- **参数说明：**
  - `pin_no`( `int`) 设备底部标注的编号仅取数字部分
  - `pin_signal`( `int`): 输入0表示设置为运行状态，输入1表示停止状态
- **返回值：** 无


### 9 socket 通信

> 机械臂需要开启服务端，服务端文件在[这里](https://github.com/elephantrobotics/pymycobot/blob/main/demo/Server.py).

```python
# for mycobot,mecharm
from pymycobot import MyCobotSocket

mc = MyCobotSocket("192.168.1.10", 9000)

print(mc.get_angles())

```


### 10 TCPIP

**10.1** `set_ssid_pwd(account, password)`

- **功能：** 更改连接的wifi(适用于m5或seed)
- **参数说明:** 
  - `account`( `str`) ：新的 wifi 帐户
  - `password`( `str`)：新的 wifi 密码
- **返回值：**  无

**10.2** `get_ssid_pwd()`

- **功能：** 获取连接的wifi账号和密码(适用于m5或seed)
- **返回值：** 当前连接的wifi账号和密码

**10.3** `set_server_port(port)`

- **功能：** 更改服务器的连接端口
- **参数说明:** 
  - `port`( `int`) 服务器的新连接端口
- **返回值：**  无


### 11 utils(模块)

该模块支持一些帮助方法，使用之前在文件开头输入代码导入模块：

```python
from pymycobot import utils
```

**11.1** `utils.get_port_list()`

- **功能：** 获取当前所有串口号列表
- **返回值：** 串口列表( `list`)

**11.2** `utils.detect_port_of_basic()`

- **功能：** 返回第一个检测到的 M5 Basic 的串口号。(只会返回一个串口号)
- **返回值：** 返回检测到的端口号，如果没有监测到串口号则返回：`None`



### 12 树莓派——GPIO

当您的机械臂为树莓派版本时，您可以用到以下API。同时在使用API之前需在文件开头输入代码导入：

```python
from pymycobot import MyCobot
```

**12.1** `gpio_init()`

- **功能：** 初始化 GPIO 模块，设置 BCM 模式
- **返回值：** 无

**12.2** `set_gpio_mode`

- **功能：** 设置树莓派GPIO针脚模式
- **参数**
  - `mode` (`str`) 输入："BCM" 或者 "BOARD" 进入相应模式

**12.3** `set_gpio_output(pin_no, state)`

- **功能：** 将引脚设置为高，低电平
- **参数说明:** 
  - `pin`( `int`) 引脚编号
  - `state`：0设置为低电平    1设置为高电平
- **返回值：**  无

**12.4**  `get_gpio_in(pin_no)`

- **功能：** 获取引脚电平状态
- **参数说明:** 
  - `pin_no`( `int`) 引脚编号
- **返回值：**  0为低电平    1为高电平

**12.5**  `gpio_output(pin,v)`

- **功能：** 设置GPIO输出值
- **参数说明:** 
  - `pin_no`( `int`) 引脚编号
  - `v`(`int`): 0设置为低电平    1设置为高电平
- **返回值：**  无

**12.6**  `set_gpio_out(pin_no, mode)`

- **功能：** 设置引脚作为输入或者输出
- **参数说明:** 
  - `pin`( `int`) 引脚编号
  - `mode`(`str`)：in - 输入 ； out - 输出
- **返回值：**  无
  

### 13 坐标变换

**13.1** `get_tool_reference()`

- **功能：** 获取工具坐标系
- **返回值：**  (`list`)[x, y, z, rx, ry, rz]

**13.2** `set_tool_reference(coords)`

- **功能：** 设置工具坐标系
- **参数说明:**  (`list`)[x, y, z, rx, ry, rz]
- **返回值：**  无


**13.3** `set_world_reference(coords)`

- **功能：** 设置世界坐标系
- **参数说明:** (`list`)[x, y, z, rx, ry, rz]
- **返回值：**  无

**13.4** `get_world_reference()`

- **功能：** 获取世界坐标系
- **返回值：**  (`list`)[x, y, z, rx, ry, rz]

**13.5** `set_reference_frame(rftype)`

- **功能：** 设置基坐标系
- **返回值：**  `rftype`: 0 - 基坐标(默认)    1 - 世界坐标


**13.6** `get_reference_frame()`

- **功能：** 获取基坐标系
- **返回值：**  (`list`)[x, y, z, rx, ry, rz]


**13.7** `set_movement_type(move_type)`

- **功能：** 设置移动类型
- **参数：**  `move_type`: 0 - movj    1 - movI
- **返回值：** 无

**13.8** `get_movement_type()`

- **功能：** 获取移动类型
- **返回值：**  0 - movj    1 - movI

**13.9** `set_end_type(end)`

- **功能：** 设置末端坐标系
- **参数：**  `end`: 0 - 法兰(默认)    1 - 工具
- **返回值：** 无

**13.10** `get_end_type()`

- **功能：** 获取末端坐标系
- **返回值：**  0 - 法兰(默认)    1 - 工具


### 14 速度规划

**14.1** `get_plan_speed()`

- **功能：** 获取规划速度
- **返回值：**  移动速度(`list`)

**14.2** `get_plan_acceleration()`

- **功能：** 获取规划加速度
- **返回值：** 加速度(`list`)


## myBuddy
### 1 机械臂整体运行状态

**1.1** ` power_off(id=0)`

- **功能：** 机械臂关闭电源

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

**1.2** ` power_on(id=0)`

- **功能：** 机械臂打开电源

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

**1.3** ` read_next_error(id=0)`

- **功能：** 机器人错误检测

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

**1.4** ` release_all_servos(id=0)`

- **功能：** 放松舵机

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)
**1.5** ` is_power_on(id=0)`

- **功能：** 控制核心连接状态查询

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

- **返回**

    1 - 开机
    0 - 关机
    -1 - 错误数据

**1.6** ` is_controller_connected(id=0)`

- **功能：** 是否与 Atom 连接。

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

- **返回**

    0 - 断开
    1 - 连通


**1.7** ` set_free_mode(id, value)`

- **功能：** 设置自由模式

- **参数**

  - **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

  - **value** - 0 - 关闭 1 - 打开

**1.8** ` set_fresh_mode(id, mode)`

- **功能：** 设置命令刷新模式

- **参数**

  - **id** – 1/2(左/右)。

  - **mode** - int
    1 - 总是先执行最新的命令。
    0 - 以队列的形式顺序执行指令。

**1.9** `release_servo(id，servo_id)`
- **功能：** 放松指定的单个舵机

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **servo_id** - 1 - 6。


**1.10** ` is_free_mode(id)`

- **功能：** 检查是否为自由模式

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

- **返回**

    0 - 否
    1 - 是


### 2 机械臂运行状态和设置


**2.1** ` stop(id)`

- **功能：** 停止移动

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)。



**2.2** ` resume(id)`

- **功能：** 恢复运动

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)。


**2.3** ` is_paused(id)`

- **功能：** 判断机械手是否暂停。

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)。

- **返回**

    1 - 暂停
    0 - 未暂停
    -1 - 错误

**2.4** ` get_speed(id)`

- **功能：** 获得速度

- **参数：**

    **id** – 1/2/3(左臂/右臂/腰部)。

- **返回**

    速度

- **返回类型**

    整数


**2.5** ` set_speed(id，speed)`

- **功能：** 设定速度值

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **speed** (_int_) - 0 - 100

**2.6** ` get_joint_min_angle(id，joint_id)`

- **功能：** 获取指定关节的最小移动角度

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **joint_id** - (int) 1 - 6

- **返回**

    角度值(浮点数)


**2.7** ` is_servo_enable(id，servo_id)`

- **功能：** 判断所有舵机是否连接

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **servo_id** - (int) 1 ~ 6

- **返回**

    0 - 不连通
    1 - 已连通
    -1 - 错误


**2.8** ` is_all_servo_enable(id)`

- **功能：** 判断是否连接了指定舵机

- **参数：**

    **id** – 1/2/3 (左臂/右臂/腰部)

- **返回**

    0 - 禁用
    1 - 启用
    -1 - 错误



**2.9** ` set_joint_min(id，joint_id，angle)`

- **功能：** 设置关节最小角度

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **joint_id** - 整数 1-6。

  - **角度** - 0 ~ 180




**2.10** ` get_robot_version(id)`

- **功能：** 获取机器人版本

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)


**2.11** ` get_system_version(id)`

- **功能：** 获取软件版本

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

**2.12** ` get_joint_max_angle(id，joint_id`

- **功能:** 获取指定关节的最大运动角度

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **joint_id** - (int) 1 - 6

- **返回**

    角度值(浮点数)


**2.13** ` set_robot_id(id, new_id)`

- **功能：** 设置此机器人 ID

- **参数**

  - **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

  - **new_id** - 1 - 253


**2.14** ` joint_brake(id, joint_id)`

- **功能：** 关节运动时使其停止，缓冲距离与现有速度正相关

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **joint_id** - 1 - 6


**2.15** ` get_robot_id(id)

- **功能：** 检测此机器人 ID

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)



### 输入程序控制模式(MDI模式)


**3.1** ` get_angles(id)`

- **功能：** 获取所有关节的度数。

- **参数**

    **id** – 1/2(左/右)

- **返回**

    长度为6的列表。

- **返回类型**

    列表

**3.2** ` send_angle(id, joint, angle, speed)`

- **功能：** 向机械臂发送单关节角度。

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **joint** – 1 ~ 6

  - **angle** - 角度值

  - **speed** – 1 ~ 100

- **返回**
  - 无

**3.3** ` send_angles(id，degrees，speed)`

- **功能：** 将所有角度发送到指定的机械臂

- **参数**

  - **id** – 1/2(左/右)。

  - **degrees** - [angle_list] len 6

  - **speed** - 1 - 100


**3.4** ` set_joint_max(id，joint_id，angle)`

- **功能：** 设置关节最大角度

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **joint_id** - 整数 1-6。

  - **角度** - 0 ~ 180




**3.5** ` send_coord(id, coord, data, speed)`

- **功能：** 向机械臂发送单个坐标

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **coord** – 1 ~ 6 (x/y/z/rx/ry/rz)

  - **data** - 坐标值

  - **speed** - 0 ~ 100

**3.6** ` send_coords(id, coords, speed, mode)`

- **功能：** 将所有坐标发送到机械臂。

- **参数**

  - **id** – 1/2(左/右)。

  - **coords** – 坐标值列表(List[float])，长度 6，[x(mm), y, z, rx(angle), ry, rz]

  - **speed** - (int) 1 ~ 100

  - **mode** - (int) 0 - moveJ, 1 - moveL, 2 - moveC


**3.7** ` get_coord(id，joint_id)`

- **功能：** 读取单个坐标参数

- **参数**

  - **id** (_int_) – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** (_int_) – 1 - 7(7 是夹爪)



**3.8** ` get_encoder(id,joint_id)`

- **功能：** 获取指定的关节电位值。

- **参数**

  - **id** - 1/2/3(左臂/右臂/腰部)。

  - **joint_id** - (int) 1 ~ 6

- **返回**

    0 ~ 4096

**3.9** ` get_encoders(id)`

- **功能：** 获取指定机械臂的六个关节电位值

- **参数**

    **id** – 1/2(左/右)。

- **返回**

    列表


**3.10** ` get_radians(id)`

- **功能：** 获取所有关节的弧度

- **参数**

    **id** – 1/2(左/右)

- **返回**

    浮动弧度列表 [radian1, ...]

- **返回类型**

    列表

**3.11** ` send_radians(id, radians, speed)`

- **功能：** 将所有关节的弧度发送到机械臂

- **参数**

  - **id** – 1/2(左/右)。

  - **radians** – 弧度值列表(List[float])，长度为 6

  - **speed** - (int)0 ~ 100


**3.12** ` is_in_position(id, data, mode)`

- **功能：** 判断是否到达位置。

- **参数**

  - **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)。

  - **data** – 数据列表、角度或坐标。如果 id 是 1/2。数据长度为 6. 如果 id 为 0. data len 13(data==[ [left_angles / left_coords],[right_angles / right_coords],[waist_angle /waist_coord]]). 如果 id 为 3. data len 1

  - **mode** - 1 - 坐标，0 - 角度

- **返回**

    1 - 已到达
    0 - 未到达
    -1 - 错误

**3.13** ` is_moving(id)`

- **功能：** 检测机器人是否在移动

- **参数**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)。

- **返回**

    0 - 不动
    1 - 正在移动
    -1 - 错误数据


**3.14** ` set_color(id, r=0, g=0, b=0)`

- **功能：** 设置机器人手臂顶部Atom的灯光颜色。

- **参数**

  - **id** - 1/2(左/右)

  - **r** (_int_) – 0 ~ 255

  - **g** (_int_) – 0 ~ 255

  - **b** (_int_) – 0 ~ 255


**3.15** ` set_encoder(id，joint_id，encoder，speed)`

- **功能：** 发送单关节的encoder值

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** - 1 - 6。

  - **encoder** – 设置编码器的值。

**3.16** ` set_encoders(id，encoder，speed)`

- **功能：** 设置指定机械臂的六个关节同步执行到指定encoder位置。

- **参数**

  - **id** – 1/2(左/右)。

  - **encoders** - 编码器列表，长度为 6。

  - **speed** – 速度 1 ~ 100


**3.17** ` get_angle(id，joint_id)`

- **功能：** 获取单个关节的角度

- **参数**

  - **id** (_int_) – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** (_int_) – 1 - 7(7 是夹爪)

**3.18** ` set_servo_calibration(id，servo_no)`

- **功能：** 设置关节当前位置为角度零点，

    对应的encoder为2048。

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **servo_no** – 舵机的序列号，1 - 6。

**3.19** ` set_joint_current(id，joint_id，current)`

- **功能：** 设置碰撞电流

- **参数:**

  - **id** - 0/1/2 (ALL/L/R)

  - **joint_id** - 1 - 6

  - **current** – 电流值


**3.19** ` set_encoders_drag(id, encoders, speeds)`

- **功能：** 设置末端坐标系

- **参数:**

  - **id** - 0/1/2 (ALL/L/R)

  - **encoders** - `list` 每个关节的电位值

  - **speed** - 通过`get_servo_speeds()`获得


**3.20** ` get_coords(id)`

- **功能：** 获取机械臂坐标

- **参数**

    **id** – 1/2(左/右)。

### 4 JOG模式和操作

**4.1** ` jog_absolute(id，joint_id，angle，speed)`

- **功能：** 绝对关节控制

- **参数:**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** - 整数 1-6。

  - **angle** - int

  - **speed** - int (0 - 100)

**4.2** ` jog_angle(id，joint_id，direction，speed)`

- **功能：** 关节控制。

- **参数:**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** - 整数 1-6。

  - **direction** - 0 - 减少，1 - 增加

  - **speed** - int (0 - 100)

**4.3** ` jog_coord(id, coord_id, direction, speed)`

- **功能：** 坐标控制。

- **参数:**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **coord_id** – int 1-6 (x/y/z/rx/ry/rz)。

  - **direction** - 0 - 减少，1 - 增加

  - **speed** - int (0 - 100)

**4.4** ` jog_inc_coord(axis，increment，speed)`

- **功能：** 双臂协同坐标步进

- **参数:**

  - **axis** – 1 - 6 (x/y/z/rx/ry/rz)

  - **increment** -

  - **speed** - 1 - 100

**4.5** ` jog_increment(id，joint_id，increment，speed)`

- **功能：** 步进模式

- **参数:**

  - **id** – 1/2/3 (左臂/右臂/腰部)。

  - **joint_id** - 整数 1-6。

  - **increment** -

  - **speed** - int (1 - 100)

**4.6** ` jog_stop(id)`

- **功能：** JOG停止

- **参数:**

    **id** – 1/2/3(左臂/右臂/腰部)。


### 5 舵机控制与操作

**5.1** ` focus_servo(id，servo_id)`

- **功能：** 上电指定舵机

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **servo_id** - 1 - 6


**5.2** ` get_servo_currents(id)`

- **功能：** 获取关节电流

- **参数：**

    **id** – 1/2/3 (左臂/右臂/腰部)

- **返回**

    毫安单位的值

<!-- **5.3** ` get_serv**5.1o_data(id，servo_no，data_id)`

- **功能：** 读取舵机指定地址的数据参数。

- **参数：**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **servo_no** – 舵机的序列号，1 - 6。

  - **data_id** – 数据地址。

- **返回**

    值 (0 - 4096)
    0 - 禁用
    1 - 启用
    -1 - 错误 -->

**5.3** ` get_servo_status(id)`

- **功能：** 获取关节状态

- **参数：**

    **id** – 1/2/3 (左臂/右臂/腰部)

- **返回**

    【电压、传感器、温度、电流、角度、过载】，值为0表示无错误

**5.4** ` get_servo_temps(id)`

- **功能：** 获取关节温度

- **参数：**

    **id** – 1/2/3 (左臂/右臂/腰部)

**5.5** ` get_servo_voltages(id)`

- **功能：** 获取关节电压

- **参数：**

    **id** – 1/2/3 (左臂/右臂/腰部)

- **返回**

    电压值 < 24 V


<!-- **5.7** ` set_servo_data(id，servo_no，data_id，value)`

- **功能：** 设置舵机指定地址的数据参数

- **参数**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **servo_no** – 舵机的序列号，1 - 6。

  - **data_id** – 数据地址。

  - **value** - 0 - 4096 -->



### 6 Atom 末端IO控制


**6.1** ` set_pin_mode(id, pin_no, pin_mode)`

- **功能：** 在 atom 中设置指定引脚的状态模式。

- **参数：**

  - **id** - 1/2(左/右)

  - **pin_no** (_int_) – 引脚编号 (1 - 5)。

  - **pin_mode** (_int_) - 0 - 输入，1 - 输出


**6.2** ` set_digital_output(id, pin_no, pin_signal)`

- **功能：** 设置 atom IO 输出电平

- **参数：**

  - **id** - 1/2(左/右)

  - **pin_no** (_int_) - 1 - 5

  - **pin_signal** (_int_) – 0 / 1


**6.3** ` get_digital_input(id, pin_no)`

- **功能：** 读取Atom IO输入电平

- **参数：**

  - **id** - 1/2(左/右)

  - **pin_no** (_int_) - 1 - 5


**6.4** ` set_pwm_output(id, channel, frequency, **6.1pin_val)`

- **功能：** 脉宽调制控制

- **参数：**

  - **id** - 1/2(左/右)

  - **channel** (_int_) – IO 编号 (1 - 5)。

  - **frequency** (_int_) – 时钟频率 (0/1: 0 - 1Mh**6.1z 1 - 10Mhz`)

  - **pin_val** (_int_) – 占空比 0 ~ 100: 0 ~ 100%

### 7 夹爪控制


**7.1** ` get_gripper_value(id)`

- **功能：** 获取夹爪的值。

- **参数**

    **id** – 1/2(左/右)

- **返回**

    夹持器值 (int)


**7.2** ` is_gripper_moving(id)`

- **功能：** 判断夹爪是否在移动

- **参数**

    **id** – 1/2(左/右)

- **返回**

    0 - 不动
    1 - 正在移动
    -1 - 错误数据


**7.3** ` set_gripper_state(id, flag)`

- **功能：** 设置夹爪开关状态

- **参数**

  - **id** - 1/2(左/右)

  - **flag** (_int_) - 0 - 关闭，1 - 打开

**7.4** ` set_gripper_value(id, value, speed)`

- **功能：** 设置夹爪的值

* **参数**

  * **id** – 1/2 (L/R)

  * **value** (_int_) – 0 ~ 100

  * **speed** (_int_) – 0 ~ 100


### 8 socket通信

```python
from pymycobot import MyBuddySocket

mst = MyBuddySocket("192.168.0.1", 9000)
mst.connect("/dev/ttyACM0", "115200")

print(mst.get_angles(1))
```

### 9 树莓派——GPIO

**9.1** ` Get_gpio_input(pin)`

- **功能：** 获取 GPIO 输入值。

- **参数**

    **pin** - (int)pin 号。

**9.2** ` set_gpio_input(pin)`

- **功能：** 设置 GPIO 输入值。

- **参数**

    **pin** - (int)pin 号。 

**9.3** ` set_gpio_mode(pin_no, mode)`

- **功能：** 初始化 GPIO 模块，设置 BCM 模式。

- **参数**

  - **pin_no** - (int) 引脚号。

  - **mode** - 0 - 输入 1 - 输出

**9.4** ` set_gpio_output(pin, v)`

- **功能：** 设置 GPIO 输出值。

- **参数**

   - **pin** - (int)pin 号。

   - **v** - (int) 0 / 1

**9.5** ` set_gpio_pwm(pin, baud, dc)`

- **功能：** 设置 GPIO PWM 值。

- **参数**

   - **pin** - (int)pin 号。

   - **baud** - (int) 10 - 1000000

   - **dc** - (int) 0 - 100


### 10 坐标变换


**10.1** ` set_tool_reference(id，coords)`

- **功能：** 设置工具坐标系

- **参数**

  - **id** - 0/1/2 (ALL/L/R)

  - **coords** – 坐标值列表(List[float])，长度为 6。[x(mm), y, z, rx(angle), ry, rz]

**10.2** ` set_world_reference(id，coords)`

- **功能：** 设置世界坐标系

- **参数**

  - **id** - 0/1/2 (ALL/L/R)

  - **coords** – 坐标值列表(List[float])，长度 6 [x(mm), y, z, rx(angle), ry, rz]


**10.3** ` get_reference_frame(id)`

- **功能：** 获取base坐标系

- **参数**

    **id** – 0/1/2 (ALL/L/R)

- **返回**

    0 - 基础 1 - 工具。


**10.4** ` get_tool_reference(id)`

- **功能：** 获取工具坐标系

- **参数**

    **id** – 0/1/2 (ALL/L/R)

**10.5** ` get_world_reference(id)`

- **功能：** 获取世界坐标系

- **参数**

    **id** – 0/1/2 (ALL/L/R)


**10.6** ` set_reference_frame(id, rftype)`

- **功能：** 设置基坐标系

- **参数**

  - **id** - 0/1/2 (ALL/L/R)

  - **rftype** - 0 - base 1 - tool。



**10.7** ` set_movement_type(id, move_type)`

- **功能：** 设置移动类型

- **参数**

  - **id** - 0/1/2 (ALL/L/R)

  - **move_type** - 1 - movel，0 - moveJ


**10.8** ` get_movement_type(id)`

- **功能：** 获取运动类型

- **参数**

    **id** – 0/1/2 (ALL/L/R)

- **返回**

    1 - 移动L
    0 - 移动J



**10.9** ` set_end_type(id, end)`

- **功能：** 设置末端坐标系

- **参数**

  - **id** - 0/1/2 (ALL/L/R)

  - **end** - 0 - 法兰，1 - 工具



**10.10** ` get_end_type(id)`

- **功能：** 获取末端坐标系

- **参数**

    **id** – 0/1/2 (ALL/L/R)

- **返回**

    0 - 法兰
    1 - 工具


**10.11** ` write_base_coords(id, coords, speed)`

- **功能：** Base坐标移动

- **参数**

  - **id** - 1/2(左/右)

  - **coords** - coords：坐标值列表(List[float])，长度 6，[x(mm), y, z, rx(angle), ry, rz]

  - **speed** - 1 - 100



**10.12** ` write_base_coord(id，axis, coord, speed)`

- **功能：**Base单坐标移动

- **参数**

  - **id** - 1/2(左/右)

  - **axis** – 1 - 6 (x/y/z/rx/ry/rz)

  - **coord** - 坐标值

  - **speed** - 1 - 100 


**10.13** ` base_to_single_coords(base_coords, arm)`

- **功能：** 将base坐标转换为坐标

- **参数：**

  - **coords** – 基坐标值 len 6 的列表

  - **arm** - 0 - 左。 1 - 对

- **返回:**

    坐标



**10.14** ` get_base_coord(id)`

- **功能：** 获取单臂的基坐标

- **参数：**

    **id** – 1/2(左/右)

**10.15** ` (\*args)get_base_coords`

- **功能：** 将坐标转换为base坐标。可以传入参数或不传参数，传入参数时，是以参数为准进行转化；无参数则以当前所在坐标进行转化。

- **参数：**

  - **coords** – 坐标值列表(List[float])，长度 6 [x(mm), y, z, rx(angle), ry, rz]

  - **arm** - 0 - 左。 1 - 

- **返回:**

    基坐标


### 11 速度规划

**11.1** ` get_plan_acceleration(id=0)`

- **功能：** 获得规划加速度

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

- **返回**

    加速度

**11.2** ` get_plan_speed(id=0)`

- **功能：** 获得规划速度

- **参数：**

    **id** – 0/1/2/3 (ALL/左臂/右臂/腰部)

- **返回**

    规划速度。


**11.3** ` set_acceleration(id, acc)`

- **功能：**设置所有移动过程中加速度

- **参数:**

  - **id** – 1/2/3 (左臂/右臂/腰部)

  - **acc** - 1 - 100


**11.4** ` get_acceleration(id)`

- **功能：**读取所有移动过程中加速度

- **参数：**

    **id** – 1/2/3 (左臂/右臂/腰部)



### 12 碰撞检测

**12.1** ` get_joint_current(id，joint_id)`

- **功能:** 获取碰撞电流

- **参数:**

  - **id** - 0/1/2 (ALL/L/R)

  - **joint_id** - 1 - 6


**12.2** ` collision_switch(state)`

- **功能:** 碰撞检测开关

- **参数:**

    **state** (_int_) - 0 - 关闭 1 - 打开(默认关闭)

**12.3** ` collision(left_angles，right_angles)`

- **功能:** 碰撞检测主程序

- **参数:**

  - **left_angles** - 左臂角度，长度为6的列表。

  - **right_angles** – 右臂角度，长度为6的列表。

- **返回**

    整数

**12.4** ` is_collision_on()`

- **参数：** 获取碰撞检测状态
- **返回：**

    0 - 禁用
    1 - 启用**