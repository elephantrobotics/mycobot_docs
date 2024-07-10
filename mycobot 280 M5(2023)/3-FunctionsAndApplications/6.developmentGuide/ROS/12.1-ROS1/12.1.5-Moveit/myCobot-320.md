### 使用MoveIt

`mycobot_ros` 现已集成了 MoveIt 部分。

打开命令行运行：
- 2022 mycobot 320-M5版本：
  
```bash
roslaunch new_mycobot_320_moveit mycobot320_moveit.launch

# 如果末端装配自适应夹爪，则运行（仅支持M5版本）：
roslaunch new_mycobot_320_gripper_moveit mycobot320_gripper_moveit.launch
```

- 2022 mycobot 320-Pi版本：
  
```bash
roslaunch new_mycobot_320_pi_moveit mycobot320_moveit.launch
```


运行效果如下：  

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-9.jpg
width ="500"  align = "center">

如果末端装配自适应夹爪，运行效果如下：

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-5.png
width ="500"  align = "center">>


如果需要让真实的机械臂同步执行计划，需要再打开一个命令行，运行：
- 2022 mycobot 320-M5版本：
  
```bash
# 2022 mycobot 320-M5版本默认串口名为"/dev/ttyUSB0"，波特率为115200.部分机型的串口名为 "dev/ttyACM0",若默认串口名发生错误，可将串口名改为"/dev/ttyACM0".
rosrun new_mycobot_320_moveit sync_plan.py _port:=/dev/ttyUSB0 _baud:=115200

# 如果末端装配自适应夹爪，则运行（仅支持M5版本，串口修改同上）：
rosrun new_mycobot_320_gripper_moveit sync_plan.py _port:=/dev/ttyUSB0 _baud:=115200
```

- 2022 mycobot 320-Pi版本：
  
```bash
# 2022 mycobot 320-Pi版本默认串口名为"/dev/ttyAMA0"，波特率为115200.
rosrun new_mycobot_320_pi_moveit sync_plan.py _port:=/dev/ttyAMA0 _baud:=115200
```

**注意：** 如果末端装配自适应夹爪，需要对夹爪进行规划时，需要将规划组切换至夹爪的规划组。

<img src =../../../resourse/12-ApplicationBaseROS/12.1.4-6.jpg
width ="500"  align = "center">>

### 修改运动速度

为了防止真实机械臂在运动过程中，发生关节抖动现象，需要**降低**关节的运动速度。

- 在 `sync_plan.py` 文件中，修改机械臂Python API的速度参数，这里修改为25。
  
  ```python
  ...

  def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "%s", data)
    data_list = []
    for index, value in enumerate(data.position):
        radians_to_angles = round(math.degrees(value), 2)
        data_list.append(radians_to_angles)

    rospy.loginfo(rospy.get_caller_id() + "%s", data_list)
    mc.send_angles(data_list, 25)  # Change speed to 25

  ...

  ```

- 在 Moveit RViz 界面中，修改速度、加速度的缩放比，这里改为0.5，然后保存当前配置即可。

  <img src =../../../resourse/12-ApplicationBaseROS/12.1.4-19.png
width ="500"  align = "center">>