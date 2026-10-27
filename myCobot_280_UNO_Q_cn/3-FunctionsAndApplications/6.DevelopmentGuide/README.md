# 第六章 软件开发指南

## 1 使用环境

myCobot 280 UNO Q 版本以 **Arduino UNO Q** 作为控制器，与机械臂本体配合使用。UNO Q 上运行 Debian Linux，并通过 Bridge 与机械臂通信；开发与运行可在电脑侧（App Lab PC-hosted）或直接在 UNO Q 上（App Lab SBC / 板端 Python）完成。

使用前请准备：

- myCobot 280 for Arduino 及电源
- Arduino UNO Q，并按交付方式连接通信线（通常为 `5V` / `GND` / `TX` / `RX`）
- 按所选方式准备 PC（USB-C 数据线）或显示器、键鼠、带外部供电的 USB Hub 等

**控制方式说明**

同一台机械臂可通过 App Lab 或板端 Python（含 TCP Socket）控制。切换控制入口前，请先停止当前程序，**同一时刻只允许一个程序发送运动指令**。使用运动案例前，请固定机械臂底座并清空工作区域。

## 2 开发环境

为满足不同场景需求，本手册提供以下开发与使用路径。请按各小节说明逐步操作，遗漏步骤可能导致环境或案例无法正常运行。

[6.1 基于 Python 开发使用](./6.1-python/README.md)<br>
在 UNO Q 的 Debian 环境中使用 Python 与适配版 `pymycobot` 控制机械臂。初始化时使用 `unoq_bridge=True`，无需手动指定串口设备名。本节包含环境检查、API、TCP Socket 远程控制、RGB / 关节 / 坐标 / 夹爪吸泵、手柄终端与源码、综合示例及故障排查。<br>

[6.2 基于 Arduino App Lab 开发使用](./6.2-applab/README.md)<br>
通过 Arduino App Lab 导入完整案例 ZIP 并运行。首次客户推荐 **PC-hosted**；手柄控制使用 **SBC** 模式。本节说明 App Lab 安装与连接、导入运行与二次修改 `python/main.py`，以及 App Lab 下手柄控制步骤。板端终端手柄源码见 6.1.8。<br>

### 本章目录

- [6.1 基于 Python 开发使用](./6.1-python/README.md)
  - [6.1.1 环境与通信检查](./6.1-python/6.1.1-Environment.md)
  - [6.1.2 API 使用说明](./6.1-python/6.1.2-API.md)
  - [6.1.3 TCP Socket 远程控制](./6.1-python/6.1.3-TCPSocket.md)
  - [6.1.4 RGB 控制](./6.1-python/6.1.4-RGB.md)
  - [6.1.5 关节控制](./6.1-python/6.1.5-JointControl.md)
  - [6.1.6 坐标控制](./6.1-python/6.1.6-CoordinateControl.md)
  - [6.1.7 夹爪与吸泵控制](./6.1-python/6.1.7-GripperPump.md)
  - [6.1.8 手柄控制（Debian 终端与源码）](./6.1-python/6.1.8-Joystick.md)
  - [6.1.9 综合演示案例](./6.1-python/6.1.9-Examples.md)
  - [6.1.10 日志与故障排查](./6.1-python/Troubleshooting.md)
- [6.2 基于 Arduino App Lab 开发使用](./6.2-applab/README.md)
  - [6.2.1 App Lab 基础使用](./6.2-applab/6.2.1-GettingStarted.md)
  - [6.2.2 手柄控制](./6.2-applab/6.2.2-Joystick.md)

---

[← 上一章](../5.BasicFunction/README.md) | [下一章 →](../7.SuccessfulCase/7-SuccessfulCases.md)
