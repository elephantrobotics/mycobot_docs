#表情使用

## myBuddy
myBuddy 自带的屏幕可以通过python接口来显示各种各样的表情。

### 使用方法：

1. 将[表情视频文件](https://github.com/elephantrobotics/pymycobot/blob/main/demo/mybuddy_demo/emoticon.zip)和[案例代码](https://github.com/elephantrobotics/pymycobot/blob/main/demo/mybuddy_demo/mybuddy_emoticon_demo.py)下载并且解压到mybuddy系统内

2. 更改案例文件代码,

将`/home/er/pymycobot/emo/face_video_3_2.mp4`替换成解压出来的视频文件路径
```python
from pymycobot import MyBuddyEmoticon
import time

# [video_path, Playback_duration(s)]
video1 = ["/home/er/pymycobot/emo/face_video_3_2.mp4", 10]

datas = [video1]

me = MyBuddyEmoticon(datas)
...
```
3. 执行mybuddy_emoticon_demo.py即可。


### API说明：

**MyBuddyEmoticon(file_path: list = [], window_size: tuple = (), loop=False)**
用于播放表情的API

* **参数**

    **file_path(list)**: `[[path, time]]`表情视频的绝对路径和播放时长。时间以秒为单位.
    **window_size(tuple)**: `(Length, width) `播放窗口的大小（默认为全屏）。.
    **loop(bool)**: 是否循环播放（默认为False，只播放一次）.

**file_path()**
* **功能：** 获取所要播放的表情视频路径
* **返回：**
  * 表情视频路径列表

**add_file_path(path_time)**
* **功能：** 增加要播放的表情视频
* **参数：**
    **path_time(list)**: `[path, time]` 需要添加的视频绝对路径及运行时间

**del_file_path(index)**
* **功能：** 删除表情视频列表中指定下标的元素
* **参数：**

    **index(int)**: 播放列表中要删除的元素的下标。

**pause()**
* **功能：** 暂停播放

**run()**
* **功能：** 继续播放

**start()**
* **功能：** 开始播放

**join()**
* **功能：** 等待播放完成后再退出程序
