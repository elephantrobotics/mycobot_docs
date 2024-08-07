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
        <td>myCobot 280 JetsonNano</td>
        <td>ubuntu 18.04</td>
        <td>
            <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280JetsonNano/myCobot_280_Jetsonnano_V221101-shrink.zip">click to download</a>
        </td>
        <td>2f1e40c1480b077bcc83abd3b79ac175f25d21e9cc344a014636167ee2eb087c</td>
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