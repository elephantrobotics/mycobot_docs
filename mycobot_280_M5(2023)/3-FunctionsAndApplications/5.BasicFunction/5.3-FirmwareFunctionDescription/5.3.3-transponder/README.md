# 电脑控制

![mycobot_led](../../../resourse/4-BasicApplication/4.2/4.2.3/4.2.3-mycobot_led.png)

电脑控制的时效性对于微控制器机械臂至关重要。对于微控制器机械臂来说，我们通常对底座的 Basic 发送控制指令，通过电脑控制转发，末端执行器将对指令进行解析，继而执行目标动作。

该功能现主要用于客户在不同环境下自行开发机械臂。

**设备类型不同，操作方式也有所不同**，大概步骤如下：

- **Atom**烧录最新版的**atomMain**
- **M5Stack-basic**烧录**minirobot**，选择**Transponder**功能，微处理器类设备无需烧录**M5Stack-basic**
- 按下检测键，检测 Basic 和末端执行器 Atom 是否正常通讯
- 按下退出按钮，退出此功能

本章，我们可以实时检测 Basic 和末端执行器 Atom 是否正常通讯。

