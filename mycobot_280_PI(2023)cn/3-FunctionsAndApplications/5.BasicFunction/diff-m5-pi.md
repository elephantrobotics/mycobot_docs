# 关于M5版本和PI版本机器的区别

## M5

- M5版本机器是大象机器人和深圳市明栈科技有限公司 - M5STACK 联合出品，采用**Esp32**核心处理器，带有**两块显示屏幕和多个实体按键**，是为用户应用于桌面级机械臂开发应用而设计，产品深度糅合M5扩展生态，根据我司提供开发环境教程，即可搭建**UIFlow、python、Arduino**等多种开发环境的一款机械臂

- M5版本机身搭载两块显示屏，多个实体按键，底座以 M5Stack-basic 作为主控，末端以M5STACK Atom 作为副控

- M5版本机器本身只具备 **录制播放** 功能，即录制动作&播放动作，如需进一步使用 **UIFlow、python、Arduino** 等方式进行开发，需连接PC进行开发，连接方式如下：
<div align=center>
<img src="../resourse/4-BasicApplication/4.1/4.1.2.1-basic_PC.jpg" alt="basic" style="zoom:50%;" />
</div>

- 连接完成后，根据以下步骤打开机械臂通讯：

**❗❗❗❗❗❗❗❗❗❗提示⚠：以下步骤极其重要，请一定要进行，不进行则机械臂无法正常通讯❗❗❗❗❗❗❗❗❗❗**

**❗❗❗❗❗❗❗❗❗❗提示⚠：以下步骤极其重要，请一定要进行，不进行则机械臂无法正常通讯❗❗❗❗❗❗❗❗❗❗**

**❗❗❗❗❗❗❗❗❗❗提示⚠：以下步骤极其重要，请一定要进行，不进行则机械臂无法正常通讯❗❗❗❗❗❗❗❗❗❗**

  - M5Stack-basic选择Transponder功能

  <div align=center>
  <img src="../resourse/2-serialproduct/2.0/trans-1.jpg" style="zoom:35%;" />
  </div>

  <div align=center>
  <img src="../resourse/2-serialproduct/2.0/trans-2.jpg" style="zoom:58%;" />
  </div>

  - 检测Atom的连接(ok表示连接正常，否则显示no)

  **❗❗❗❗❗❗❗❗❗❗提示⚠：到达此页面后，需要一直停留在此页面才可保持通讯❗❗❗❗❗❗❗❗❗❗**

  **❗❗❗❗❗❗❗❗❗❗提示⚠：到达此页面后，需要一直停留在此页面才可保持通讯❗❗❗❗❗❗❗❗❗❗**

  **❗❗❗❗❗❗❗❗❗❗提示⚠：到达此页面后，需要一直停留在此页面才可保持通讯❗❗❗❗❗❗❗❗❗❗**

  <div align=center>
  <img src="../resourse/2-serialproduct/2.0/trans-3.jpg" style="zoom:55%;" />
  </div>

- 适用的开发方式有：myBlockly, Python, C++, C#, Arduino, JavaScript, ROS。


## PI

- PI版本机器是大象机器人和**树莓派**官方联名产品，机械臂采用**树莓派 RaspBerry PI 4B** 核心处理器，为应对客户**Linux**系统应用的需求，以及一体式集成机器人开发便捷的设备的需求而设计，产品保留了RaspBerry PI 4B 的原生硬件接口，同时设备内置 **Ubuntu 18.04** 操作系统， **python、ROS、myBlockly** 等多种开发环境，

- PI版本机器内嵌树莓派4B，1.5GHz 4核微处理器，运行Debian/Ubuntu平台，支持4路USB，2路HDMI，标准化GPIO接口、TF卡可插拔

- PI版本机器的本质是带有独立系统的开发板，是可以看做一个微型的电脑主机，主机和主机之间无法简单的通过一根线构成通讯。它只能连接到一台独立显示器上，并搭配电源、鼠标、键盘，进入到开发板内置的系统后对其进行开发和操作

**❗❗❗❗❗❗❗❗❗❗提示⚠：以下图中圈出的Type-C口，HDMI口，USB口全部无法用于与PC以及笔记本电脑通讯❗❗❗❗❗❗❗❗❗❗**

**❗❗❗❗❗❗❗❗❗❗提示⚠：以下图中圈出的Type-C口，HDMI口，USB口全部无法用于与PC以及笔记本电脑通讯❗❗❗❗❗❗❗❗❗❗**

**❗❗❗❗❗❗❗❗❗❗提示⚠：以下图中圈出的Type-C口，HDMI口，USB口全部无法用于与PC以及笔记本电脑通讯❗❗❗❗❗❗❗❗❗❗**

<div align=center>
<img src="../resourse/2-serialproduct/2.0/atom-type-c.jpg" style="zoom:50%;" />
</div>

<div align=center>
<img src="../resourse/2-serialproduct/2.0/pi-type-c-hdmi.jpg" style="zoom:20%;" />
</div>

<div align=center>
<img src="../resourse/2-serialproduct/2.0/pi-usb.jpg" style="zoom:13%;" />
</div>

- PI版本机器无需搭配PC、笔记本等设备，连接显示器即可进行应用开发

**❗❗❗❗❗❗❗❗❗❗提示⚠：请使用配套发货的HDMI线连接显示器，使用内置系统进行开发❗❗❗❗❗❗❗❗❗❗**

**❗❗❗❗❗❗❗❗❗❗提示⚠：请使用配套发货的HDMI线连接显示器，使用内置系统进行开发❗❗❗❗❗❗❗❗❗❗**

**❗❗❗❗❗❗❗❗❗❗提示⚠：请使用配套发货的HDMI线连接显示器，使用内置系统进行开发❗❗❗❗❗❗❗❗❗❗**

  - 先将HDMI线插入显示器的HDMI接口

  <div align=center>
  <img src="../resourse/2-serialproduct/myCobot 280/Pi/2.1.2.3开箱与首次使用/PI连接3.jpg" style="zoom:80%;" />
  </div>

  - 再将另一头插入机械臂的HDMI接口即可

  <div align=center>
  <img src="../resourse/2-serialproduct/myCobot 280/Pi/2.1.2.3开箱与首次使用/PI连接4.jpg" style="zoom:25%;" />
  </div>

  <div align=center>
  <img src="../resourse/2-serialproduct/myCobot 280/Pi/2.1.2.3开箱与首次使用/PI连接2.jpg" style="zoom:25%;" />
  </div>

  <div align=center>
  <img src="../resourse/2-serialproduct/myCobot 280/Pi/2.1.2.3开箱与首次使用/PI连接1.jpg" style="zoom:25%;" />
  </div>

- 适用的开发方式有：myBlockly, Python, ROS。