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
        <td rowspan='3'>myCobot 280 JetsonNano</td>
        <td>ubuntu 18.04</td>
        <td>
            <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280JetsonNano/myCobot_280_Jetsonnano_V221101-shrink.zip">点击下载</a>
        </td>
        <td>2f1e40c1480b077bcc83abd3b79ac175f25d21e9cc344a014636167ee2eb087c</td>
    </tr>
    <tr>
        <td>ubuntu 20.04</td>
        <td>
            <a href="https://download-elephantrobotics.oss-cn-shenzhen.aliyuncs.com/Product_software/iMage-ISO/myCobot-280JetsonNano/myCobot_280_ubuntu_V20231023_20.04JN_aarch64_shrunk.img.gz">点击下载</a>
        </td>
        <td>2024/10/09前购买的机器请烧录此镜像系统</td>
    </tr>
    <tr>
        <td>ubuntu 20.04 V20241108</td>
        <td>
            <a href="https://download.elephantrobotics.com/Product_software/iMage-ISO/myCobot-280JetsonNano/myCobot_280_ubuntu_V20241108_20.04JN_aarch64.tar.gz">点击下载</a>
        </td>
        <td>2024/10/09后购买的机器请烧录此镜像系统</td>
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

