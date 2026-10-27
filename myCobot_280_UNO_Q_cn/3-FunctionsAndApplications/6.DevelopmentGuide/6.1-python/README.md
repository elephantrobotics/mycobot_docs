# 6.1 基于 Python 开发使用

本节介绍在 **Arduino UNO Q** 的 Debian 环境中，使用 Python 与适配版 `pymycobot` 控制 myCobot 280。

## 适用说明

- **适用对象**：需要在板端编写脚本、调试 API，或通过局域网做 TCP Socket 远程控制的用户。
- **与 App Lab 的关系**：首次导入 ZIP、快速验证案例请优先看 [6.2 基于 Arduino App Lab 开发使用](../6.2-applab/README.md)。本节偏板端 Python 与二次开发；App Lab 手柄见 [6.2.2](../6.2-applab/6.2.2-Joystick.md)，终端手柄与源码见 [6.1.8](./6.1.8-Joystick.md)。
- **通信方式**：初始化使用 `MyCobot280(unoq_bridge=True)`，无需填写串口设备名；UNO Q 会自动转发机械臂通信。
- **依赖**：请使用交付包中的 UNO Q 适配版 `pymycobot`，不要替换为未适配的普通版本。

> 所有运动示例都应先固定机械臂、清空工作区域，并停止 App Lab、TCP 客户端等其他控制入口。建议先完成只读通信和 RGB 测试，再运行运动案例。

## 本节目录

- [6.1.1 环境与通信检查](./6.1.1-Environment.md)
- [6.1.2 API 使用说明](./6.1.2-API.md)
- [6.1.3 TCP Socket 远程控制](./6.1.3-TCPSocket.md)
- [6.1.4 RGB 控制](./6.1.4-RGB.md)
- [6.1.5 关节控制](./6.1.5-JointControl.md)
- [6.1.6 坐标控制](./6.1.6-CoordinateControl.md)
- [6.1.7 夹爪与吸泵控制](./6.1.7-GripperPump.md)
- [6.1.8 手柄控制](./6.1.8-Joystick.md)
- [6.1.9 综合演示案例](./6.1.9-Examples.md)
- [6.1.10 日志与故障排查](./Troubleshooting.md)

[← 上一节](../README.md) | [下一节 →](./6.1.1-Environment.md)
