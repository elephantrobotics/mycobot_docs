## MoveIt

### Introduction to MoveIt

MoveIt is an integrated development platform in ROS, consisting of a variety of function packages for manipulating robotic arms, including: motion planning, manipulation, control, inverse kinematics, 3D perception, and collision detection.

The figure below shows the high-level structure of the main node **move_group** provided by Moveit. It is like a combiner: it integrates all individual components together and provides a series of actions and services for users to use.

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.5-Moveit/moveit-1.png
width ="500" align = "center">

### User Interface
Users can access the operations and services provided by move_group in three ways:

* In C++: Use the move_group_interface package to facilitate the practical use of move_group.
* In Python: Use the moveit_commander package.

* Via GUI: Use Rviz (ROS Visualizer) from Motion-commander.

move_group can be configured using the ROS parameter server, from which it can also get the robot's URDF and SRDF.

### Configuration
move_group is a ROS node. It uses the ROS parameter server to get three kinds of information:

1. URDF - move_group looks up the robot_description parameter on the ROS parameter server to get the robot's URDF.

2. SRDF - move_group looks up the robot_description_semantic parameter on the ROS parameter server to get the robot's SRDF. The SRDF is usually created by the user using the MoveIt Setup Assistant.

3. MoveIt Configuration - move_group will look up additional configuration specific to MoveIt on the ROS parameter server, including joint limits, kinematics, motion planning, perception, and other information. Configuration files for these components are automatically generated by the MoveIt setup assistant and stored in the configuration directory of the corresponding MoveIt configuration package for the robot.

## How to use MoveIt

>>**Note:** For better motion effects, the Atom firmware version of the end arm is 6.5, and the python driver library pymycobot version is 3.5.3

`mycobot_ros` now has MoveIt integrated.

Open the command line and run:

- mycobot 280-Arduino version:

```bash
roslaunch mycobot_280arduino_moveit mycobot_moveit.launch
```

The running effect is as follows:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.5-Moveit/moveit-2.png
width ="500" align = "center">

You can plan and execute, demonstration effect:

<img src =../../../../../resource\3-FunctionsAndApplications\6.developmentGuide\ROS\12.1-ROS1\12.1.5-Moveit/moveit-3.gif
width ="500" align = "center">

If you need to let the real robot arm execute the plan synchronously, you need to open another command line and run:

- mycobot 280-Arduino version:

```bash
# The default serial port name of mycobot 280-Arduino version is "/dev/ttyACM0" and the baud rate is 1000000.
rosrun mycobot_280arduino_moveit sync_play.py _port:=/dev/ttyACM0 _baud:=1000000
```