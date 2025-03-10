# 第五章 基础功能

**本章主要解释产品的基本功能用法和基本软件的使用。本章至关重要，应仔按照顺序细阅读。在实际应用机器人之前，请确保正确理解所述操作。**

#### 关于M5版本和PI版本机器的区别

M5版本机器是大象机器人和深圳市明栈科技有限公司 - M5STACK 联合出品，采用Esp32核心处理器，带有两块显示屏幕和多个实体按键。PI版本机器是大象机器人和树莓派官方联名产品，机械臂采用树莓派 RaspBerry PI 4B核心处理器，为应对客户Linux系统应用的需求，以及一体式集成机器人开发便捷的设备的需求而设计。

**PI 型号机器人就是电脑主机**

PI版本机器内嵌树莓派4B，1.5GHz 4核微处理器，运行Debian/Ubuntu平台，支持4路USB，2路HDMI，标准化GPIO接口 TF卡可插拔。

PI版本机器的本质是带有独立系统的开发板，是可以看做一个微型的电脑主机，主机和主机之间无法简单的通过一根线构成通讯。它只能连接到一台独立显示器上，并搭配电源 鼠标 键盘，进入到开发板内置的系统后对其进行开发和操作。

请跟随以下章节，对pi版本的机械臂进行学习。

- [pi版本机械臂入门](5.1-Functionlnstruction/3.5.1-SW-description.md)  
  本部分将介绍如何快速入门PI版本的机械臂以及如何对操作系统进行更新升级。

- [系统基础功能说明](5.2-Softwarelnstructions/3.5.2-SW-detail-description.md)<br>
  本部分会介绍Ubuntu操作系统以及如何进行蓝牙配置、VNC配置、网络配置等操作以及myStudio的使用。

- [固件说明](5.3-FirmwareFunctionDescription/README.md)  
  本部分会介绍PI版本机器人的通用硬件接口，出厂固件以及使用myStudio烧录 Atom 固件。

- [mystudio](5.2-Softwarelnstructions/README.md)
  一站式服务平台myStudio，整合myCobot软件资源及各类资料，支持固件下载与更新。提供产品使用视频教程以及维护/维修方面等信息。

---

[← 上一章](../../2-BasicSettings/4.FirstTimeInstallation/4-FirstTimeInstallation.md) | [下一章 →](../6.developmentGuide/README.md)