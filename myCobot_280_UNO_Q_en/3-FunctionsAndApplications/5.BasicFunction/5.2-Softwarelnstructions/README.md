# myStudio

![Cover](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/mystudioShow.jpg)

**[myStudio video tutorial](https://www.bilibili.com/video/BV1Qr4y1N7B5/)**

## 1 Original intention of myStudio

- myStudio is a one-stop platform for using robots such as myRobot/myCobot.

- It is convenient for users to select different firmware and download them according to their own usage scenarios, and at the same time learn related teaching materials and browse tutorial videos online.

## 2 Latest version of myStudio and supported platforms

- Latest version: V3.5.8

- Applicable to: Windows, Mac, Linux

## 3 myStudio functions

- Burn and update firmware
- Provide robot tutorials, such as user manuals, video tutorials, Q&A, etc.
- Information on maintenance and repairs

## 4 Applicable devices for myStudio

- myCobot 280
- myCobot 280 M5
- myCobot 280 PI
- myCobot 280 Jetson Nano
- **myCobot 280 for Arduino**

## 5 Firmware version recommendation

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
<tr>
<td rowspan='2'>M5 version</td>
<td>M5Stack-Basic</td>
<td>miniRobot firmware</td>
<td>Recommended to burn v2.1 version, you can use drag teaching, wifi, Bluetooth and other functions</td>
</tr>
<tr>
<td>Atom</td>
<td>atomMain firmware</td>
<td>For products with serial numbers ER28001202200415 and earlier, or products without serial numbers, it is recommended to burn v4.1; for products with serial numbers ER28001202200416 and later, it is recommended to burn v5.1</td>
</tr>
<tr>
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
<td rowspan='3'>Arduino version</td>
<td>mega2560</td>
<td>transponder firmware</td>
<td>Recommend burning v1.0 version</td>
</tr>
<td>mkrwifi1010</td>
<td>transponder firmware</td>
<td>Recommend burning v1.0 version</td>
</tr>
<tr>
<td>Atom</td>
<td>atomMain firmware</td>
<td>For products with serial numbers of ER28001202200415 and earlier, or products without serial numbers, it is recommended to burn v4.1; for products with serial numbers of ER28001202200416 and later, it is recommended to burn v5.1</td>
</tr>
<tr>
<td rowspan='2'>Jetson nano version</td>
<td>JestonNano</td>
<td>ubuntu firmware</td>
<td>Recommend burning V18.04. version</td>
</tr>
<tr>
<td>Atom</td>
<td>atomMain firmware</td>
<td>For products with serial numbers of ER28001202200415 and earlier, or products without serial numbers, it is recommended to burn v4.1; for products with serial numbers of ER28001202200416 and later, it is recommended to burn v5.1</td>
</tr>
</table>

## myStudio environment setup
## myStudio download and installation

>Note: The installation path of myStudio cannot have any spaces

Download address:

**1. [GitHub address](https://github.com/elephantrobotics/myStudio)**

* After entering the download address, click `myStudio` on the right and select the corresponding version to download.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/mystudiogithub.jpg" style="zoom: 35%;" />

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/githubassets.jpg" style="zoom: 67%;" />

* Different suffixes represent different systems, please download the corresponding version:
* *.tra.xz —— Linux system
* *.dmg —— Mac system
* *.exe —— Window system

**2. [Official website address](https://www.elephantrobotics.com/download/)**

You can download it according to your computer system.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/mystudiodownload.jpg" style="zoom: 50%;" />

> **Note:** Please download the latest version. You can view the current version in the downloaded myStudio interface and update to the latest version.
>
> <img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/mystudiorenew.jpg" style="zoom: 33%;" />

## Install the driver

Users can click the button below to download the corresponding **CP210X** or **CP34X** driver package according to their operating system. After decompressing the package, select the installation package corresponding to the operating system bit number for installation.

There are currently two driver chip versions, **CP210X** (for CP2104 version) and **CP34X** (for CH9102 version) driver compression packages. If you are not sure which USB chip your device uses, you can install both drivers at the same time. ( **CH9102_VCP_SER_MacOS** may show an error during installation, but it has actually been installed, so just ignore it.)

For Mac OS, make sure the system "Preferences->Security and Privacy->General" is set before installation, and allow downloads from the App Store and approved developers.

- Download the bottom **M5Stack-basic** serial port driver

- **CP210X**
- [ **Windows10** ](https://download.elephantrobotics.com/software/drivers/CP210x_VCP_Windows.zip)
- [ **MacOS** ](https://download.elephantrobotics.com/software/drivers/CP210x_VCP_MacOS.zip)
- [ **Linux** ](https://download.elephantrobotics.com/software/drivers/CP210x_VCP_Linux.zip)

* **CP34X**

- [ **Windows10** ](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_SER_Windows.exe)

- [ **MacOS** ](https://download.elephantrobotics.com/software/drivers/CH9102_VCP_MacOS.zip)

- Download the terminal **Atom** serial port driver
- [ **Windows10** ](https://download.elephantrobotics.com/software/drivers/CDM21228_Setup.zip)

![P210X_install](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/4.1.1.2-CP210X_install.gif)

## How to distinguish CP210X and CP34X chips

- As shown in the figure below, open **Device Manager** and check **Ports (COM and LPT)**

![frimware_check](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/4.1.1.3-firmware_check.gif)

* If **Port (COM and LPT)** shows **USB-Enhanced-SERIAL CH9102**, it is **CP34X chip**

![CP34X](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/4.1.1.3-CP34X.png)

* If **Port (COM and LPT)** shows **Silicon Labs CP210x USB to UART Bridge**, it is **CP210X chip**

![CP210C](../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.2-Softwarelnstructions/4.1.1.3-CP210X.png)

## Burn and update firmware

**[myStudio video tutorial](https://www.bilibili.com/video/BV1Qr4y1N7B5/)**

