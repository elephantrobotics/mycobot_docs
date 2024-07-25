# API Description

API (Application Programming Interface), that is, application program interface functions, are some predefined functions. When using the following function interfaces, please import our API library at the beginning, that is, enter the code below, otherwise it will not run successfully:

```python
#Applicable to myCobot, mechArm series
from pymycobot.mycobot import MyCobot

#Applicable to myPalletizer series
from pymycobot.mypalletizer import MyPalletizer

#Applicable to myBuddy series
from pymycobot.mybuddy import MyBuddy

#Applicable to myArm
from pymycobot.myarm import MyArm
```

> **Note: **Some function interfaces have return values, but if you enter the code directly, the result returned is no return value. You need to use the `print` function to print out the result. For example, if you want to get the current speed value of the robot arm, you can use `get_speed()`, but directly entering the function will not result in any result. The correct way to write it is: `print(get_speed())` to print out the speed value. If the API description below states **no return value**, you do not need to use the `print` function. Otherwise, you need to use the `print` function to print the result.

## myCobot / myPalletizer / mechArm / myArm

### 1 Overall operation status of the robot

**1.1** `power_on()`

- **Function:** Power on the robot

- **Return value:** None

**1.2** `power_off()`

- **Function:** Power off the robot, all functions will be invalid

- **Return value:** None

**1.3** `is power on()`

* **Function**: Determine whether the robot is powered on

- **Return value:** 1- The robot is powered on 0 - The robot is powered off -1- Error

**1.4** `release_all_servos`

- **Function:** Set the robot to free movement mode (can swing the robot freely manually)

- **Return value:** None

**1.5** `is_controller_connected`

- **Function:** Determine whether it is connected to Atom

- **Return value:** 1- Connected 0 - Not connected -1- Error

**1.6** `read_next_error()`

- **Function:** Robotic arm error detection

- **Return value:** 0- No abnormality 1 - Communication interruption 2 - Communication unstable 3 - Servo abnormality

**1.7** `set_fresh_mode(mode)`

- **Function:**: Set interpolation/refresh motion mode

- **Parameter description:** mode: 0: Execute instructions in sequence 1: Execute the first instruction

- **Return value:** 1- Robotic arm is powered on 0 - Robotic arm is powered off -1- Error

**1.8** `get_fresh_mode()`

- **Function:**: Query interpolation/refresh motion mode

- **Return value:** 0: Execute instructions in sequence 1: Execute the first instruction

### 2 Robotic arm operation status and settings

**2.1** `pause()`

- **Function:** Let the robot pause the current movement
- **Return value:** None

**2.2** `stop()`

- **Function:** Let the robot stop all movements
- **Return value:** None

**2.3** `resume()`

- **Function:** Let the robot resume the previously set movement
- **Return value:** None

**2.4** `is_paused()`

- **Function:** Determine whether the robot is in a paused state
- **Return value:** 1 - Paused 0 - Not paused -1 - Error

**2.5** `get_speed()`

- **Function:** Get the robot's movement speed
- **Return value:** The robot's current set running speed, ranging from 1-100

**2.6** `set_speed(speed)`

- **Function:** Set the robot's movement speed
- **Parameter description:** speed: Enter the speed range you want to set in 1-100, in mm/s
- **Return value:** None

**2.7** `get_joint_min_angle(joint_id)`

- **Function:** Get the minimum angle that the specified joint can run to
- **Parameter description:** `joint_id`: (`int`) The joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** `angle`: The returned degree

**2.8** `get_joint_max_angle(joint_id)`

- **Function:** Get the maximum angle that the specified joint can run to
- **Parameter description:** `joint_id`: (`int`) The range of the robot arm joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** `angle`: (`float`) returned degrees

**2.9** `is_servo_enable(servo id)`

- **Function:** Determine whether the specified joint is connected
- **Parameter description:** servo id: The joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** (int) 1 - connected 0 - not connected -1 - error

**2.10** `is_all_servo_enable()`

- **Function:** Determine whether all joints of the robot are connected
- **Return value:** (int) 1 - connected 0 - not connected -1 - error

**2.11** `release_servo(servo_id)`

- **Function:** Release the specified joint
- **Parameter description:** servo id: (`int`) The specified joint of the robot arm, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** None

**2.12** `get_tof_distance()`

- **Function:** Get the detected distance (external distance detector is required)
- **Return value:** The detected distance value in mm.

**2.13** `get_error_information()`

- **Function:** Get error information

- **Return value:**
- 0: No error information.
- 1 ~ 6: The corresponding joint exceeds the limit.
- 16 ~ 19: Collision protection.
- 32: There is no solution for the inverse kinematics.
- 33 ~ 34: There is no adjacent solution for linear motion.

**2.14** `clear_error_information()`

- **Function:** Clear error information

**2.15** `set_joint_min(id, angle)`

- **Function:** Set the minimum angle that the specified joint can run to

- **Parameter description:**
- `id`: (`int`) The specified joint of the robot arm, ranging from 1 to 6
- `angle`: The minimum angle that the joint can run to

- **Return value:** None

**2.16** `set_joint_max(id, angle)`

- **Function:** Set the maximum angle that the specified joint can run to
- **Parameter Description:**
- `id`: (`int`) The specified joint of the robot arm, ranging from 1 to 6
- `angle`: The maximum angle that the joint can run
- **Return value:** None

**2.17** `get_basic_version()`

- **Function:** Get the firmware version
- **Return value:** Firmware version (`float`)

**2.18** `set_communicate_mode(mode)`

- **Function:** Set the basic communication mode
- **Parameter Description:** (`int`) 0 - Close 1- Open
- **Return value:** None

### 3 Enter program control mode (MDI mode)

> **Note:** The limit of different series of robot arms is different, and the settable posture values ​​are also different. For details, please refer to the parameter introduction of the corresponding model

**3.1** `get_angles()`

- **Function:** Get all joint angles
- **Return value:** `list` A list of floating point values ​​representing the angles of all joints

**3.2** `send_angle(id, degree, speed)`

- **Function:** Send the specified single joint movement to the specified angle
- **Parameter description:**
- `id`: Represents the joint of the robot arm. The six-axis has six joints and the four-axis has four joints. There is a specific representation method
Representation of joint 1: `Angle.J1.value`. (Can also be represented by numbers 1-6)
- `degree`: Indicates the angle of the joint
- `speed`: Indicates the speed of the robot arm, ranging from 0 to 100
- **Return value: ** None

**3.3** `send_angles(degrees, speed)`

- **Function: ** Send all angles to all joints of the robot arm
- **Parameter description: **
- `degrees`: (List[float]) Contains the angles of all joints. The six-axis robot has six joints, so the length is 6, and the four-axis length is 4. The representation method is: [20,20,20,20,20,20]
- `speed`: Indicates the speed of the robot arm, ranging from 0 to 100
- **Return value: ** None

**3.4** `get_coords()`

- **Function: ** Get the current coordinates and posture
- **Return value: ** `list` Contains a list of coordinates and postures
- Six-axis: The length is 6, in order of `[x, y, z, rx, ry, rz]`
- Four-axis: length is 6, in order `[x, y, z, rx]`

**3.5** `send_coord(id,coord,speed)`

- **Function:** Send a single coordinate value to the robot for movement
- **Parameter description:**
- `id`: represents the coordinate of the robot, six-axis has six coordinates, four-axis has four coordinates, there is a specific representation method
X coordinate representation: `Coord.X.value`, there is also a simple representation method: for example, X axis can be filled in 1, Y fill in 2, and so on
- `coord`: Enter the coordinate value you want to reach
- `speed`: Indicates the speed of the robot movement, the range is 0-100
- **Return value:** None

**3.6** `send_coords(coords, speed, mode)`

- **Function:** Send the overall coordinates and posture to move the robot head from the original point to the specified point
- **Parameter Description: **
- `coords`:
- Six-axis: [x,y,z,rx,ry,rz] coordinate value, length is 6
- Four-axis: [x,y,z,rx] coordinate value, length is 4
- `speed`: Indicates the speed of the robot movement, the range is 0-100
- `mode`: ( `int`): The value is limited to 0 and 1
- 0 means that the path of the robot head movement is nonlinear, that is, the route is randomly planned, as long as the robot head moves to the specified point while maintaining the specified posture.
- 1 means that the path of the robot head movement is linear, that is, the intelligent planning route allows the robot head to move to the specified point in a straight line.
- **Return value:** None

**3.7** `get_encoders()`

- **Function:** Get the potential values ​​of all joints of the robot

- **Return value:** `list` contains the list of potential values ​​of all joints of the robot

**3.8** `get_encoder(joint_id)`

- **Function# API Description

API (Application Programming Interface), that is, application program interface functions, are some predefined functions. When using the following function interfaces, please import our API library at the beginning, that is, enter the code below, otherwise it will not run successfully:

```python
#Applicable to myCobot, mechArm series
from pymycobot.mycobot import MyCobot

#Applicable to myPalletizer series
from pymycobot.mypalletizer import MyPalletizer

#Applicable to myBuddy series
from pymycobot.mybuddy import MyBuddy

#Applicable to myArm
from pymycobot.myarm import MyArm
```

> **Note: **Some function interfaces have return values, but if you enter the code directly, the result returned is no return value. You need to use the `print` function to print out the result. For example, if you want to get the current speed value of the robot arm, you can use `get_speed()`, but directly entering the function will not result in any result. The correct way to write it is: `print(get_speed())` to print out the speed value. If the API description below states **no return value**, you do not need to use the `print` function. Otherwise, you need to use the `print` function to print the result.

## myCobot / myPalletizer / mechArm / myArm

### 1 Overall operation status of the robot

**1.1** `power_on()`

- **Function:** Power on the robot

- **Return value:** None

**1.2** `power_off()`

- **Function:** Power off the robot, all functions will be invalid

- **Return value:** None

**1.3** `is power on()`

* **Function**: Determine whether the robot is powered on

- **Return value:** 1- The robot is powered on 0 - The robot is powered off -1- Error

**1.4** `release_all_servos`

- **Function:** Set the robot to free movement mode (can swing the robot freely manually)

- **Return value:** None

**1.5** `is_controller_connected`

- **Function:** Determine whether it is connected to Atom

- **Return value:** 1- Connected 0 - Not connected -1- Error

**1.6** `read_next_error()`

- **Function:** Robotic arm error detection

- **Return value:** 0- No abnormality 1 - Communication interruption 2 - Communication unstable 3 - Servo abnormality

**1.7** `set_fresh_mode(mode)`

- **Function:**: Set interpolation/refresh motion mode

- **Parameter description:** mode: 0: Execute instructions in sequence 1: Execute the first instruction

- **Return value:** 1- Robotic arm is powered on 0 - Robotic arm is powered off -1- Error

**1.8** `get_fresh_mode()`

- **Function:**: Query interpolation/refresh motion mode

- **Return value:** 0: Execute instructions in sequence 1: Execute the first instruction

### 2 Robotic arm operation status and settings

**2.1** `pause()`

- **Function:** Let the robot pause the current movement
- **Return value:** None

**2.2** `stop()`

- **Function:** Let the robot stop all movements
- **Return value:** None

**2.3** `resume()`

- **Function:** Let the robot resume the previously set movement
- **Return value:** None

**2.4** `is_paused()`

- **Function:** Determine whether the robot is in a paused state
- **Return value:** 1 - Paused 0 - Not paused -1 - Error

**2.5** `get_speed()`

- **Function:** Get the robot's movement speed
- **Return value:** The robot's current set running speed, ranging from 1-100

**2.6** `set_speed(speed)`

- **Function:** Set the robot's movement speed
- **Parameter description:** speed: Enter the speed range you want to set in 1-100, in mm/s
- **Return value:** None

**2.7** `get_joint_min_angle(joint_id)`

- **Function:** Get the minimum angle that the specified joint can run to
- **Parameter description:** `joint_id`: (`int`) The joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** `angle`: The returned degree

**2.8** `get_joint_max_angle(joint_id)`

- **Function:** Get the maximum angle that the specified joint can run to
- **Parameter description:** `joint_id`: (`int`) The range of the robot arm joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** `angle`: (`float`) returned degrees

**2.9** `is_servo_enable(servo id)`

- **Function:** Determine whether the specified joint is connected
- **Parameter description:** servo id: The joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** (int) 1 - connected 0 - not connected -1 - error

**2.10** `is_all_servo_enable()`

- **Function:** Determine whether all joints of the robot are connected
- **Return value:** (int) 1 - connected 0 - not connected -1 - error

**2.11** `release_servo(servo_id)`

- **Function:** Release the specified joint
- **Parameter description:** servo id: (`int`) The specified joint of the robot arm, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** None

**2.12** `get_tof_distance()`

- **Function:** Get the detected distance (external distance detector is required)
- **Return value:** The detected distance value in mm.

**2.13** `get_error_information()`

- **Function:** Get error information

- **Return value:**
- 0: No error information.
- 1 ~ 6: The corresponding joint exceeds the limit.
- 16 ~ 19: Collision protection.
- 32: There is no solution for the inverse kinematics.
- 33 ~ 34: There is no adjacent solution for linear motion.

**2.14** `clear_error_information()`

- **Function:** Clear error information

**2.15** `set_joint_min(id, angle)`

- **Function:** Set the minimum angle that the specified joint can run to

- **Parameter description:**
- `id`: (`int`) The specified joint of the robot arm, ranging from 1 to 6
- `angle`: The minimum angle that the joint can run to

- **Return value:** None

**2.16** `set_joint_max(id, angle)`

- **Function:** Set the maximum angle that the specified joint can run to
- **Parameter Description:**
- `id`: (`int`) The specified joint of the robot arm, ranging from 1 to 6
- `angle`: The maximum angle that the joint can run
- **Return value:** None

**2.17** `get_basic_version()`

- **Function:** Get the firmware version
- **Return value:** Firmware version (`float`)

**2.18** `set_communicate_mode(mode)`

- **Function:** Set the basic communication mode
- **Parameter Description:** (`int`) 0 - Close 1- Open
- **Return value:** None

### 3 Enter program control mode (MDI mode)

> **Note:** The limit of different series of robot arms is different, and the settable posture values ​​are also different. For details, please refer to the parameter introduction of the corresponding model

**3.1** `get_angles()`

- **Function:** Get all joint angles
- **Return value:** `list` A list of floating point values ​​representing the angles of all joints

**3.2** `send_angle(id, degree, speed)`

- **Function:** Send the specified single joint movement to the specified angle
- **Parameter description:**
- `id`: Represents the joint of the robot arm. The six-axis has six joints and the four-axis has four joints. There is a specific representation method
Representation of joint 1: `Angle.J1.value`. (Can also be represented by numbers 1-6)
- `degree`: Indicates the angle of the joint
- `speed`: Indicates the speed of the robot arm, ranging from 0 to 100
- **Return value: ** None

**3.3** `send_angles(degrees, speed)`

- **Function: ** Send all angles to all joints of the robot arm
- **Parameter description: **
- `degrees`: (List[float]) Contains the angles of all joints. The six-axis robot has six joints, so the length is 6, and the four-axis length is 4. The representation method is: [20,20,20,20,20,20]
- `speed`: Indicates the speed of the robot arm, ranging from 0 to 100
- **Return value: ** None

**3.4** `get_coords()`

- **Function: ** Get the current coordinates and posture
- **Return value: ** `list` Contains a list of coordinates and postures
- Six-axis: The length is 6, in order of `[x, y, z, rx, ry, rz]`
- Four-axis: length is 6, in order `[x, y, z, rx]`

**3.5** `send_coord(id,coord,speed)`

- **Function:** Send a single coordinate value to the robot for movement
- **Parameter description:**
- `id`: represents the coordinate of the robot, six-axis has six coordinates, four-axis has four coordinates, there is a specific representation method
X coordinate representation: `Coord.X.value`, there is also a simple representation method: for example, X axis can be filled in 1, Y fill in 2, and so on
- `coord`: Enter the coordinate value you want to reach
- `speed`: Indicates the speed of the robot movement, the range is 0-100
- **Return value:** None

**3.6** `send_coords(coords, speed, mode)`

- **Function:** Send the overall coordinates and posture to move the robot head from the original point to the specified point
- **Parameter Description: **
- `coords`:
- Six-axis: [x,y,z,rx,ry,rz] coordinate value, length is 6
- Four-axis: [x,y,z,rx] coordinate value, length is 4
- `speed`: Indicates the speed of the robot movement, the range is 0-100
- `mode`: ( `int`): The value is limited to 0 and 1
- 0 means that the path of the robot head movement is nonlinear, that is, the route is randomly planned, as long as the robot head moves to the specified point while maintaining the specified posture.
- 1 means that the path of the robot head movement is linear, that is, the intelligent planning route allows the robot head to move to the specified point in a straight line.
- **Return value:** None

**3.7** `get_encoders()`

- **Function:** Get the potential values ​​of all joints of the robot

- **Return value:** `list` contains the list of potential values ​​of all joints of the robot

**3.8** `get_encoder(joint_id)`

- **Function# API Description

API (Application Programming Interface), that is, application program interface functions, are some predefined functions. When using the following function interfaces, please import our API library at the beginning, that is, enter the code below, otherwise it will not run successfully:

```python
#Applicable to myCobot, mechArm series
from pymycobot.mycobot import MyCobot

#Applicable to myPalletizer series
from pymycobot.mypalletizer import MyPalletizer

#Applicable to myBuddy series
from pymycobot.mybuddy import MyBuddy

#Applicable to myArm
from pymycobot.myarm import MyArm
```

> **Note: **Some function interfaces have return values, but if you enter the code directly, the result returned is no return value. You need to use the `print` function to print out the result. For example, if you want to get the current speed value of the robot arm, you can use `get_speed()`, but directly entering the function will not result in any result. The correct way to write it is: `print(get_speed())` to print out the speed value. If the API description below states **no return value**, you do not need to use the `print` function. Otherwise, you need to use the `print` function to print the result.

## myCobot / myPalletizer / mechArm / myArm

### 1 Overall operation status of the robot

**1.1** `power_on()`

- **Function:** Power on the robot

- **Return value:** None

**1.2** `power_off()`

- **Function:** Power off the robot, all functions will be invalid

- **Return value:** None

**1.3** `is power on()`

* **Function**: Determine whether the robot is powered on

- **Return value:** 1- The robot is powered on 0 - The robot is powered off -1- Error

**1.4** `release_all_servos`

- **Function:** Set the robot to free movement mode (can swing the robot freely manually)

- **Return value:** None

**1.5** `is_controller_connected`

- **Function:** Determine whether it is connected to Atom

- **Return value:** 1- Connected 0 - Not connected -1- Error

**1.6** `read_next_error()`

- **Function:** Robotic arm error detection

- **Return value:** 0- No abnormality 1 - Communication interruption 2 - Communication unstable 3 - Servo abnormality

**1.7** `set_fresh_mode(mode)`

- **Function:**: Set interpolation/refresh motion mode

- **Parameter description:** mode: 0: Execute instructions in sequence 1: Execute the first instruction

- **Return value:** 1- Robotic arm is powered on 0 - Robotic arm is powered off -1- Error

**1.8** `get_fresh_mode()`

- **Function:**: Query interpolation/refresh motion mode

- **Return value:** 0: Execute instructions in sequence 1: Execute the first instruction

### 2 Robotic arm operation status and settings

**2.1** `pause()`

- **Function:** Let the robot pause the current movement
- **Return value:** None

**2.2** `stop()`

- **Function:** Let the robot stop all movements
- **Return value:** None

**2.3** `resume()`

- **Function:** Let the robot resume the previously set movement
- **Return value:** None

**2.4** `is_paused()`

- **Function:** Determine whether the robot is in a paused state
- **Return value:** 1 - Paused 0 - Not paused -1 - Error

**2.5** `get_speed()`

- **Function:** Get the robot's movement speed
- **Return value:** The robot's current set running speed, ranging from 1-100

**2.6** `set_speed(speed)`

- **Function:** Set the robot's movement speed
- **Parameter description:** speed: Enter the speed range you want to set in 1-100, in mm/s
- **Return value:** None

**2.7** `get_joint_min_angle(joint_id)`

- **Function:** Get the minimum angle that the specified joint can run to
- **Parameter description:** `joint_id`: (`int`) The joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** `angle`: The returned degree

**2.8** `get_joint_max_angle(joint_id)`

- **Function:** Get the maximum angle that the specified joint can run to
- **Parameter description:** `joint_id`: (`int`) The range of the robot arm joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** `angle`: (`float`) returned degrees

**2.9** `is_servo_enable(servo id)`

- **Function:** Determine whether the specified joint is connected
- **Parameter description:** servo id: The joint you specified, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** (int) 1 - connected 0 - not connected -1 - error

**2.10** `is_all_servo_enable()`

- **Function:** Determine whether all joints of the robot are connected
- **Return value:** (int) 1 - connected 0 - not connected -1 - error

**2.11** `release_servo(servo_id)`

- **Function:** Release the specified joint
- **Parameter description:** servo id: (`int`) The specified joint of the robot arm, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** None

**2.12** `get_tof_distance()`

- **Function:** Get the detected distance (external distance detector is required)
- **Return value:** The detected distance value in mm.

**2.13** `get_error_information()`

- **Function:** Get error information

- **Return value:**
- 0: No error information.
- 1 ~ 6: The corresponding joint exceeds the limit.
- 16 ~ 19: Collision protection.
- 32: There is no solution for the inverse kinematics.
- 33 ~ 34: There is no adjacent solution for linear motion.

**2.14** `clear_error_information()`

- **Function:** Clear error information

**2.15** `set_joint_min(id, angle)`

- **Function:** Set the minimum angle that the specified joint can run to

- **Parameter description:**
- `id`: (`int`) The specified joint of the robot arm, ranging from 1 to 6
- `angle`: The minimum angle that the joint can run to

- **Return value:** None

**2.16** `set_joint_max(id, angle)`

- **Function:** Set the maximum angle that the specified joint can run to
- **Parameter Description:**
- `id`: (`int`) The specified joint of the robot arm, ranging from 1 to 6
- `angle`: The maximum angle that the joint can run
- **Return value:** None

**2.17** `get_basic_version()`

- **Function:** Get the firmware version
- **Return value:** Firmware version (`float`)

**2.18** `set_communicate_mode(mode)`

- **Function:** Set the basic communication mode
- **Parameter Description:** (`int`) 0 - Close 1- Open
- **Return value:** None

### 3 Enter program control mode (MDI mode)

> **Note:** The limit of different series of robot arms is different, and the settable posture values ​​are also different. For details, please refer to the parameter introduction of the corresponding model

**3.1** `get_angles()`

- **Function:** Get all joint angles
- **Return value:** `list` A list of floating point values ​​representing the angles of all joints

**3.2** `send_angle(id, degree, speed)`

- **Function:** Send the specified single joint movement to the specified angle
- **Parameter description:**
- `id`: Represents the joint of the robot arm. The six-axis has six joints and the four-axis has four joints. There is a specific representation method
Representation of joint 1: `Angle.J1.value`. (Can also be represented by numbers 1-6)
- `degree`: Indicates the angle of the joint
- `speed`: Indicates the speed of the robot arm, ranging from 0 to 100
- **Return value: ** None

**3.3** `send_angles(degrees, speed)`

- **Function: ** Send all angles to all joints of the robot arm
- **Parameter description: **
- `degrees`: (List[float]) Contains the angles of all joints. The six-axis robot has six joints, so the length is 6, and the four-axis length is 4. The representation method is: [20,20,20,20,20,20]
- `speed`: Indicates the speed of the robot arm, ranging from 0 to 100
- **Return value: ** None

**3.4** `get_coords()`

- **Function: ** Get the current coordinates and posture
- **Return value: ** `list` Contains a list of coordinates and postures
- Six-axis: The length is 6, in order of `[x, y, z, rx, ry, rz]`
- Four-axis: length is 6, in order `[x, y, z, rx]`

**3.5** `send_coord(id,coord,speed)`

- **Function:** Send a single coordinate value to the robot for movement
- **Parameter description:**
- `id`: represents the coordinate of the robot, six-axis has six coordinates, four-axis has four coordinates, there is a specific representation method
X coordinate representation: `Coord.X.value`, there is also a simple representation method: for example, X axis can be filled in 1, Y fill in 2, and so on
- `coord`: Enter the coordinate value you want to reach
- `speed`: Indicates the speed of the robot movement, the range is 0-100
- **Return value:** None

**3.6** `send_coords(coords, speed, mode)`

- **Function:** Send the overall coordinates and posture to move the robot head from the original point to the specified point
- **Parameter Description: **
- `coords`:
- Six-axis: [x,y,z,rx,ry,rz] coordinate value, length is 6
- Four-axis: [x,y,z,rx] coordinate value, length is 4
- `speed`: Indicates the speed of the robot movement, the range is 0-100
- `mode`: ( `int`): The value is limited to 0 and 1
- 0 means that the path of the robot head movement is nonlinear, that is, the route is randomly planned, as long as the robot head moves to the specified point while maintaining the specified posture.
- 1 means that the path of the robot head movement is linear, that is, the intelligent planning route allows the robot head to move to the specified point in a straight line.
- **Return value:** None

**3.7** `get_encoders()`

- **Function:** Get the potential values ​​of all joints of the robot

- **Return value:** `list` contains the list of potential values ​​of all joints of the robot

**3.8** `get_encoder(joint_id)`

- **Function：** Get the potential value of a single joint specified by the robot
- **Parameter Description:**
- `joint_id`: Represents the joint of the robot. The six-axis robot has six joints, so the length is 6, and the four-axis length is 4. There is a specific representation method.
Joint one representation: `Angle.J1.value` (can also be represented by numbers 1-6)
- **Return value:** The potential value of the single joint you specified

**3.9** `set_encoder(joint_id, encoder)`

- **Function:** Send the specified single joint movement to the specified potential value
- **Parameter Description:**
- `joint_id`: Represents the joint of the robot. The six-axis robot has six joints, so the length is 6, and the four-axis length is 4. There is a specific representation method.
Joint one representation: `Angle.J1.value` (can also be represented by numbers 1-6)
- `encoder`: Represents the potential value of the robot, the value range is 0 ~ 4096
- **Return value:** None

**3.10** `set_encoders(encoders, sp)`

- **Function:** Send potential value to all joints of the robot

- **Parameter description:**
- `encoder`: Indicates the potential value of the robot, the value range is 0 ~ 4096, the length of the six-axis is 6, the length of the four-axis is 4, the representation method is: [2048,2048,2048,2048,2048,2048]
- `sp`: Indicates the speed of the robot movement, the value range is 0-100
- **Return value:** None

**3.11** `get_radians()`

- **Function:** Get the radian of all joints

- **Return value:** `list` contains a list of all joint radian values

**3.12** `send_radians(radians, speed)`

- **Function:** Send radian value to all joints of the robot
- **Parameter description:**
- `radians`: indicates the radian value of the robot arm
- **Return value:** None

**3.13** `sync_send_angles(degrees, speed, timeout=7)`

- **Function:** Synchronously send angles and return when reaching the target point
- **Parameter description:**
- `degrees`: list of angle values ​​of each joint ( `List[float]`)
- `speed`: ( `int`) speed of the robot arm movement, the value range is 0-100.
- `timeout`: default time is 7s
- **Return value: ** None

**3.14** `sync_send_coords(coords, speed, mode)`

- **Function: ** Synchronously send coordinates and return when reaching the target point
- **Parameter description: **
- `coords`: coordinate value list ( `List[float]`),
- Six-axis: length is 6, in order `[x, y, z, rx, ry, rz]`
- Four-axis: length is 6, in order `[x, y, z, rx]`
- `speed`: ( `int`) speed of the robot movement, the value range is 0-100
- **Return value: ** None

**3.15** `is_in_position(data, flag)`

- **Function: ** Determine whether the robot has reached the specified position
- **Parameter description: **
- `data`: The set of data you provide can be an angle or a coordinate value, such as: [10,20,20,10,20,10]
- `flag`: data type (value range 0 or 1)
- `0`: indicates that the value entered is an angle value
- `1`: indicates that the value entered is a coordinate value
- **Return value:** 1 - reached 0 - not reached -1 - error

**3.16** `is_moving()`

- **Function:** Determine whether the robot arm is moving
- **Return value:** 1 - moving 0 - not moving -1 - error

**3.17** `set_color(r, g, b)`

- **Function:** Set the light color on the top of the robot arm (LED light control)
- **Parameter description:** r, g, b indicate the light color value on the top of the robot
- `r`: 0 ~ 255
- `g`: 0 ~ 255
- `b`: 0 ~ 255
- **Return value: **None

**3.18** `set_encoders_drag(encoders, speeds)`

- **Function: **Send all potential values ​​and speeds
- **Parameter description: **
- `encoders`: Potential values ​​of all joints of the robot arm (list)
- `speed`: Speed ​​of all joints of the robot arm
- **Return value: **None

**3.19** `get_solution_angles()`

- **Function: **Get the deflection angle value (only for MyArm)
- **Return value: **None

**3.20** `set_solution_angles(angle, speed)`

- **Function: **Set the deflection angle value (only for MyArm)
- **Parameter description: **
- `angle`: Angle of the first joint
- `speed`: Speed ​​(0 - 100)
- **Return value: **None

**3.21** `set_solution_angles(angle, speed)`

- **Function:** Set the deflection angle value (only for MyArm)
- **Parameter description:**
- `angle`: Angle of the first joint
- `speed`: Speed ​​(0 - 100)
- **Return value:** None

**3.16** `set_solution_angles(angle, speed)`

- **Function:** Set the deflection angle value (only for MyArm)
- **Parameter description:**
- `angle`: Angle of the first joint
- `speed`: Speed ​​(0 - 100)
- **Return value:** None

**3.17** `get_transponder_mode()`

- **Function:** Get the configuration information of serial port transmission (only for MyArm)
- **Return value:** None
- `0`: Turn off transparent transmission
- `1`: Turn on transparent transmission and detect all data
- `2`: turn on transparent transmission, only detect the configuration information of the communication forwarding mode (default is 0)

**3.18** `set_transponder_mode(mode)`

- **Function:** Set the serial port transmission mode (only for MyArm)

- **Parameter description:**

- `0`: turn off transparent transmission

- `1`: turn on transparent transmission, detect all data

- `2`: turn on transparent transmission, only detect the configuration information of the communication forwarding mode

- **Return value:** None

### 4 JOG mode and operation

**4.1** `jog_angle(joint_id, direction, speed)`

- **Function:** Control the robot to move continuously at the specified angle

- **Parameter description:**

- `joint_id`: represents the joint of the robot arm, enter 1~6 according to the joint id

- `direction`: mainly controls the direction of movement of the robot arm, enter 0 for negative movement, enter 1 for positive movement

- `speed`: speed 0 ~ 100
- **Return value: **None

**4.2** `jog_coord(coord_id, direction, speed)`

- **Function: **Control the robot to move continuously according to the specified coordinate or posture value
- **Parameter description: **
- `coord_id`: Represents the joint of the robot arm, enter 1~6 according to the joint id
- `direction`: Mainly controls the direction of movement of the robot arm, enter 0 for negative movement, and enter 1 for positive movement
- `speed`: Speed ​​0 ~ 100
- **Return value: **None

**4.3** `jog_stop()`

- **Function: **Stop continuous movement under jog control
- **Return value: **None

**4.4** `jog_absolute(joint_id, angle, speed)`

- **Function: **Control a specific joint of the robot to move to a specified angle
- **Parameter description: **
- `joint_id`: represents the joint of the robot arm, enter 1~6 according to the joint id
- `angle`: specifies the angle of joint movement
- `speed`: speed 0 ~ 100
- **Return value: ** None

**4.5** `jog_increment(joint_id, angle, speed)`

- **Function: ** Step mode, make the movement angle run at a given increment
- **Parameter description: **
- `joint_id`: represents the joint of the robot arm, enter 1~6 according to the joint id
- `angle`: Increment range
- `speed`: speed 0 ~ 100
- **Return value: ** None

### 5 Servo control and operation

<!-- **5.1** `set_servo_data(servo_no, data_id, value)`

- **Function: ** Set the data parameters of the specified address of the servo
- **Parameter description: **
- `servo_no`: servo serial number, enter 1 - 6 according to joint id
- `data_id`: data address
- `value`: value range 0 - 4096
- **Return value:** None

**5.2** `get_servo_data(servo_no, data_id)`

- **Function:** Read the data parameters of the specified address of the servo.
- **Parameter description:**
- `servo_no`: the serial number of each servo, enter 1 - 6 according to the joint id
- `data_id`: data address
- **Return value:** data parameter value, range 0-4096 -->

**5.1** `set_servo_calibration(servo_no)`

- **Function:** Calibrate the specified joint, set the current position as the angle zero point, the corresponding potential value is 2048
- **Parameter description:** servo_no:(`int`): the specified joint of the robot arm, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value:** None

**5.2** `focus_servo(servo_id)`

- **Function:** Power on the specified joint
- **Parameter description:** servo id: (`int`): The specified joint of the robot arm, the range of mycobot series is 1~6, the range of mypalletizer series is 1-4, and the range of myArm series is 1-7
- **Return value: ** None

**5.3** `joint_brake(joint_id)`

- **Function: ** Stop the joint from moving, the buffer distance is positively correlated with the current speed
- **Parameter description: ** joint_id: (`int`): The specified joint of the robot arm, the range is 1~7
- **Return value: ** None

**5.4** `get_servo_speeds()`

- **Function: ** Get the joint running speed
- **Return value: ** (`list`) The running speed of each joint

**5.5** `get_servo_currents()`

- **Function: ** Get the current running speed of the joint
- **Return value: ** (`list`) The speed of each joint

**5.6** `get_servo_voltages()`

- **Function: ** Get joint voltage
- **Return value:** (`list`) Voltage of each joint

**5.7** `get_servo_status()`

- **Function:** Get joint status
- **Return value:** (`list`) Status of each joint

**5.8** `get_servo_temps()`

- **Function:** Get joint temperature
- **Return value:** (`list`) Temperature of each joint

### 6 Atom terminal IO control

**6.1** `set_pin_mode(pin_no, pin_mode)`

- **Function:** Set the status mode of the specified pin in atom
- **Parameter description:**

- `pin_no` (int): The specific pin number on the top of the robot
- `pin_mode` (int): Limited to 0~2
- 0 is set to the running state
- 1 is set to the stop state
- 2 is set to the pull-up mode
- **Return value: ** None

**6.2** `set_digital_output(pin_no, pin_signa)`

- **Function: ** Set the working state of the end pin number
- **Parameter description: **
- `pin_no`( `int`) The number marked at the end of the device only takes the digital part
- `pin_signal`( `int`): Input 0 means set to the running state, input 1 means stop state
- **Return value: ** None

**6.3** `get_digital_input(self, pin_no):`

- **Function: ** Get the working state of the end pin number
- **Parameter description: ** `pin_no`: Indicates the specific pin number at the end of the robot
- **Return value: ** `pin_signal`( `int`) When the returned value is 0, it means it is running in the working state, and 1 means it is stopped.

**6.4** `set_pwm_output(channel, frequency, pin_val):`

- **Function:** Pulse width modulation control
- **Parameter description:**
- `channel`(`int`): The specific pin number on the top of the robot
- `frequency`(`int`): Clock frequency
- `pin_val`(`int`): Duty cycle 0~256; 128 is 50%
- **Return value:** None

### 7 Gripper control

**7.1** `is_gripper_moving()`

- **Function:** Determine whether the gripper is running
- **Return value:**
- `0`: Indicates that the gripper of the robot arm is not running
- `1`: Indicates that the gripper of the robot arm is running
- `-1`: Indicates an error

**7.2** `set_gripper_value(value, speed, gripper_type=None)`

- **Function:** Let the gripper rotate to the specified position at the specified speed
- **Parameter description:**
- `value`: Indicates the position that the gripper is going to reach, with a value range of 0~100
- `speed`: Indicates the speed at which the gripper rotates, with a value range of 0~100
- `gripper_type`: Gripper type, the default is adaptive gripper
- `1`: Adaptive gripper
- `3`: Parallel gripper
- `4`: Flexible gripper
- **Return value:** None

**7.3** `get_gripper_value(gripper_type=None)`

- **Function:** Get the current position data information of the gripper
- **Parameter description:**
- `gripper_type`: Gripper type, the default is adaptive gripper
- `1`: Adaptive gripper
- `3`: Parallel gripper
- `4`: Flexible gripper
- **Return value:** Gripper data information

**7.4** `set_gripper_state(flag, speed， _type=None)`

- **Function:** Let the gripper enter the specified state at the specified speed
- **Parameter description:**
- `flag`: 1 indicates the gripper is closed, 0 indicates the gripper is open.
- `speed`: indicates how fast to reach the specified state, the value range is 0~100
- `_type`: Gripper type, the default is adaptive gripper
- `1`: Adaptive gripper
- `2`: Five-finger dexterous hand
- `3`: Parallel gripper
- `4`: Flexible gripper
- **Return value: ** None

**7.5** `move_round()`

- **Function:** Drive the four-piece chess servo to rotate counterclockwise, and it takes 1.5s to complete a circle

**7.6** `set_eletric_gripper(status)`

- **Function:** Set the gripper mode (only works on 350)
- **Parameter description:** `status`: 1 indicates the gripper is closed, 0 indicates the gripper is open.
- **Return value: **None

**7.7** `set_gripper_mode(status)`

- **Function: **Set gripper mode

- **Parameter description: ** `status`: 1 transparent mode, 0 I/O mode

- **Return value: **None

**7.8** `get_gripper_mode()`

- **Function: **Get gripper status

- **Return value: ** `status(int)`: 0 - transparent mode 1 - I/O mode

**7.9** `set_HTS_gripper_torque(torque)`

- **Function: **Set adaptive gripper torque

- **Parameter description: **
- `torque`: 150 ~ 900

- **Return value: **0 - Setting failed; 1 - Setting successful

**7.10** `get_HTS_gripper_torque()`

- **Function: **Get adaptive gripper torque

- **Return value: ** 150 ~ 900

**7.11** `get_gripper_protect_current()`

- **Function:** Get the gripper protection current

- **Return value:** 1 ~ 500

**7.12** `init_gripper()`

- **Function:** Initialize the gripper

- **Return value:** 0 - Initialization failed; 1 - Initialization successful

**7.13** `set_gripper_protect_current(current)`

- **Function:** Set the gripper protection current

- **Parameter description:**
- `current`: 1 ~ 500
- **Return value:** 0 - Initialization failed; 1 - Initialization successful

### 8 Base BasicIO control

**8.1** `get_basic_input(pin_no)`

- **Function:** Get the working status of the bottom pin number
- **Parameter description:** `pin_no`: Indicates the specific pin number at the bottom of the robot.
- **Return value:** `pin_signal`(`int`) When the returned value is 0, it means it is running in working state, and 1 means it is stopped.

**8.2** `set_basic_output(pin_no, pin_signal)`

- **Function:** Set the working state of the bottom pin number.
- **Parameter description:**
- `pin_no`( `int`) The number marked on the bottom of the device is only the digital part
- `pin_signal`( `int`): Enter 0 to set it to running state, enter 1 to stop state
- **Return value:** None

### 9 socket communication

> The robot arm needs to open the server, the server file is [here](https://github.com/elephantrobotics/pymycobot/blob/main/demo/Server.py).

```python
# for mycobot,mecharm
from pymycobot import MyCobotSocket

mc = MyCobotSocket("192.168.1.10", 9000)

print(mc.get_angles())

```

### 10 TCPIP

**10.1** `set_ssid_pwd(account, password)`

- **Function:** Change the connected wifi (applicable to m5 or seed)
- **Parameter description:**
- `account`( `str`): new wifi account
- `password`( `str`): new wifi password
- **Return value:** None

**10.2** `get_ssid_pwd()`

- **Function:** Get the connected wifi account and password (applicable to m5 or seed)
- **Return value:** The currently connected wifi account and password

**10.3** `set_server_port(port)`

- **Function:** Change the server connection port
- **Parameter description:**
- `port`( `int`) The new connection port of the server
- **Return value:** None

### 11 utils (module)

This module supports some helper methods. Use the code entered at the beginning of the file to import the module:

```python
from pymycobot import utils
```

**11.1** `utils.get_port_list()`

- **Function:** Get the current list of all serial port numbers

- **Return value:** Serial port list (`list`)

**11.2** `utils.detect_port_of_basic()`

- **Function:** Return the first detected serial port number of M5 Basic. (Only one serial port number will be returned)

- **Return value:** Return the detected port number, if no serial port number is detected, return: `None`

### 12 Raspberry Pi - GPIO

When your robot arm is the Raspberry Pi version, you can use the following API. At the same time, before using the API, you need to enter the code import at the beginning of the file:

```python
from pymycobot import MyCobot
```

**12.1** `gpio_init()`

- **Function:** Initialize the GPIO module and set the BCM mode
- **Return value:** None

**12.2** `set_gpio_mode`

- **Function:** Set the Raspberry Pi GPIO pin mode
- **Parameter**
- `mode` (`str`) Input: "BCM" or "BOARD" to enter the corresponding mode

**12.3** `set_gpio_output(pin_no, state)`

- **Function:** Set the pin to high or low level
- **Parameter description:**
- `pin`( `int`) Pin number
- `state`: 0 is set to low level 1 is set to high level
- **Return value:** None

**12.4** `get_gpio_in(pin_no)`

- **Function:** Get the pin level status
- **Parameter description:**
- `pin_no`( `int`) Pin number
- **Return value:** 0 is low level 1 is high level

**12.5** `gpio_output(pin,v)`

- **Function:** Set GPIO output value
- **Parameter description:**
- `pin_no`( `int`) Pin number
- `v`(`int`): 0 is set to low level 1 is set to high level
- **Return value:** None

**12.6** `set_gpio_out(pin_no, mode)`

- **Function:** Set the pin as input or output
- **Parameter description:**
- `pin`( `int`) Pin number
- `mode`(`str`): in - input; out - output
- **Return value:** None

### 13 Coordinate transformation

**13.1** `get_tool_reference()`

- **Function:** Get tool coordinate system
- **Return value:** (`list`)[x, y, z, rx, ry, rz]

**13.2** `set_tool_reference(coords)`

- **Function:** Set tool coordinate system
- **Parameter description:** (`list`)[x, y, z, rx, ry, rz]
- **Return value:** None

**13.3** `set_world_reference(coords)`

- **Function:** Set world coordinate system
- **Parameter description:** (`list`)[x, y, z, rx, ry, rz]
- **Return value:** None

**13.4** `get_world_reference()`

- **Function:** Get world coordinate system
- **Return value:** (`list`)[x, y, z, rx, ry, rz]

**13.5** `set_reference_frame(rftype)`

- **Function:** Set the base coordinate system
- **Return value:** `rftype`: 0 - Base coordinates (default) 1 - World coordinates

**13.6** `get_reference_frame()`

- **Function:** Get the base coordinate system
- **Return value:** (`list`)[x, y, z, rx, ry, rz]

**13.7** `set_movement_type(move_type)`

- **Function:** Set the movement type
- **Parameter:** `move_type`: 0 - movj 1 - movI
- **Return value:** None

**13.8** `get_movement_type()`

- **Function:** Get the movement type
- **Return value:** 0 - movj 1 - movI

**13.9** `set_end_type(end)`

- **Function:** Set the end coordinate system
- **Parameter:** `end`: 0 - flange (default) 1 - tool
- **Return value:** None

**13.10** `get_end_type()`

- **Function:** Get the end coordinate system
- **Return value:** 0 - flange (default) 1 - tool

### 14 Speed ​​planning

**14.1** `get_plan_speed()`

- **Function:** Get the planned speed
- **Return value:** Moving speed (`list`)

**14.2** `get_plan_acceleration()`

- **Function:** Get the planned acceleration
- **Return value:** Acceleration (`list`)

## myBuddy
### 1 Overall operation status of the robot

**1.1** ` power_off(id=0)`

- **Function:** Turn off the power of the robot

- **Parameter:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

**1.2** ` power_on(id=0)`

- **Function:** Turn on the power of the robot

- **Parameter**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

**1.3** ` read_next_error(id=0)`

- **Function:** Robot error detection

- **Parameter**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

**1.4** ` release_all_servos(id=0)`

- **Function:** Release the servos

- **Parameter**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

**1.5** ` is_power_on(id=0)`

- **Function:** Query the control core connection status

- **Parameter**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **Return**

1 - Power on
0 - Power off
-1 - Error data

**1.6** ` is_controller_connected(id=0)`

- **Function:** Whether connected to Atom.

- **parameter**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **return**

0 - disconnect
1 - connect

**1.7** ` set_free_mode(id, value)`

- **Function:** Set free mode

- **parameter**

- **id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **value** - 0 - off 1 - on

**1.8** ` set_fresh_mode(id, mode)`

- **Function:** Set command refresh mode

- **parameter**

- **id** – 1/2 (left/right).

- **mode** - int
1 - always execute the latest command first.
0 - execute commands sequentially in a queue.

**1.9** `release_servo(id, servo_id)`
- **Function:** Release the specified single servo

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist)

- **servo_id** – 1 - 6.

**1.10** `is_free_mode(id)`

- **Function:** Check if it is in free mode

- **Parameter**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **Return**

0 - No
1 - Yes

### 2 Robot arm operation status and settings

**2.1** `stop(id)`

- **Function:** Stop moving

- **Parameter:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist).

**2.2** ` resume(id)`

- **Function:** Resume motion

- **Parameter:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist).

**2.3** ` is_paused(id)`

- **Function:** Determine if the robot is paused.

- **Parameter:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist).

- **Return**

1 - Pause
0 - Not paused
-1 - Error

**2.4** ` get_speed(id)`

- **Function:** Get speed

- **Parameter:**

**id** – 1/2/3 (left arm/right arm/waist).

- **Return**

Speed

- **Return type**

Integer

**2.5** ` set_speed(id, speed)`

- **Function:** Set speed value

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **speed** (_int_) - 0 - 100

**2.6** ` get_joint_min_angle(id, joint_id)`

- **Function:** Get the minimum moving angle of the specified joint

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **joint_id** - (int) 1 - 6

- **Return**

Angle value (floating point number)

**2.7** ` is_servo_enable(id, servo_id)`

- **Function:** Determine whether all servos are connected

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **servo_id** – (int) 1 ~ 6

- **Return**

0 – Not connected
1 – Connected
-1 – Error

**2.8** ` is_all_servo_enable(id)`

- **Function:** Determine if the specified servo is connected

- **Parameters:**

**id** – 1/2/3 (left arm/right arm/waist)

- **Return**

0 – Disable
1 – Enable
-1 – Error

**2.9** ` set_joint_min(id, joint_id, angle)`

- **Function:** Set the minimum angle of the joint

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **joint_id** – integer 1-6.

- **angle** - 0 ~ 180

**2.10** ` get_robot_version(id)`

- **Function:** Get robot version

- **Parameter:**

**id** - 0/1/2/3 (ALL/left arm/right arm/waist)

**2.11** ` get_system_version(id)`

- **Function:** Get software version

- **Parameter:**

**id** - 0/1/2/3 (ALL/left arm/right arm/waist)

**2.12** ` get_joint_max_angle(id, joint_id`

- **Function:** Get the maximum movement angle of the specified joint

- **Parameter**

- **id** - 1/2/3 (left arm/right arm/waist)

- **joint_id** - (int) 1 - 6

- **Return**

Angle value (floating point number)

**2.13** ` set_robot_id(id, new_id)`

- **Function:** Set this robot ID

- **Parameter**

- **id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **new_id** - 1 - 253

**2.14** ` joint_brake(id, joint_id)`

- **Function:** Stop the joint when it moves, and the buffer distance is positively correlated with the current speed

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist)

- **joint_id** - 1 - 6

**2.15** ` get_robot_id(id)

- **Function:** Detect this robot ID

- **Parameter:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

### Enter program control mode (MDI mode)

**3.1** ` get_angles(id)`

- **Function:** Get the degrees of all joints.

- **Parameter**

**id** – 1/2 (left/right)

- **Return**

List of length 6.

- **Return type**

List

**3.2** ` send_angle(id, joint, angle, speed)`

- **Function:** Send a single joint angle to the robot.

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist)

- **joint** – 1 ~ 6

- **angle** - Angle value

- **speed** – 1 ~ 100

- **Return**

- None

**3.3** ` send_angles(id, degrees, speed)`

- **Function:** Send all angles to the specified robot

- **Parameter**

- **id** – 1/2 (left/right).

- **degrees** – [angle_list] len 6

- **speed** – 1 - 100

**3.4** ` set_joint_max(id, joint_id, angle)`

- **Function:** Set the maximum angle of the joint

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist)

- **joint_id** – integer 1-6.

- **angle** – 0 ~ 180

**3.5** ` send_coord(id, coord, data, speed)`

- **Function:** Send a single coordinate to the robot

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist).

- **coord** – 1 ~ 6 (x/y/z/rx/ry/rz)

- **data** – Coordinate value

- **speed** – 0 ~ 100

**3.6** ` send_coords(id, coords, speed, mode)`

- **Function:** Send all coordinates to the robot.

- **Parameter**

- **id** – 1/2 (left/right).

- **coords** – Coordinate value list (List[float]), length6, [x(mm), y, z, rx(angle), ry, rz]

- **speed** - (int) 1 ~ 100

- **mode** - (int) 0 - moveJ, 1 - moveL, 2 - moveC

**3.7** ` get_coord(id, joint_id)`

- **Function:** Read a single coordinate parameter

- **Parameter**

- **id** (_int_) – 1/2/3 (left arm/right arm/waist).

- **joint_id** (_int_) – 1 - 7 (7 is the gripper)

**3.8** ` get_encoder(id,joint_id)`

- **Function:** Get the specified joint potential value.

- **Parameter**

- **id** - 1/2/3 (left arm/right arm/waist).

- **joint_id** - (int) 1 ~ 6

- **Return**

0 ~ 4096

**3.9** ` get_encoders(id)`

- **Function:** Get the six joint potential values ​​of the specified robot

- **Parameter**

**id** – 1/2(left/right).

- **Return**

List

**3.10** ` get_radians(id)`

- **Function:** Get the radians of all joints

- **Parameter**

**id** – 1/2(left/right)

- **Return**

List of floating radians [radian1, ...]

- **Return type**

List

**3.11** ` send_radians(id, radians, speed)`

- **Function:** Send the radians of all joints to the robot

- **Parameter**

- **id** – 1/2(left/right).

- **radians** – List of radian values ​​(List[float]), length 6

- **speed** – (int)0 ~ 100

**3.12** ` is_in_position(id, data, mode)`

- **Function:** Determine if the position has been reached.

- **Parameter**

- **id** – 0/1/2/3 (ALL/left arm/right arm/waist).

- **data** – Data list, angle or coordinate. If id is 1/2. Data length is 6. If id is 0. data len 13 (data==[ [left_angles / left_coords],[right_angles / right_coords],[waist_angle /waist_coord]]). If id is 3. data len 1

- **mode** - 1 - coordinates, 0 - angles

- **return**

1 - reached
0 - not reached
-1 - error

**3.13** ` is_moving(id)`

- **Function:** Check if the robot is moving

- **Parameter**

**id** - 0/1/2/3 (ALL/left arm/right arm/waist).

- **return**

0 - not moving
1 - moving
-1 - wrong data

**3.14** ` set_color(id, r=0, g=0, b=0)`

- **Function:** Set the light color of the Atom at the top of the robot arm.

- **Parameter**

- **id** - 1/2 (left/right)

- **r** (_int_) – 0 ~ 255

- **g** (_int_) – 0 ~ 255

- **b** (_int_) – 0 ~ 255

**3.15** ` set_encoder(id, joint_id, encoder, speed)`

- **Function:** Send the encoder value of a single joint

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist).

- **joint_id** - 1 - 6.

- **encoder** – Set the encoder value.

**3.16** ` set_encoders(id, encoder, speed)`

- **Function:** Set the six joints of the specified robot to execute synchronously to the specified encoder position.

- **Parameter**

- **id** – 1/2 (left/right).

- **encoders** – Encoder list, length 6.

- **speed** – Speed ​​1 ~ 100

**3.17** ` get_angle(id, joint_id)`

- **Function:** Get the angle of a single joint

- **Parameter**

- **id** (_int_) – 1/2/3 (left arm/right arm/waist).

- **joint_id** (_int_) – 1 - 7 (7 is the gripper)

**3.18** ` set_servo_calibration(id, servo_no)`

- **Function:** Set the current position of the joint to the angle zero point,

The corresponding encoder is 2048.

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **servo_no** – Servo serial number, 1 - 6.

**3.19** ` set_joint_current(id, joint_id, current)`

- **Function:** Set the collision current

- **Parameters:**

- **id** - 0/1/2 (ALL/L/R)

- **joint_id** - 1 - 6

- **current** – Current value

**3.19** ` set_encoders_drag(id, encoders, speeds)`

- **Function:** Set the end coordinate system

- **Parameters:**

- **id** - 0/1/2 (ALL/L/R)

- **encoders** - `list` Potential value of each joint

- **speed** - Get through `get_servo_speeds()`

**3.20** ` get_coords(id)`

- **Function:** Get the robot arm coordinates

- **Parameters**

**id** – 1/2 (left/right).

### 4 JOG mode and operation

**4.1** `jog_absolute(id, joint_id, angle, speed)`

- **Function:** Absolute joint control

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist).

- **joint_id** – integer 1-6.

- **angle** – int

- **speed** – int (0 - 100)

**4.2** `jog_angle(id, joint_id, direction, speed)`

- **Function:** Joint control.

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist).

- **joint_id** – integer 1-6.

- **direction** - 0 - decrease, 1 - increase

- **speed** - int (0 - 100)

**4.3** ` jog_coord(id, coord_id, direction, speed)`

- **Function:** Coordinate control.

- **Parameters:**

- **id** - 1/2/3 (left arm/right arm/waist).

- **coord_id** - int 1-6 (x/y/z/rx/ry/rz).

- **direction** - 0 - decrease, 1 - increase

- **speed** - int (0 - 100)

**4.4** ` jog_inc_coord(axis, increment, speed)`

- **Function:** Dual-arm coordinated coordinate stepping

- **Parameters:**

- **axis** - 1 - 6 (x/y/z/rx/ry/rz)

- **increment** -

- **speed** - 1 - 100

**4.5** ` jog_increment(id, joint_id, increment, speed)`

- **Function:** Stepping mode

- **Parameters:**

- **id** - 1/2/3 (left arm/right arm/waist).

- **joint_id** - integer 1-6.

- **increment** -

- **speed** - int (1 - 100)

**4.6** ` jog_stop(id)`

- **Function:** JOG stop

- **Parameter:**

**id** – 1/2/3 (left arm/right arm/waist).

### 5 Servo control and operation

**5.1** ` focus_servo(id, servo_id)`

- **Function:** Power on the specified servo

- **Parameter:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **servo_id** - 1 - 6

**5.2** ` get_servo_currents(id)`

- **Function:** Get joint current

- **Parameter:**

**id** – 1/2/3 (left arm/right arm/waist)

- **Return**

Value in milliampere units

<!-- **5.3** ` get_serv**5.1o_data(id, servo_no, data_id)`

- **Function:** Read the data parameters of the specified address of the servo.

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **servo_no** – servo serial number, 1 - 6.

- **data_id** – data address.

- **Return**

Value (0 - 4096)

0 - Disable

1 - Enable

-1 - Error -->

**5.3** ` get_servo_status(id)`

- **Function:** Get joint status

- **Parameter:**

**id** – 1/2/3 (left arm/right arm/waist)

- **Return**

[voltage, sensor, temperature, current, angle, overload], value 0 means no error

**5.4** ` get_servo_temps(id)`

- **Function:** Get joint temperature

- **Parameter:**

**id** – 1/2/3 (left arm/right arm/waist)

**5.5** ` get_servo_voltages(id)`

- **Function:** Get joint voltage

- **Parameter:**

**id** – 1/2/3 (left arm/right arm/waist)

- **Return**

Voltage value < 24 V

<!-- **5.7** ` set_servo_data(id, servo_no, data_id, value)`

- **Function:** Set the data parameters of the specified address of the servo

- **Parameter**

- **id** – 1/2/3 (left arm/right arm/waist)

- **servo_no** – Servo serial number, 1 - 6.

- **data_id** – Data address.

- **value** - 0 - 4096 -->

### 6 Atom terminal IO control

**6.1** ` set_pin_mode(id, pin_no, pin_mode)`

- **Function:** Set the state mode of the specified pin in the atom.

- **Parameter:**

- **id** - 1/2 (left/right)

- **pin_no** (_int_) –Pin number (1 - 5).

- **pin_mode** (_int_) - 0 - input, 1 - output

**6.2** ` set_digital_output(id, pin_no, pin_signal)`

- **Function:** Set atom IO output level

- **Parameter:**

- **id** - 1/2(left/right)

- **pin_no** (_int_) - 1 - 5

- **pin_signal** (_int_) – 0 / 1

**6.3** ` get_digital_input(id, pin_no)`

- **Function:** Read Atom IO input level

- **Parameter:**

- **id** - 1/2(left/right)

- **pin_no** (_int_) - 1 - 5

**6.4** ` set_pwm_output(id, channel, frequency, **6.1pin_val)`

- **Function:** PWM control

- **Parameters:**

- **id** - 1/2 (left/right)

- **channel** (_int_) – IO number (1 - 5).

- **frequency** (_int_) – Clock frequency (0/1: 0 - 1Mh**6.1z 1 - 10Mhz`)

- **pin_val** (_int_) – Duty cycle 0 ~ 100: 0 ~ 100%

### 7 Gripper control

**7.1** ` get_gripper_value(id)`

- **Function:** Get the value of the gripper.

- **Parameter**

**id** – 1/2(left/right)

- **Return**

Gripper value (int)

**7.2** ` is_gripper_moving(id)`

- **Function:** Determine if the gripper is moving

- **Parameter**

**id** – 1/2(left/right)

- **Return**

0 - Not moving
1 - Moving
-1 - Wrong data

**7.3** ` set_gripper_state(id, flag)`

- **Function:** Set the gripper switch state

- **Parameter**

- **id** - 1/2(left/right)

- **flag** (_int_) - 0 - Close, 1 - Open

**7.4** ` set_gripper_value(id, value, speed)`

- **Function:** Set the gripper value

* **Parameter**

* **id** – 1/2 (L/R)

* **value** (_int_) – 0 ~ 100

* **speed** (_int_) – 0 ~ 100

### 8 socket communication

```python
from pymycobot import MyBuddySocket

mst = MyBuddySocket("192.168.0.1", 9000)

mst.connect("/dev/ttyACM0", "115200")

print(mst.get_angles(1))
```

### 9 Raspberry Pi - GPIO

**9.1** ` Get_gpio_input(pin)`

- **Function:** Get GPIO input value.

- **Parameter**

**pin** - (int) pin number.

**9.2** ` set_gpio_input(pin)`

- **Function:** Set GPIO input value.

- **Parameter**

**pin** - (int)pin number.

**9.3** ` set_gpio_mode(pin_no, mode)`

- **Function:** Initialize GPIO module, set BCM mode.

- **Parameter**

- **pin_no** - (int)pin number.

- **mode** - 0 - input 1 - output

**9.4** ` set_gpio_output(pin, v)`

- **Function:** Set GPIO output value.

- **Parameter**

- **pin** - (int)pin number.

- **v** - (int) 0 / 1

**9.5** ` set_gpio_pwm(pin, baud, dc)`

- **Function:** Set GPIO PWM value.

- **Parameter**

- **pin** - (int)pin number.

- **baud** - (int) 10 - 1000000

- **dc** - (int) 0 - 100

### 10 Coordinate transformation

**10.1** ` set_tool_reference(id, coords)`

- **Function:** Set tool coordinate system

- **Parameter**

- **id** - 0/1/2 (ALL/L/R)

- **coords** – List of coordinate values ​​(List[float]), length 6. [x(mm), y, z, rx(angle), ry, rz]

**10.2** ` set_world_reference(id, coords)`

- **Function:** Set the world coordinate system

- **Parameter**

- **id** - 0/1/2 (ALL/L/R)

- **coords** – List of coordinate values ​​(List[float]), length 6 [x(mm), y, z, rx(angle), ry, rz]

**10.3** ` get_reference_frame(id)`

- **Function:** Get the base coordinate system

- **Parameter**

**id** – 0/1/2 (ALL/L/R)

- **Return**

0 - Base 1 - Tool.

**10.4** ` get_tool_reference(id)`

- **Function:** Get tool coordinate system

- **Parameter**

**id** – 0/1/2 (ALL/L/R)

**10.5** ` get_world_reference(id)`

- **Function:** Get world coordinate system

- **Parameter**

**id** – 0/1/2 (ALL/L/R)

**10.6** ` set_reference_frame(id, rftype)`

- **Function:** Set base coordinate system

- **Parameter**

- **id** - 0/1/2 (ALL/L/R)

- **rftype** - 0 - base 1 - tool.

**10.7** ` set_movement_type(id, move_type)`

- **Function:** Set the movement type

- **Parameter**

- **id** - 0/1/2 (ALL/L/R)

- **move_type** - 1 - movel, 0 - moveJ

**10.8** ` get_movement_type(id)`

- **Function:** Get the movement type

- **Parameter**

**id** – 0/1/2 (ALL/L/R)

- **Return**

1 - Move L
0 - Move J

**10.9** ` set_end_type(id, end)`

- **Function:** Set the end coordinate system

- **Parameter**

- **id** - 0/1/2 (ALL/L/R)

- **end** - 0 - Flange, 1 - Tool

**10.10** ` get_end_type(id)`

- **Function:** Get the end coordinate system

- **Parameter**

**id** – 0/1/2 (ALL/L/R)

- **Return**

0 - Flange
1 - Tool

**10.11** ` write_base_coords(id, coords, speed)`

- **Function:** Base coordinate movement

- **Parameter**

- **id** - 1/2 (left/right)

- **coords** - coords: coordinate value list (List[float]), length 6, [x(mm), y, z, rx(angle), ry, rz]

- **speed** - 1 - 100

**10.12** ` write_base_coord(id，axis, coord, speed)`

- **Function:** Base single coordinate movement

- **Parameter**

- **id** - 1/2 (left/right)

- **axis** – 1 - 6 (x/y/z/rx/ry/rz)

- **coord** - coordinate value

- **speed** - 1 - 100

**10.13** ` base_to_single_coords(base_coords, arm)`

- **Function:** Convert base coordinates to coordinates

- **Parameters:**

- **coords** – list of base coordinate values ​​len 6

- **arm** - 0 - left. 1 - Right

- **Return:**

Coordinates

**10.14** ` get_base_coord(id)`

- **Function:** Get the base coordinates of a single arm

- **Parameters:**

**id** – 1/2(left/right)

**10.15** ` (\*args)get_base_coords`

- **Function:** Convert coordinates to base coordinates. You can pass in parameters or not. When passing in parameters, the conversion is based on the parameters; when there are no parameters, the conversion is based on the current coordinates.

- **Parameters:**

- **coords** – List of coordinate values ​​(List[float]), length 6 [x(mm), y, z, rx(angle), ry, rz]

- **arm** - 0 - Left. 1 -

- **Return:**

Base coordinates

### 11 Speed ​​planning

**11.1** ` get_plan_acceleration(id=0)`

- **Function:** Get planned acceleration

- **Parameters:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **Return**

Acceleration

**11.2** ` get_plan_speed(id=0)`

- **Function:** Get planned speed

- **Parameters:**

**id** – 0/1/2/3 (ALL/left arm/right arm/waist)

- **Return**

Planned speed.

**11.3** ` set_acceleration(id, acc)`

- **Function: **Set acceleration during all movements

- **Parameters:**

- **id** – 1/2/3 (left arm/right arm/waist)

- **acc** - 1 - 100

**11.4** ` get_acceleration(id)`

- **Function: **Read acceleration during all movements

- **Parameters:**

**id** – 1/2/3 (left arm/right arm/waist)

### 12 Collision Detection

**12.1** ` get_joint_current(id, joint_id)`

- **Function:**Get collision current

- **Parameters:**

- **id** - 0/1/2 (ALL/L/R)

- **joint_id** - 1 - 6

**12.2** ` collision_switch(state)`

- **Function:** Collision detection switch

- **Parameters:**

**state** (_int_) - 0 - off 1 - on (off by default)

**12.3** ` collision(left_angles, right_angles)`

- **Function:** Collision detection main program

- **Parameters:**

- **left_angles** - left arm angles, list of length 6.

- **right_angles** - right arm angles, list of length 6.

- **Return**

integer

**12.4** ` is_collision_on()`

- **Parameters:** Get collision detection state

- **Return:**

0 - disabled
1 - enabled**