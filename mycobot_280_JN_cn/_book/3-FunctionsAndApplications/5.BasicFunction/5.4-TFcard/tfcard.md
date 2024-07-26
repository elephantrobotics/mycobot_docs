### **myCobot 280 Jetson Nano**

### **更换TF卡教程**

设备底座正面展示图

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-1.png" alt="image-20221115161942636" style="zoom: 30%;" />


- 第一步：查看确认TF卡槽位置，TF卡在设备内部，这里需要动手拆除底座下盖更换

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-1.1.png" alt="image-20221115161942636" style="zoom: 30%;" />


- 第二步：取出正面的2颗固定螺丝，使用1.5十字螺丝刀

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-2.png" alt="image-20221115161942636" style="zoom: 30%;" />



- 第三步：取出底部面的6颗2*8固定螺丝，使用1.5MM十字螺丝刀

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-3.png" alt="image-20221115161942636" style="zoom: 30%;" />

- 第四步：拔开舵机（黑红白3PIN）连接线

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-4.png" alt="image-20221115161942636" style="zoom: 30%;" />


- 第五步：需拔下风扇连接线，电源指示灯连接线，电源黑红线

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-5.png" alt="image-20221115161942636" style="zoom: 60%;" />

- 第六步：取出图中绿色PCBA板，取出板上3颗固定螺丝


<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-6.png" alt="image-20221115161942636" style="zoom: 60%;" />


- 第七步：取出六角固定柱3颗

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-7.png" alt="image-20221115161942636" style="zoom: 60%;" />


- 第八步：取出主控板（请注意防静电措施）

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-8.png" alt="image-20221115161942636" style="zoom: 30%;" />


- 第九步：取出TF卡，或更换TF卡。 （请注意防静电措施）


<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-9.1.png" alt="image-20221115161942636" style="zoom: 30%;" />

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-9.2.png" alt="image-20221115161942636" style="zoom: 30%;" />


- 第十步：装回主控板

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-10.png" alt="image-20221115161942636" style="zoom: 30%;" />


- 第十一步：装配注意要点

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-11.png" alt="image-20221115161942636" style="zoom: 60%;" />

- 第十二步：装配注意要点

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-12.1.png" alt="image-20221115161942636" style="zoom: 80%;" />

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.5.4-12.2.png" alt="image-20221115161942636" style="zoom: 80%;" />  

# 镜像烧录

本章介绍镜像下载和烧录步骤，如已下载所需镜像，可直接查看烧录步骤

## 1.1 下载链接

<table>
<tr>
	<td>产品名称</td>
    <td>系统版本</td>
    <td>下载链接</td>
    <td>SHA256 Hash</td>
</tr>
<tr>
	<td>AI Kit 280</td>
    <td>ubuntu 18.04</td>
    <td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/AI_Kit/AI_myCobot_280_ubuntu_V20221030-shrink.zip">点击下载</a>
    </td>
    <td>d44439be351a52decdb4470cb623a032047e223ffce73477d29aa973bb9100e1</td>
</tr>
<tr>
	<td rowspan='2'>myCobot 280 PI</td>
	<td>ubuntu 18.04</td>
	<td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280/myCobot_280_ubuntu_V20221030-shrink.zip">点击下载</a></td>
	<td>04e40af5b637ec003a8b23ef9012e353361fd336db4e17cf9a65feb75e92927e</td>
</tr>
<tr>
	<td>ubuntu 20.04</td>
	<td> 
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280/myCobot_280_ubuntu_V20230222_20.04Pi_aarch64_shrunk.img.gz">点击下载</a>
    </td>
	<td>ce666e6c1047c512fe6b270336d472e48f231be12808729ed57f743f9d284397</td>
</tr>
<tr>
	<td>myCobot 280 JetsonNano</td>
	<td>ubuntu 18.04</td>
	<td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280JetsonNano/myCobot_280_Jetsonnano_V221101-shrink.zip">点击下载</a>
    </td>
	<td>2f1e40c1480b077bcc83abd3b79ac175f25d21e9cc344a014636167ee2eb087c</td>
</tr>
<tr>
	<td rowspan='2'>myCobot 320 PI</td>
	<td>ubuntu 18.04</td>
	<td>
        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-320/myCobot_320_ubuntu_V20220805-2.zip">点击下载</a>
                 </td>
	<td>bc2ed6ef8d51a885f45379392b71e35420638a427d5b4b3a3c9d1803d7e589eb</td>
</tr>
<tr>
	<td>ubuntu 20.04</td>
	<td><a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-320/myCobot_320_ubuntu_V20221101_20.04Pi_aarch64-shrink.zip">点击下载</a>
        </td>
	<td>c95633bfd49246254f2be4783c6a91a15212422219157962c93125092aff6b34</td>
</tr>
<tr>
	<td rowspan='2'>mechArm 270</td>
	<td>ubuntu 18.04</td>
	<td><a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/mechArm-270/mechArm270_V221030-shrink.zip">点击下载</a>
        </td>
	<td>9af1fcbf9c608eda269dc395a8d68ea0a270008a88ec8ec3cf97758371a11178<td>
​      
</tr>
<tr>
​	<td>镜像已知问题</td>
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
​	<td><a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280/myCobot_280_ubuntu_V20221030-shrink.zip">点击下载</a>
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
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-Pro-600/myCobot_Pro_600_bebian_V20230601.rar">点击下载</a>
​    </td>
​    <td>6214baba79d9afa1f9036997c31fe2a2f687e7899792b8cb1e2e80e5aa0af786</td>
</tr>
<tr>
​    <td>myBuddy 280</td>
​    <td>ubuntu 20.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myBuddy-280/myBuddy_280_ubuntu_V20221028_20.04Pi_aarch64_shrunk.img.gz">点击下载</a>
​    </td>
​    <td>2b5452f665bcb999faf1727b2103dc1e5745705f5706728e140d62906b099920</td>
​    </td>
</tr>
<tr>
​    <td>myAGV</td>
​    <td>ubuntu 18.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myAGV/myAGV_ubuntu18.04_20221028-shrink.zip">点击下载</a>
​     </td>
<td>bedad7d9769cb69380c6a4b9742ba7aefc21db41ab239172b7a5a7b632453baa</td>
</tr>
<tr>
​    <td>myAGV 2023 Pi</td>
​    <td>ubuntu 20.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myAGV/myAGV2023_ubuntu_V20240103_20.04Pi_aarch64_shrunk.img.gz">点击下载</a>
​     </td>
<td></td>
</tr>
<tr>
​    <td>myAGV 2023 JN</td>
​    <td>ubuntu 20.04</td>
​    <td>
​        <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myAGV/myAGV2023_ubuntu_V20240402_20.04JN_aarch64_shrunk.img.gz">点击下载</a>
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

## 1.2 烧录步骤

**Step 1:** 下载镜像后解压文件，可以看到一个光盘映像文件。

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/1.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 2:** 下载 Win32DiskImager 软件。

下载地址：[Win32DiskImager](https://sourceforge.net/projects/win32diskimager/)

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/2.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 3:** 取下机械臂底部的 SD 卡，使用读卡器将 SD 卡插入电脑。

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/3.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 4:** 打开 Win32DiskImager 烧录软件。

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/4.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 5:** 选择 E 盘和光盘映像文件，然后点击“写入”，即可开始写入。
<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/5.png" alt="image-20221115161942636" style="zoom: 60%;" />

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/6.png" alt="image-20221115161942636" style="zoom: 60%;" />

**Step 6:** 写入成功后会有提示。

<img src="../../../resource\3-FunctionsAndApplications\5.BasicFunction\5.4-TFcard/7.png" alt="image-20221115161942636" style="zoom: 60%;" />
