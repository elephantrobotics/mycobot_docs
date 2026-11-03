# 机械臂电气接口

## 1 介绍

### 1.1 底座

* A. 底座正面接口如图 2.1.8.2-1 所示:

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-1.png" style="zoom:100%;" />
  
  图 2.1.8.2-1 F底座正面接口
  - ① 功能接口组一  
  - ② 功能接口组二
  - ③ 功能接口组三
  - ④ 功能接口组四 

* B. 底座上面接口如图 2.1.8.2-2 所示:

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-2.png" style="zoom:100%;" />

  图 2.1.8.2-2 底座上面接口
  - ① 功能接口组五
​													
* C. 底座右侧接口如图 2.1.8.2-3 所示:

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-3.png" style="zoom:100%;" />

  图 2.1.8.2-3 底座右侧接口
  - ① 电源DC接口

### 1.2 底座接口说明

> **注意:** 功能接口组均为2.54mm杜邦接口，外部可使用2.54mm杜邦线。

A. 图 2.1.8.2-4, 图 2.1.8.2-5, 图 2.1.8.2-6 和图 2.1.8.2-7 分别为底座正面的四个拓展接口组的信号名，该部分接口用于连接不同的Arduino开发板
功能接口组一与功能接口组四 可用于扩展针脚为Arduino UNO 接口相同开发板，如：Arduino UNO, Arduino MEGA 2560等；

功能接口组二与功能接口组三 可用于扩展针脚为 Arduino MKR WiFi 1010 接口一致开发板；

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-4.png" style="zoom:100%;" /> 

  图 2.1.8.2-4 功能接口组一

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-5.png" style="zoom:100%;" /> 

  图 2.1.8.2-5 功能接口组二

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-6.png" style="zoom:100%;" />

  图 2.1.8.2-6 功能接口组三

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-7.png" style="zoom:100%;" />

  图 2.1.8.2-7 功能接口组四

B. 图 2.1.8.2-8 为底座上面功能接口组无的信号名，该部分接口与所连接的Arduino开发板的各个功能接口一一对应。

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-8.png" style="zoom:100%;" />

  图 2.1.8.2-8 功能接口组五

C. 电源DC接口：使用DC电源插座，外径6.5mm，内径2.0mm；可使用厂家配备的12V 5A  DC电源适配器给myCobot 280进行供电。

## 2 机械臂末端电气接口

### 2.1 机械臂末端介绍

* A. 机械臂末端如图 2.1.8.2-9 和图 2.1.8.2-10 所示:

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-9.png" style="zoom:100%;" />

  图 2.1.8.2-9 机械臂末端
  - ① 舵机接口
  - ② Atom

  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-10.png" style="zoom:100%;" />	

  图 2.1.8.2-10 机械臂末端
  - ① 功能接口组六
  - ② Grove 
  - ③ Type C

### 2.2 末端接口说明

* A. 功能接口组六各个接口的定义如表 2.1.8.2-1 所示:
  
<center>表 2.1.8.2-1</center>

| 标签 | 信号名 | 类型 | 功能 | 备注 |
| :---: | :----: | :--: | :------: | :----: |
| 5V | 5V | P | DC 5V |  |
| GND | GND | P | GND |  |
| 3V3 | 3V3 | P | DC 3.3V |  |
| G22 | G22 | I/O | GPIO22 |  |
| G19 | G19 | I/O | GPIO19 |  |
| G23 | G23 | I/O | GPIO23 |  |
| G33 | G33 | I/O | GPIO33 |  |

> **注意:** 
> 1. I: 仅作为输入。
> 
> 2. I/O: 该功能信号包含输入和输出组合。
> 
> 3. 当管角设置为输出端时，它将输出电压3.3V。
> 
> 4. 单个管角的拉电流随管脚数量增加而减小，从约40mA减小到29mA。
> 
> 5. 如果某个GPIO被设置为输出模式时，输出高电平信号，电路连接如图 2.1.8.2-11 所示，LED灯将点亮。
> 
> <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-11.png" style="zoom:100%;" />
> 
> 图 2.1.8.2-11

* B. Type C接口：可用于和PC端连接通讯，更新固件使用。

* C. Grove : 定义如图 2.1.8.2-12 所示
  
  <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.3-FirmwareFunctionDescription/2.1.8.2-12.png" style="zoom:100%;" />

  图 2.1.8.2-12 Grove

* D. 舵机接口：用于末端拓展夹爪时使用，当前支持配套的自适应夹爪使用。

* E. Atom：用于 5X5 RGB LED（G27）显示和按键功能（G39）

 