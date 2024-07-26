# 第五章 基础功能

**本章主要解释产品的基本功能用法和基本软件的使用。本章至关重要，应仔按照顺序细阅读。在实际应用机器人之前，请确保正确理解所述操作。**

ER myCobot 280 Jetson Nano 采用 NVIDIA® Jetson Nano™ 核心开发版作为主控，内置Ubuntu Mate 20.04 操作系统，无需额外搭配PC主控，直接链接显示器、键盘、鼠标即可使用，是可以看做一个微型的电脑主机，主机和主机之间无法简单的通过一根线构成通讯。它只能连接到一台独立显示器上，并搭配电源 鼠标 键盘，进入到开发板内置的系统后对其进行开发和操作。

请跟随以下章节，对myCobot 280 JN版本的机械臂进行基础功能学习。

- [系统使用介绍](5.1-Functionlnstruction/README - 1.md)  
  本部分将介绍对myCobot 280 JN机械臂的开发环境以及系统内置软件进行简要介绍。

- [系统基础功能说明](5.2-Softwarelnstructions/3.5.2-SW-detail-description.md)<br>
  本部分会介绍Ubuntu操作系统以及如何进行VNC配置、网络配置等操作。

- [固件说明](5.3-FirmwareFunctionDescription/3.5.3-HW-description-JN.md)  
  本部分会介绍JN版本机器人的通用硬件接口

- [mystudio介绍](5.2-Softwarelnstructions/README.md)
  一站式服务平台myStudio，整合myCobot软件资源及各类资料，支持固件下载与更新。提供产品使用视频教程以及维护/维修方面等信息。

- [TF卡更换教程以及烧录镜像](5.4-TFcard/tfcard.md)
  此版本机械臂出厂自带64G TF卡，内置Ubuntu20.04 系统，已安装myStudio 固件烧录软件，myBlockly 图形化编程软件，且已适配python 、ROS开发环境。当系统因操作不当而损坏或设置错误且无法更改时，可以重新刻录系统映像并恢复初始设置（需要SD卡读取器）

---

[← 上一章](../../2-BasicSettings/4.FirstTimeInstallation/4-FirstTimeInstallation.md) | [下一章 →](../6.developmentGuide/README.md)