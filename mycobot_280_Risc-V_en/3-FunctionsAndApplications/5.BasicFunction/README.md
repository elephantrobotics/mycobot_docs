# Chapter 5 Basic Functions

**This chapter mainly explains the basic functions and usage of the product and the use of basic software. This chapter is very important and should be read carefully in order. Before actually applying the robot, please make sure you understand the described operations correctly.**

#### About the difference between M5 version and RISC-V version machine

The M5 version machine is a joint product of Elephant Robot and Shenzhen Mingzhan Technology Co., Ltd. - M5STACK. It uses the Esp32 core processor and has two display screens and multiple physical buttons. The RISC-V version of the machine is an official joint product of Elephant Robotics and Spacemit. The robotic arm uses the Spacemit K1 RISC-V AI processor and is designed to meet customers' needs for Linux system applications and the need for an all-in-one integrated robot for convenient development.

**PI model robot is a computer host**

The RISC-V version of the machine has Bianbu OS, a 1.6GHz 8-core microprocessor, runs the Ubuntu platform, supports 4 USB3.0, 2 HDMI, a standardized GPIO interface, and a pluggable TF card.

The essence of the RISC-V version machine is a development board with an independent system. It can be regarded as a miniature computer host. The host and the host cannot simply communicate through a line. It can only be connected to an independent monitor, and equipped with a power supply, mouse and keyboard, and then developed and operated after entering the built-in system of the development board.

**❗❗❗❗❗❗❗❗❗❗❗ Tips⚠: Please use the HDMI cable delivered with the package to connect the monitor and use the built-in system for development❗❗❗❗❗❗❗❗❗❗❗**

Please follow the following chapters to learn about the RISC-V version of the robotic arm.

- [RISC-V Robotic Arm Introduction](5.1-Functionlnstruction/3.5.1-SW-description.md)
  
    This section will introduce how to quickly get started with the RISC-V version of the robot and how to update the operating system.

- [System Basic Function Description](5.2-Softwarelnstructions/3.5.2-SW-detail-description.md)

    This section will introduce the Bianbu OS operating system and how to configure Bluetooth, VNC, network configuration, and use the Titan flashing tool.

- [Firmware Description](5.3-FirmwareFunctionDescription/README.md)

    This section will introduce the general hardware interface of the RISC-V version of the robot, the factory firmware, and the use of the Titan flashing tool.

- [Titan Flash Tool](5.2-Softwarelnstructions/README.md)

    myCobot 280 Risc-V uses the Titan Flash Tool independently developed by Jindie Space Technology Co., Ltd. to burn the firmware.

---

[← Previous Chapter](../../2-BasicSettings/4.FirstTimeInstallation/4-FirstTimeInstallation.md) | [Next Chapter →](../6.developmentGuide/README.md)