# 6.2 基于 Arduino App Lab 开发使用

本节介绍如何用 **Arduino App Lab** 连接 UNO Q，并导入、运行、修改 myCobot 280 案例。

## 适用说明

- **适用对象**：首次使用客户、希望用图形化 App Lab 运行案例的用户。
- **推荐路径**：先按 [6.2.1](./6.2.1-GettingStarted.md) 完成 PC-hosted 连接与 RGB 验证；手柄控制使用 SBC 模式，见 [6.2.2](./6.2.2-Joystick.md)。
- **与 Python 节的关系**：板端 Debian 脚本、TCP Socket、API 与终端手柄源码见 [6.1 基于 Python 开发使用](../6.1-python/README.md)。本节不展开板端终端开发。
- **案例入口**：可在 App Lab **Apps** 页打开 myCobot **Built-in Case**；也可用完整 App ZIP 导入。App 内通常含 `app.yaml`、`python/main.py`、`requirements.txt` 与 UNO Q 适配版 `pymycobot` wheel（当前无需 `sketch/`）。

同一时刻只允许一个程序控制机械臂。切换案例前请先 **Stop**。

## 本节目录

- [6.2.1 App Lab 基础使用](./6.2.1-GettingStarted.md)
- [6.2.2 手柄控制](./6.2.2-Joystick.md)

[← 上一节](../README.md) | [下一节 →](./6.2.1-GettingStarted.md)
