# 第七章 UNO Q 开发板使用指南

Arduino UNO Q 同时包含运行 Debian Linux 的 MPU 和运行 Arduino Sketch 的 MCU。myCobot 280 通过 UNO Q 的 Bridge 通信链路实现 App Lab、UNO Q Python 和局域网远程控制。

本章介绍以下内容：

- [7.1 UNO Q 与 Arduino App Lab 快速入门](7.1-GettingStarted.md)
- [7.2 Python 开发](7.2-Python.md)
  - [7.2.1 环境与通信检查](python/7.2.1-Environment.md)
  - [7.2.2 API 使用说明](python/7.2.2-API.md)
  - [7.2.3 RGB 与 IO 控制](python/7.2.3-RGBIO.md)
  - [7.2.4 关节控制](python/7.2.4-JointControl.md)
  - [7.2.5 坐标控制](python/7.2.5-CoordinateControl.md)
  - [7.2.6 夹爪与吸泵控制](python/7.2.6-GripperPump.md)
  - [7.2.7 综合演示案例](python/7.2.7-Examples.md)
- [7.3 TCP Socket 远程控制](7.3-TCPSocket.md)
- [7.4 SBC 手柄控制](7.4-Joystick.md)
- [7.5 性能、日志与故障排查](7.5-Troubleshooting.md)

> 使用运动案例前，请固定机械臂并清空工作区域。同一时刻只能由一个程序发送运动指令。

[← 上一章](../6.developmentGuide/README.md) | [下一章 →](../8.SuccessfulCase/8-SuccessfulCases.md)





