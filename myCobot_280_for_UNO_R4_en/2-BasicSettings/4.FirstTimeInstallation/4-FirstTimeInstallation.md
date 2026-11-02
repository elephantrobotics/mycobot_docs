# Chapter 4 First Use
## 1. Product Standard List
## 1.1 Product List Image
> Thank you for choosing the Elephant Robot myCobot 280 For Arduino Robotic Arm. This chapter is designed to help you easily get started with the Elephant Robotic product and enjoy every wonderful moment brought by the product.

![Unboxing Kit](../../resource/2-BasicSettings/4.FirstTimeInstallation/r4-packing-list.jpg)

## 1.2 Product Standard List Comparison Table

| Serial Number | Product |
| :----: | :------------------------------------------- |
| 1 | myCobot Robotic Arm (Model myCobot 280 For Arduino) |
| 2 | myCobot Robotic Arm-Product Brochure |
| 3 | myCobot Robotic Arm-Matching Power Cord |
| 4 | USB-Type C |
| 5 | Several Dupont Wires |

**Note:** After the packaging box arrives, please confirm that the robot packaging is intact. If there is any damage, please contact the logistics company and the supplier in your area in time. After unpacking, please check the actual items in the box according to the list of items.

---
## 2. Product unpacking guide
## 2.1 Product unpacking graphic guide

**Why do you need to disassemble the product according to the steps**

In this section, we strongly recommend disassembling the product according to the specified steps. This not only helps to ensure that the product is not damaged during transportation, but also minimizes the risk of unexpected failures. Please read the following graphic guide carefully to ensure the safety of your product during the unpacking process.

- **1** Check the packaging box for damage. If there is any damage or missing accessories, please contact the logistics company and the supplier in your area in time.

- **2** Open the box and take out the product brochure, sponge packaging cover, myCobot robot arm, matching power supply, flat base and accessory bag.

- **3** Make sure each step is completed before proceeding to the next step to prevent unnecessary damage or omissions.

**Note:** After taking out the product, please carefully check the appearance of each item. Please check the actual items in the box against the list of items.

## 3. Startup Inspection Guide
## 3.1 Structural Installation and Fixing

During the movement of the **robotic arm**, if the **bottom surface of myCobot is not connected to the desktop or other bottom surface**, myCobot will still **shake or overturn**.

**There are three common ways to fix the robotic arm**:

1) Use Lego keys to fix it on a base with a Lego interface

We sell two types of bases: flat suction cup base and G-type clamp base
![Base](../../resource/2-BasicSettings/4.FirstTimeInstallation/stand.jpg)
​ Flat base Applicable model: myCobot 280

* Install suction cups at the four corners of the base and tighten them.

* Use the included Lego technology parts to connect the flat base and the bottom of the robotic arm.

* Fix the four suction cups on a flat and smooth surface before starting to use.
* Tips: You can add a small amount of non-conductive liquid under the suction cup to fill the gap between the suction cup and the desktop to achieve the best adsorption effect.
![Base 2](../../resource/2-BasicSettings/4.FirstTimeInstallation/stand_2.jpg)

---

G-type base Applicable models: myCobot 280 series, myPalletizer 260

![G base](../../resource/2-BasicSettings/4.FirstTimeInstallation/r4-gstand-parts.jpg)

- Use the G-clip to fix the base to the edge of the table

- Use the included Lego tech parts to connect the base and the bottom of the robot arm

- Make sure it is stable before starting to use

![G base 2](../../resource/2-BasicSettings/4.FirstTimeInstallation/r4-mounted-on-base.jpg)

2 myCobot base screw hole connection

The robot needs to be fixed on a solid base before it can be used normally. Base weight requirements: fixed base, or mobile base.

Please make sure that there are corresponding threaded holes on the fixed base before installation.

Before formal installation, please confirm:

* The installation environment meets the requirements of the above "Working Environment and Conditions" table.

* The installation location is not less than the robot's working range, and there is enough space for installation, use, maintenance, and repair.

* Place the base in a suitable position.

* The installation-related tools are ready, such as screws, wrenches, etc.

**After confirming the above content**, please move the robot to the base installation table, adjust the robot position, and align the robot base fixing holes with the holes on the base installation table. After aligning the holes, align the screws with the holes and tighten them.

* Note: When adjusting the robot position on the base installation table, please try to avoid pushing and pulling the robot directly on the base installation table to avoid scratches. When manually moving the robot, please try to avoid applying external force to the fragile parts of the robot body to avoid unnecessary damage to the robot.

---
## 4. Power on and preliminary inspection
## Power on the robot

Before operation, please make sure you have read and followed the contents of **Chapter 1 Safety Instructions** to ensure safe operation. At the same time, connect the power adapter to the robot arm and fix the base of the robot arm on the table. The connection method is shown in Figure 3-1:

<img src="../../resource/2-BasicSettings/4.FirstTimeInstallation/2.1.8.3-2-001.png" alt="2.1.5.3-2-001" style="zoom:80%;" />

Figure 3-1

myCobot **must be powered by an external power supply** to provide sufficient power:

- Rated voltage: 12V
- Rated current: 3-5A
- Plug type: DC 5.5mm x 2.1

Note that **it cannot be powered by just the TypeC plugged into the M5Stack-basic**. Use the official power adapter to avoid damage to the robot arm.

## Connect external devices

- Connect to the computer via USB

<img src="../../resource/2-BasicSettings/4.FirstTimeInstallation/2111pic4.png" alt="img" style="zoom:100%;" />

Figure 3-2 USB interface connection diagram

## Robot working status detection
## Unboxing video

<video id="my-video" class="video-js" controls preload="auto" width="100%"
poster="" data-setup='{"aspectRatio":"16:9"}'>
<source src="https://www.elephantrobotics.com/wp-content/uploads/2022/05/Arduino%E8%A7%86%E9%A2%91%E7%9A%84%E6%9B%B4%E6%8D%A2%E4%B8%AD.mp4#t=4"></video>

## Hardware connection

**Note:** The current 280AR serial port baud rate is 1000000.

| Development board type | Baud rate | Control method | Wiring method |
| :------: | :----------------------: | :----------------------: | :-----------------: |
| UNO R4 | 1000000 | Arduino IDE / python | TX-->TX、RX-->RX、GND-->GND |

**Power the arm down before wiring.**

The UNO R4's D0/D1 connect **straight through** to the pads of the same name on
the base: TX to TX, RX to RX. Do not cross the wires yourself. Ground must be
common.

The base header, with the RX, TX and GND pads labelled:

![base header](../../resource/2-BasicSettings/4.FirstTimeInstallation/r4-wiring-base-header.jpg)

The same three wires on the UNO R4's own pin header:

![board pins](../../resource/2-BasicSettings/4.FirstTimeInstallation/r4-wiring-board-pins.jpg)

**Why straight through?** The base's function interface groups 1 and 4 follow
the Arduino UNO pin layout, and the UNO R4 uses that same layout. The pads are
labelled from the board's point of view, so the pad marked `RX` is where the
board's RX pin goes, and the base handles the crossover internally.

A MEGA 2560 is wired differently (TX1-->RX, RX1-->TX) because it uses TX1/RX1
rather than the shield's D0/D1 pins.

Note that the `MyCobot_Mkr` setting in `ParameterList.h` is unrelated to the
wiring - it only selects which serial port the library uses in software
(`Serial1`, which is D0/D1 on the UNO R4).

## 5. Common Problem Solving
This section aims to help users solve common problems encountered during use, covering hardware, software, accessories, and how to self-check for the first time. If you encounter problems while using the robot arm, please read the contents of this section first to find solutions. If the listed problems cannot help you solve and you have more after-sales questions to consult, please add the after-sales butler WeChat.

[First-time self-check](../../4-SupportAndService/9.Troubleshooting/9.4-first-time-self-check.md)

[Common software problems and solutions](../../4-SupportAndService/9.Troubleshooting/9.2-software.md)

[Common hardware problems and solutions](../../4-SupportAndService/9.Troubleshooting/9.3-hardware.md)

[Common accessories problems and solutions](../../4-SupportAndService/9.Troubleshooting/9.1-accessories.md)

[Other problems and solutions](../../4-SupportAndService/9.Troubleshooting/9.0-other.md)

---

If you have read all the contents of this chapter, please continue to read the next chapter. <br>
[← Previous Chapter](../3.UserNotice/3-UserInstructions.md) | [Next Chapter →](../../3-FunctionsAndApplications/5.BasicFunction/README.md)