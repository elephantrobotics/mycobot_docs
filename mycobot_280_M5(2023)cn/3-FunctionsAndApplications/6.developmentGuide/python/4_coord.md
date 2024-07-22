# 坐标控制

主要用于实现智能规划路线让机械臂从一个位置到另一个指定位置。分为`[x,y,z,rx,ry,rz]`，其中`[x,y,z]`表示的是机械臂头部在空间中的位置（该坐标系为[直角坐标系](https://zhidao.baidu.com/question/2125035227927850747.html)），`[rx,ry,rz]`表示的是机械臂头部在该点的姿态（该坐标系为欧拉坐标）。算法的实现以及欧拉坐标的表示需要一定的学术知识，这里不对其过多的讲解，我们只要懂得直角坐标系就可以很好的使用这个函数了。

> **注意：** 在设置坐标时，不同系列的机械臂关节构造有所不同，同一组坐标，不同系列的机械臂会展示不同的姿态。
>
> <img src="../../../resources\3-FunctionsAndApplications\6.developmentGuide\python\axis/坐标.jpg" style="zoom: 67%;" />

## myCobot

###  单参数坐标

**send_coord(id,coord,speed)**

- **功能：** 发送单个坐标值给机械臂进行移动
- **参数说明：**
  - `id`：代表机械臂的坐标，六轴有六个坐标，四轴有四个坐标，有特定的表示方法
    X坐标的表示法：`Coord.X.value`，也有简易的表示方法：如X轴可以填写1，Y填写2，以此类推
  - `coord`：输入您想要到达的坐标值
  - `speed`：表示机械臂运动的速度，范围是0-100
- **返回值：** 无



###  多参数坐标

**get_coords()**

- **功能：** 获取当前坐标和姿态
- **返回值：** `list`包含坐标和姿态的列表
  - 六轴：长度为 6，依次为 `[x, y, z, rx, ry, rz]`
  - 四轴：长度为 6，依次为 `[x, y, z, rx]`

**send_coords(coords, speed, mode)**

- **功能：** 发送整体坐标和姿态,让机械臂头部从原来点移动到您指定点。
- **参数说明：**
  - `coords`: 
    - 六轴：[x,y,z,rx,ry,rz]的坐标值，长度为6
    - 四轴：[x,y,z,rx]的坐标值，长度为4
  - `speed`: 表示机械臂运动的速度，范围是0-100
  - `mode`: ( `int`): 取值限定 0 和 1。
    - 0 表示机械臂头部移动的路径为非线性，即随机规划路线，只要机械臂头部以保持规定的姿态移动到指定点即可。
    - 1 表示机械臂头部移动的路径为线性的，即智能规划路线让机械臂头部以直线的方式移动到指定点。
- **返回值：** 无

**set_tool_reference(coords)**

- **功能：** 设置工具坐标系。
- **参数说明：**
  - `coords`: 
    - 六轴：[x,y,z,rx,ry,rz]的坐标值，长度为6, x,y,z的范围为-280 ~ 280，rx,ry,yz的范围为-314 ~ 314
- **返回值：** 无

**get_tool_reference()**

- **功能：** 获取工具坐标系。
- **返回值：** 返回一个长度为6的坐标列表

**get_world_reference()**

- **功能：** 获取世界坐标系。
- **返回值：** 返回一个长度为6的坐标列表

**set_world_reference(coords)**

- **功能：** 设置世界坐标系。
- **参数说明：**
  - `coords`: 
    - 六轴：[x,y,z,rx,ry,rz]的坐标值，长度为6, x,y,z的范围为-280 ~ 280，rx,ry,yz的范围为-314 ~ 314
- **返回值：** 无

**set_reference_frame(rftype)**

- **功能：** 设置基坐标系。
- **参数说明：**
  - `rftype`: 0 - 基坐标系(默认)，1 - 世界坐标系
- **返回值：** 无

**get_reference_frame()**

- **功能：** 获取基坐标系。
- **返回值：** 0 - 基坐标系，1 - 世界坐标系，-1 - 通信失败

**set_end_type(end)**

- **功能：** 设置末端坐标系。
- **参数说明：**
  - `end`: 0 - 法兰(默认)，1 - 工具
- **返回值：** 无

**get_end_type()**

- **功能：** 获取末端坐标系。
- **返回值：** 0 - 法兰(默认)，1 - 工具，-1 - 通信失败

### 案例使用

```python
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Coord
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化
import time

# MyCobot 类初始化需要两个参数：
#   第一个是串口字符串， 如：
#       linux： "/dev/ttyUSB0"
#       windows: "COM3"
#   第二个是波特率：
#       M5版本为： 115200
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
# 下面为 windows版本创建对象代码
mc = MyCobot("COM3", 115200)

# 获取当前头部的坐标以及姿态
coords = mc.get_coords()
print(coords)

# # 智能规划路线，让头部以线性的方式到达[57.0, -107.4, 316.3]这个坐标，以及保持[-93.81, -12.71, -163.49]这个姿态，速度为80mm/s
mc.send_coords([57.0, -107.4, 316.3, -93.81, -12.71, -163.49], 80, 1)

# 设置等待时间1.5秒
time.sleep(1.5)

# 智能规划路线，让头部以线性的方式到达[-13.7, -107.5, 223.9]这个坐标，以及保持[165.52, -75.41, -73.52]这个姿态，速度为80mm/s
mc.send_coords([-13.7, -107.5, 223.9, 165.52, -75.41, -73.52], 80, 1)

# 设置等待时间1.5秒
time.sleep(1.5)

# 仅改变头部的x坐标，设置头部的x坐标为-40。让其智能规划路线让头部移动到改变后的位置，，速度为70mm/s
mc.send_coord(Coord.X.value, -40, 70)
```
