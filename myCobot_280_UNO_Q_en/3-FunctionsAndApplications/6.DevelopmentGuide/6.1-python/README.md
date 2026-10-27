# 6.1 Development and Usage with Python

This section describes how to control myCobot 280 with Python and the UNO Q–adapted `pymycobot` package in the **Arduino UNO Q** Debian environment.

## Scope

- **Audience**: Users who write scripts on the board, debug APIs, or use TCP Socket remote control over a LAN.
- **Relation to App Lab**: For first-time ZIP/built-in case runs, start with [6.2 Development and Usage with Arduino App Lab](../6.2-applab/README.md). This section focuses on onboard Python. App Lab joystick: [6.2.2](../6.2-applab/6.2.2-Joystick.md). Terminal joystick and source: [6.1.8](./6.1.8-Joystick.md).
- **Communication**: Initialize with `MyCobot280(unoq_bridge=True)`. No serial device name is required; the UNO Q forwards arm traffic.
- **Dependencies**: Use the UNO Q–adapted `pymycobot` wheel from the delivery package. Do not replace it with a standard, unadapted package.

> Before any motion example, secure the arm, clear the workspace, and stop App Lab, TCP clients, and other control entries. Verify read-only communication and RGB first, then run motion examples.

## Section Contents

- [6.1.1 Environment and Communication Check](./6.1.1-Environment.md)
- [6.1.2 API Usage](./6.1.2-API.md)
- [6.1.3 TCP Socket Remote Control](./6.1.3-TCPSocket.md)
- [6.1.4 RGB Control](./6.1.4-RGB.md)
- [6.1.5 Joint Control](./6.1.5-JointControl.md)
- [6.1.6 Coordinate Control](./6.1.6-CoordinateControl.md)
- [6.1.7 Gripper and Pump Control](./6.1.7-GripperPump.md)
- [6.1.8 Joystick Control](./6.1.8-Joystick.md)
- [6.1.9 Integrated Demo Examples](./6.1.9-Examples.md)
- [6.1.10 Logging and Troubleshooting](./Troubleshooting.md)

[← Previous Section](../README.md) | [Next Section →](./6.1.1-Environment.md)
