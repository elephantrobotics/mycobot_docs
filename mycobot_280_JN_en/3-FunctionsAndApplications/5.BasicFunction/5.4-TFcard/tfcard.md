### **myCobot 280 Jetson Nano**

### **Tutorial on replacing TF card**

Front view of the device base

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-1.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 1: Check and confirm the position of the TF card slot. The TF card is inside the device. You need to remove the bottom cover of the base to replace it.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-1.1.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 2: Remove the two fixing screws on the front, using a 1.5 Phillips screwdriver

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-2.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 3: Remove the six 2*8 fixing screws on the bottom, using a 1.5MM Phillips screwdriver

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-3.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 4: Unplug the servo (black, red, and white 3PIN) connection cable

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-4.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 5: Unplug the fan connection cable, power indicator connection cable, and power black and red cable

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-55.png" alt="image-20221115161942636" style="zoom: 80%;" />

- Step 6: Remove the green PCBA board in the picture and the three fixing screws on the board

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-66.png" alt="image-20221115161942636" style="zoom: 80%;" />

- Step 7: Remove the three hexagonal fixing columns

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-77.png" alt="image-20221115161942636" style="zoom: 80%;" />

- Step 8: Remove the main control board (please pay attention to anti-static measures)

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-8.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 9: Remove the TF card or replace it. (Please pay attention to anti-static measures)

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-9.1.png" alt="image-20221115161942636" style="zoom: 30%;" />

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-9.2.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 10: Reinstall the main control board

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-10.png" alt="image-20221115161942636" style="zoom: 30%;" />

- Step 11: Assembly points

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-111.png" alt="image-20221115161942636" style="zoom: 60%;" />

- Step 12: Assembly points

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-12.11.png" alt="image-20221115161942636" style="zoom: 80%;" /> 

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-12.22.png" alt="image-20221115161942636" style="zoom: 80%;" />

# Image Burning

This chapter introduces the image download and burning steps. If you have downloaded the required image, you can directly view the burning steps

## 1.1 Download Link

<table>
<tr>
	<td>Product Name</td>
    <td>System Version</td>
    <td>Download Link</td>
    <td>SHA256 Hash</td>
</tr>
<tr>
	<td>AI Kit 280</td>
    <td>ubuntu 18.04</td>
    <td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/AI_Kit/AI_myCobot_280_ubuntu_V20221030-shrink.zip">click to download</a>
    </td>
    <td>d44439be351a52decdb4470cb623a032047e223ffce73477d29aa973bb9100e1</td>
</tr>
<tr>
	<td rowspan='2'>myCobot 280 PI</td>
	<td>ubuntu 18.04</td>
	<td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280/myCobot_280_ubuntu_V20221030-shrink.zip">click to download</a></td>
	<td>04e40af5b637ec003a8b23ef9012e353361fd336db4e17cf9a65feb75e92927e</td>
</tr>
<tr>
	<td>ubuntu 20.04</td>
	<td> 
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280/myCobot_280_ubuntu_V20230222_20.04Pi_aarch64_shrunk.img.gz">click to download</a>
    </td>
	<td>ce666e6c1047c512fe6b270336d472e48f231be12808729ed57f743f9d284397</td>
</tr>
<tr>
	<td>myCobot 280 JetsonNano</td>
	<td>ubuntu 18.04</td>
	<td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280JetsonNano/myCobot_280_Jetsonnano_V221101-shrink.zip">click to download</a>
    </td>
	<td>2f1e40c1480b077bcc83abd3b79ac175f25d21e9cc344a014636167ee2eb087c</td>
</tr>
<tr>
	<td rowspan='2'>myCobot 320 PI</td>
	<td>ubuntu 18.04</td>
	<td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-320/myCobot_320_ubuntu_V20220805-2.zip">click to download</a>
                 </td>
	<td>bc2ed6ef8d51a885f45379392b71e35420638a427d5b4b3a3c9d1803d7e589eb</td>
</tr>
<tr>
	<td>ubuntu 20.04</td>
	<td><a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-320/myCobot_320_ubuntu_V20221101_20.04Pi_aarch64-shrink.zip">click to download</a>
        </td>
	<td>c95633bfd49246254f2be4783c6a91a15212422219157962c93125092aff6b34</td>
</tr>
<tr>
	<td rowspan='2'>mechArm 270</td>
	<td>ubuntu 18.04</td>
	<td><a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/mechArm-270/mechArm270_V221030-shrink.zip">click to download</a>
        </td>
	<td>9af1fcbf9c608eda269dc395a8d68ea0a270008a88ec8ec3cf97758371a11178<td>
​      
</tr>
<tr>
​	<td>not available</td>
​	<td>无法使用moveit</td>
​	<td>
    解决方法：
 </br>执行moveit会出现以下提示，说明没有赋予权限:
     <img src="../../resourse/19-mirroring/15.2-mirroring-burning/15.2No permission.png">
​   </br>进入如图所示路径，赋予该py文件可执行权限即可
​        <img src="../../resourse/19-mirroring/15.2-mirroring-burning/15.2give permission.png">
    </br>执行moveit会出现以下提示，说明代码内编码格式错误: 
    <img src="../../resourse/19-mirroring/15.2-mirroring-burning/15.2encoding error.png">
    </br>进入如图所示路径，打开该py文件在顶部输入：#coding=utf8 保存即可
     <img src="../../resourse/19-mirroring/15.2-mirroring-burning/15.2coding.png">
    </td>
</tr>
<tr>
​	<td rowspan='2'>myPalletizer 260</td>
​	<td>ubuntu 18.04</td>
​	<td><a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280/myCobot_280_ubuntu_V20221030-shrink.zip">click to download</a>
​    </td>
​	<td>f6fe999519146428e4c60960b242f647ae5c73c704852d686b28580b3a3f695d</td>
</tr>
<tr>
​	<td>ubuntu 20.04</td>
​	<td>-</td>
​	<td>-</td>
</tr>
<tr>
​    <td>myCobot Pro 600</td>
​    <td>Raspberry Debian</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-Pro-600/myCobot_Pro_600_bebian_V20230601.rar">click to download</a>
​    </td>
​    <td>6214baba79d9afa1f9036997c31fe2a2f687e7899792b8cb1e2e80e5aa0af786</td>
</tr>
<tr>
​    <td>myBuddy 280</td>
​    <td>ubuntu 20.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myBuddy-280/myBuddy_280_ubuntu_V20221028_20.04Pi_aarch64_shrunk.img.gz">click to download</a>
​    </td>
​    <td>2b5452f665bcb999faf1727b2103dc1e5745705f5706728e140d62906b099920</td>
​    </td>
</tr>
<tr>
​    <td>myAGV</td>
​    <td>ubuntu 18.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myAGV/myAGV_ubuntu18.04_20221028-shrink.zip">click to download</a>
​     </td>
<td>bedad7d9769cb69380c6a4b9742ba7aefc21db41ab239172b7a5a7b632453baa</td>
</tr>
<tr>
​    <td>myAGV 2023 Pi</td>
​    <td>ubuntu 20.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myAGV/myAGV2023_ubuntu_V20240103_20.04Pi_aarch64_shrunk.img.gz">click to download</a>
​     </td>
<td></td>
</tr>
<tr>
​    <td>myAGV 2023 JN</td>
​    <td>ubuntu 20.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myAGV/myAGV2023_ubuntu_V20240402_20.04JN_aarch64_shrunk.img.gz">click to download</a>
​     </td>
<td></td>
</tr>
<tr>
​    <td>marsCat</td>
​    <td>-</td>
​    <td>-</td>
​    <td>-</td>
</tr>
</table>


## 1.2 Burning steps

**Step 1:** After downloading the image, unzip the file and you will see a CD image file.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/1.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 2:** Download Win32DiskImager software.

Download address: [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/2.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 3:** Remove the SD card at the bottom of the robot arm and insert the SD card into the computer using a card reader.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 4:** Open Win32DiskImager burning software.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/4.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 5:** Select the E drive and the CD image file, then click "Write" to start writing.
<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/5.png" alt="image-20221115161942636" style="zoom: 60%;" />

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/6.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 6:** There will be a prompt after writing successfully.

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/7.png" alt="image-20221115161942636" style="zoom: 60%;" />