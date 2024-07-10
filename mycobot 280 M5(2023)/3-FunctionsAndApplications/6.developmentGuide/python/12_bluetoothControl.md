# 蓝牙控制

> 注意：客户端连接结束后蓝牙服务器会自动关闭，再次使用时需要重新打开（最好不要主动关闭服务器，可能会导致下次无法打开）


## myBuddy
### 开启蓝牙服务器
1.双击打开桌面上的**mybuddy**软件

<img src =../resourse/17-myBuddy/Python/p1.jpg
width ="600"  align = "center">

2.选择“Transponder”, 端口选择“/dev/ttyACM0”, 点击Connect.

<img src =../resourse/17-myBuddy/Python/p2.jpg
width ="600"  align = "center">

3.点击 "BT"

<img src =../resourse/17-myBuddy/Python/p5.jpg
width ="600"  align = "center">

4.点击"OPEN"，开启蓝牙服务器

<img src =../resourse/17-myBuddy/Python/p6.jpg
width ="600"  align = "center">



如果以上步骤顺利完成，蓝牙服务器则开启完成。

### 客户端

> 注意：在使用蓝牙功能之前，客户端必须先安装pybluez2，推荐安装版本0.40, 可以通过指令pip install pybluez2==0.40来安装指定版本。

客户端程序示例：
```python
from pymycobot import MyBuddyBlueTooth

mst = MyBuddyBlueTooth("00:00:00:00:00:00", 1)
mst.connect("/dev/ttyACM0", "115200")

print(mst.get_angles(1))
```