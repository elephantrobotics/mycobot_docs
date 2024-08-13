# myStudio

![Cover](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/mystudioShow.jpg)

**[myStudio video tutorial](https://www.bilibili.com/video/BV1Qr4y1N7B5/)**

## Original intention of myStudio

- myStudio is a one-stop platform for using robots such as myRobot/myCobot.

- It is convenient for users to select different firmware and download them according to their own usage scenarios, and at the same time learn related teaching materials and browse tutorial videos online.

##  Latest version of myStudio and supported platforms

- Latest version: V3.5.8

- Applicable to: Windows, Mac, Linux

## myStudio functions

- Burn and update firmware
- Provide robot tutorials, such as user manuals, video tutorials, Q&A, etc.
- Information on maintenance and repairs

## Applicable devices for myStudio

- myCobot 280

- myCobot 280 M5

- myCobot 280 PI

- myCobot 280 Jetson Nano

- myCobot 280 for Arduino

  

## Firmware version recommendation

Different models of robotic arms require different firmware to be burned. The following are the firmware versions recommended for burning different models of robotic arms.

**myCobot 280 series**

The myCobot 280 series has 4 versions: M5 version, PI version, ardunio version and jetsonnano version. Different versions have different core models, and the firmware and versions required to be burned are also different.

<table>
<tr>
<td>Robot version number</td>
<td>Core</td>
<td>Required firmware to be burned</td>
<td>Recommended firmware and version</td>
</tr>
<td rowspan='2'>PI version</td>
<td>RaspberryPI 4B</td>
<td>ubuntu firmware</td>
<td>Recommend burning V18.04. version</td>
</tr>
<tr>
<td>Atom</td>
<td>atomMain firmware</td>
<td>For products with serial numbers ER28001202200415 and earlier, or products without serial numbers, it is recommended to burn v4.1; for products with serial numbers ER28001202200416 and later, it is recommended to burn v5.1</td>
</tr>
<tr>
</table>


## Update and burn Atom firmware

Step 1: Connect to PC. Use USB to connect the Atom at the end.

![Atom link](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions\atom_PC.jpg)

Step 2: Select `ATOM` in the `Board` column, and the Atom firmware will appear in the `Basic` sidebar. There is only one Atom firmware, click to burn it (the figure below takes myCobot 280 as an example).

![Atom link](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions\atom2.jpg)