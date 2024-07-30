# 第二章 机器人参数说明

> 第一章中，我们探讨了产品的卖点及其设计理念，为您提供了对产品高层次理解的全景视角。现在，让我们进入第二章——机器人参数说明。这一章节将是您理解产品技术细节的关键。详细了解这些技术参数，不仅可以帮助您充分认识到我们产品的先进性和实用性，而且还能够确保您能够更有效地利用这些技术来满足您的具体需求。

<img src="../../resource\1-ProductInformation\2.ProductParameter/280arduino.png" style="zoom:100%;" />


## 1机器人规格参数

### 1.1机械臂参数

|   指标   |           参数           |
| :------: | :----------------------: |
|   名称   |      小象协作机械臂      |
|   型号   | myCobot 280 Arduino 2023 |
|  自由度  |            6             |
| 有效负载 |           250g           |
| 工作半径 |          280mm           |
|   重量   |           860g           |
| 电源输入 |          12V,5A          |
| 工作温度 |          -5-45℃          |
|   通信   |   USB (根据开发板而定)   |

## 2.控制核心参数

|    指标    |                参数                |
| :--------: | :--------------------------------: |
|    SOC     |                 无                 |
|    CPU     |                 无                 |
| 蓝牙/无线  |                 无                 |
|    USB     |                 无                 |
|  显示屏幕  |                 无                 |
| HDMI 接口  |                 无                 |
| 自定义按键 |                 无                 |
|  IO 接口   | 面板 IO 均为转接功能，视扩展板决定 |

## 3.结构尺寸参数
### 3.1工作空间

<img src="../../resource\1-ProductInformation\2.ProductParameter/worksize.png" style="zoom:100%;" />

### 3.2规格尺寸

<img src="../../resource\1-ProductInformation\2.ProductParameter/arduinosize.jpg" style="zoom:50%;" />

### 3.3关节运动范围

| 关节       | 范围 |
| :--------: | :----------:|
| J1        | -168 ~ +168     |
| J2        | -135 ~ +135      |
| J3  | -150 ~ +150                   |
| J4        | -145 ~ +145 |
| J5   | -165 ~ +165                   |
| J6   | -180 ~ +180         |


### 3.4孔位安装

- 机器人底座安装法兰，底座同时兼容乐高科技件安装方式和M4螺丝安装方式。

<img src="../../resource\1-ProductInformation\2.ProductParameter/base1.jpg" style="zoom:100%;" />


- 机器人末端安装法兰，机械臂末端同时兼容乐高科技件孔与螺丝螺纹孔。

<img src="../../resource\1-ProductInformation\2.ProductParameter/base2.png" style="zoom:60%;" />

## 4.电气特性参数
## 机械臂电气接口
## 4.1 介绍
### 底座

* A. 底座正面接口如图 2.1.8.2-1 所示:

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-1.png" style="zoom:100%;" />
  
  图 2.1.8.2-1 F底座正面接口
  - ① 功能接口组一  
  - ② 功能接口组二
  - ③ 功能接口组三
  - ④ 功能接口组四 

* B. 底座上面接口如图 2.1.8.2-2 所示:

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-2.png" style="zoom:100%;" />

  图 2.1.8.2-2 底座上面接口
  - ① 功能接口组五
​													
* C. 底座右侧接口如图 2.1.8.2-3 所示:

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-3.png" style="zoom:100%;" />

  图 2.1.8.2-3 底座右侧接口
  - ① 电源DC接口

###  底座接口说明

> **注意:** 功能接口组均为2.54mm杜邦接口，外部可使用2.54mm杜邦线。

A. 图 2.1.8.2-4, 图 2.1.8.2-5, 图 2.1.8.2-6 和图 2.1.8.2-7 分别为底座正面的四个拓展接口组的信号名，该部分接口用于连接不同的Arduino开发板
功能接口组一与功能接口组四 可用于扩展针脚为Arduino UNO 接口相同开发板，如：Arduino UNO, Arduino MEGA 2560等；

功能接口组二与功能接口组三 可用于扩展针脚为 Arduino MKR WiFi 1010 接口一致开发板；

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-4.png" style="zoom:100%;" /> 

  图 2.1.8.2-4 功能接口组一

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-5.png" style="zoom:100%;" /> 

  图 2.1.8.2-5 功能接口组二

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-6.png" style="zoom:100%;" />

  图 2.1.8.2-6 功能接口组三

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-7.png" style="zoom:100%;" />

  图 2.1.8.2-7 功能接口组四

B. 图 2.1.8.2-8 为底座上面功能接口组无的信号名，该部分接口与所连接的Arduino开发板的各个功能接口一一对应。

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-8.png" style="zoom:100%;" />

  图 2.1.8.2-8 功能接口组五

C. 电源DC接口：使用DC电源插座，外径6.5mm，内径2.0mm；可使用厂家配备的12V 5A  DC电源适配器给myCobot 280进行供电。

## 4.2 机械臂末端电气接口
###  机械臂末端介绍

* A. 机械臂末端如图 2.1.8.2-9 和图 2.1.8.2-10 所示:

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-9.png" style="zoom:100%;" />

  图 2.1.8.2-9 机械臂末端
  - ① 舵机接口
  - ② Atom

  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-10.png" style="zoom:100%;" />	

  图 2.1.8.2-10 机械臂末端
  - ① 功能接口组六
  - ② Grove 
  - ③ Type C

###  末端接口说明

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
> <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-11.png" style="zoom:100%;" />
> 
> 图 2.1.8.2-11

* B. Type C接口：可用于和PC端连接通讯，更新固件使用。

* C. Grove : 定义如图 2.1.8.2-12 所示
  
  <img src="../../resource\1-ProductInformation\2.ProductParameter/2.1.8.2-12.png" style="zoom:100%;" />

  图 2.1.8.2-12 Grove

* D. 舵机接口：用于末端拓展夹爪时使用，当前支持配套的自适应夹爪使用。

* E. Atom：用于 5X5 RGB LED（G27）显示和按键功能（G39）

 

## 5.DH参数

<img src="../../resource/1-ProductInformation/2.ProductParameter/280DH.jpg" style="zoom:15%;" />

SDH参数表：

<img src="../../resource/1-ProductInformation/2.ProductParameter/SDH.png" style="zoom:80%;" />


---

[← 上一章](../1.ProductIntroduction/1-ProductIntroduction.md) | [下一章 →](../../2-BasicSettings/3.UserNotice/3-UserInstructions.md)
