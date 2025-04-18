# mycobot280RDKX5视觉套装

## 1 软件环境配置

在终端输入下面指令,按下键盘回车键,将程序克隆到本地
```bash
git clone https://github.com/elephantrobotics/mycobot280RDKX5_vision_kit.git
```

在终端输入下面指令,按下键盘回车键,进入克隆的文件夹
```bash
cd mycobot280RDKX5_vision_kit
```

在终端输入下面指令,按下键盘回车键,安装需要的依赖库
```bash
pip install -r requirements.txt
```

## 2 硬件安装

将地图放置在桌子的边缘，方便后面机械臂固定

<img src="./rdk_kit_img/rdk1.jpg" style="zoom: 50%;" />

将底座对准机械臂的底部安装孔，用内六角扳手进行固定

<img src="./rdk_kit_img/rdk8.jpg" style="zoom: 50%;" />

再用G型夹将机械臂固定到地图的机械臂固定区域

<img src="./rdk_kit_img/rdk2.jpg" style="zoom: 50%;" />

尽量将底座和矩形框贴合

<img src="./rdk_kit_img/rdk3.jpg" style="zoom: 50%;" />


进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键,机械臂各个关节会回到零位
```bash
python robot_test.py
```

然后将相机务必按照图片的位置安装到机械臂末端法兰上，否则会导致后面的案例程序则无法正常运行。
**注意：** 待机械臂回到零位后，观察J6是否处在，若不在的话，需要对机械臂进行零位校准操作

<img src="./rdk_kit_img/rdk4.jpg" style="zoom: 50%;" />

安装完后，需对比一下实物和图片安装是否一致。

<img src="./rdk_kit_img/rdk5.jpg" style="zoom: 50%;" />

然后将末端吸盘安装到相机的乐高插件孔中

<img src="./rdk_kit_img/rdk6.jpg" style="zoom: 50%;" />

之后将吸泵盒的控制线按照图片进行连接

<img src="./rdk_kit_img/rdk9.jpg" style="zoom: 50%;" />

将相机线接入底部主控的USB接口

<img src="./rdk_kit_img/rdk10.jpg" style="zoom: 50%;" />


## 3 案例复现

**注意**：若要切换案例，需要先把当前案例程序结束掉。先把木块放到拍摄区，再运行案例程序

### stag二维码分拣
将4个木块贴着stag码朝上放置到拍摄区，尽量放置在中间，避免机械臂限位

<img src="./rdk_kit_img/rdk_stag1.jpg" style="zoom: 30%;" />

进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键后，稍等一段时间，就会打开一个相机窗口，识别成功后，机械臂就会开始抓取
```bash
python stag_demo.py
```

<img src="./rdk_kit_img/rdk_stag2.jpg" style="zoom: 30%;" />

### 颜色分拣
将4个木块没有贴纸的一面朝上放置到拍摄区，尽量放置在中间，避免机械臂限位

<img src="./rdk_kit_img/rdk_color.jpg" style="zoom: 30%;" />

进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键后，稍等一段时间，就会打开一个相机窗口，识别成功后，机械臂就会开始抓取
```bash
python color_demo.py
```
<img src="./rdk_kit_img/rdk_color2.jpg" style="zoom: 30%;" />

### 物体分拣
将4个木块贴着物品的一面朝上放置到拍摄区，尽量放置在中间，避免机械臂限位

<img src="./rdk_kit_img/rdk_yolo.jpg" style="zoom: 30%;" />

进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键后，稍等一段时间，就会打开一个相机窗口，识别成功后，机械臂就会开始抓取
```bash
python yolo_demo.py
```
<img src="./rdk_kit_img/rdk_yolo2.jpg" style="zoom: 30%;" />

**注意**：如有线物品长时间识别不到，可用人手稍微旋转或移动一下木块

### aruco二维码码垛
将4个木块贴着aruco二维码的一面朝上放置到拍摄区，尽量放置在中间，避免机械臂限位

<img src="./rdk_kit_img/rdk_aruco.jpg" style="zoom: 30%;" />

进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键后，稍等一段时间，就会打开一个相机窗口，识别成功后，机械臂就会开始抓取
```bash
python aruco_demo.py
```
<img src="./rdk_kit_img/rdk_aruco2.jpg" style="zoom: 30%;" />

**注意**：若有一个木块没成功堆叠，需要先把程序结束掉，把4个木块放回拍摄区，重新运行程序，避免在码垛区发生碰撞

### OCR分拣
将4个木块贴着英文单词的一面朝上放置到OCR拍摄区，尽量放置在中间，避免机械臂限位

<img src="./rdk_kit_img/rdk_ocr.jpg" style="zoom: 30%;" />

先在终端输入下面指令，按下键盘回车键
```bash
export LD_PRELOAD=/home/sunrise/.local/lib/python3.10/site-packages/paddle/libs/libcommon.so
```

然后进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键后，稍等一段时间，就会打开一个相机窗口，识别成功后，机械臂就会开始抓取
```bash
python ocr_demo.py
```
<img src="./rdk_kit_img/rdk_ocr2.jpg" style="zoom: 50%;" />



### 垃圾检测
先将末端吸盘从机械臂末端拆下来，将连接主控的吸泵盒，进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键,机械臂各个关节会回到零位
```bash
python robot_test.py
```
然后夹爪按照下图进行连接

<img src="./rdk_kit_img/rdk7.jpg" style="zoom: 50%;" />

将夹爪线接到机械臂末端的3Pin接口上

<img src="./rdk_kit_img/rdk12.jpg" style="zoom: 50%;" />

打开一个终端输入命令，按下键盘回车键运行
```bash
export CAM_TYPE=usb
```
然后再输入下面命令，启动相机识别节点
```bash
ros2 launch dnn_node_example dnn_node_example.launch.py dnn_example_config_file:=config/ppyoloworkconfig.json dnn_example_msg_pub_topic_name:=ai_msg_mono2d_trash_detection dnn_example_image_width:=640 dnn_example_image_height:=480
```
在RDKX5主控上的浏览器输入http://192.168.127.10:8000 即可查看图像和算法渲染效果：

<img src="./rdk_kit_img/rdk_trash.jpg" width="60%">

然后进入mycobot280RDKX5_vision_kit文件夹,在终端输入下面指令,按下键盘回车键后，识别成功后，机械臂就会开始抓取
```bash
python garbage_demo.py
```



