# Chapter 6 Software Development Guide

## 1 Usage Environment

The myCobot 280 UNO Q edition uses an **Arduino UNO Q** as the controller together with the robot arm. The UNO Q runs Debian Linux and communicates with the arm through the Bridge. You can develop and run programs from a PC (App Lab PC-hosted) or directly on the UNO Q (App Lab SBC / onboard Python).

Before you start, prepare:

- myCobot 280 for Arduino and its power supply
- Arduino UNO Q, wired for communication as delivered (typically `5V` / `GND` / `TX` / `RX`)
- A PC with a USB-C data cable, or a monitor, keyboard, mouse, and an externally powered USB hub, depending on the mode you use

**Control entry note**

The same arm can be controlled from App Lab or from onboard Python (including TCP Socket). Stop the current program before switching entries. **Only one program may send motion commands at a time.** Before any motion example, secure the base and clear the workspace.

## 2 Development Paths

This chapter provides the following paths. Follow each subsection carefully; missing steps may prevent the environment or examples from running.

[6.1 Development and Usage with Python](./6.1-python/README.md)<br>
Control the arm from the UNO Q Debian environment with the UNO Q–adapted `pymycobot` package. Initialize with `unoq_bridge=True` (no serial device name required). This section covers environment checks, APIs, TCP Socket remote control, RGB / joints / coordinates / gripper and pump, terminal joystick source, integrated examples, and troubleshooting.<br>

[6.2 Development and Usage with Arduino App Lab](./6.2-applab/README.md)<br>
Run examples through Arduino App Lab. First-time users should start with **PC-hosted**; joystick control uses **SBC** mode. This section covers App Lab install and connection, running built-in cases (or importing a ZIP), editing `python/main.py`, and App Lab joystick steps. Terminal joystick source is in 6.1.8.<br>

### Chapter Contents

- [6.1 Development and Usage with Python](./6.1-python/README.md)
  - [6.1.1 Environment and Communication Check](./6.1-python/6.1.1-Environment.md)
  - [6.1.2 API Usage](./6.1-python/6.1.2-API.md)
  - [6.1.3 TCP Socket Remote Control](./6.1-python/6.1.3-TCPSocket.md)
  - [6.1.4 RGB Control](./6.1-python/6.1.4-RGB.md)
  - [6.1.5 Joint Control](./6.1-python/6.1.5-JointControl.md)
  - [6.1.6 Coordinate Control](./6.1-python/6.1.6-CoordinateControl.md)
  - [6.1.7 Gripper and Pump Control](./6.1-python/6.1.7-GripperPump.md)
  - [6.1.8 Joystick Control (Debian Terminal and Source)](./6.1-python/6.1.8-Joystick.md)
  - [6.1.9 Integrated Demo Examples](./6.1-python/6.1.9-Examples.md)
  - [6.1.10 Logging and Troubleshooting](./6.1-python/Troubleshooting.md)
- [6.2 Development and Usage with Arduino App Lab](./6.2-applab/README.md)
  - [6.2.1 Getting Started with App Lab](./6.2-applab/6.2.1-GettingStarted.md)
  - [6.2.2 Joystick Control](./6.2-applab/6.2.2-Joystick.md)

---

[← Previous Chapter](../5.BasicFunction/README.md) | [Next Chapter →](../7.SuccessfulCase/7-SuccessfulCases.md)
