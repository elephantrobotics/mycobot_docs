# myCobot PRO 600 Moveit
`mycobot_ros` 现已集成了 MoveIt 部分。

使用之前需要确定机械臂的IP地址是否与程序文件中的保持一致，如果不一致，需修改程序文件中的IP地址，在程序文件：https://github.com/elephantrobotics/mycobot_ros/blob/noetic/mycobot_pro/mycobot_600_moveit/scripts/sync_plan.py 中的`listener`函数查看修改。

```bash

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from socket import *
import math
import sys
import time
from multiprocessing import Lock

import rospy
from sensor_msgs.msg import JointState

global mc
mutex = Lock()

# 此处省略部分代码......

old_list = []


def callback(data):
    """callback function,回调函数"""
    satrt_time=time.time()
    global old_list
    # rospy.loginfo(rospy.get_caller_id() + "%s", data.position)
    print ("position", data.position)
    data_list = []
    for index, value in enumerate(data.position):
        value = value * 180 / math.pi
        data_list.append(value)
    print ("data", data_list)

    if not old_list:
        old_list = data_list
        mc.write_angles(data_list, 1999)
    elif old_list != data_list:
        old_list = data_list
        # if mc.check_running():
            # mc.task_stop()
            # time.sleep(0.05)
            
        mc.write_angles(data_list, 1999)

        end_time=time.time()
        print('loop_time:',end_time-satrt_time)

def listener():
    global mc
    rospy.init_node("control_slider", anonymous=True)

    ip = rospy.get_param("~ip", "192.168.10.159")
    print (ip)
    mc = ElephantRobot(ip, 5001)
    # START CLIENT,启动客户端
    res = mc.start_client()
    if res != "":
        sys.exit(1)
        # print ep.wait(5)
    # print mc.get_angles()
    # print mc.get_coords()
    mc.set_speed(90)
    # print mc.get_speed()

    rospy.Subscriber("joint_states", JointState, callback)
    end_time=time.time()
    # spin() simply keeps python from exiting until this node is stopped
    # spin()只是阻止python退出，直到该节点停止
    print ("sping ...")
    rospy.spin()


if __name__ == "__main__":
    listener()

```

打开命令行运行：

```bash
roslaunch mycobot_600_moveit mycobot600_moveit.launch
```

运行效果如下：  

<img src =../../../resourse/12-ApplicationBaseROS/12.2.7-8.jpg
width ="500"  align = "center">

如果需要让真实的机械臂同步执行计划，需要再打开一个命令行，运行：

```bash
# mycobot pro 600 默认IP为"192.168.10.159"，端口号为5001.具体IP以实际机械臂连接的网络为准.
rosrun mycobot_600_moveit sync_plan.py
```