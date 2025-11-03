## Gripper control

Before using Python to control the gripper, you need to install and connect the gripper on the robot arm. Different grippers are compatible with different robots (for specific adaptation information, please refer to **[Product accessories](https://docs.elephantrobotics.com/docs/gitbook/2-serialproduct/2.7-accessories/2.7-accessories.html)**.)

> **Note:**
>
> MyCobot 280 adaptive gripper inserts the gripper into the pins on the Atom, see the following figure:
>
> <img src="../../../resources\3-FunctionsAndApplications\6.developmentGuide\python\Jaw/gripper1.jpg" style="zoom: 67%;" />
>


### Gripper control

**`is_gripper_moving()`**

- **Function:** Determine whether the gripper is running
- **Return value:**
  - `0`: Indicates that the gripper of the robot arm is not running
  - `1`: Indicates that the gripper of the robot arm is running
  - `-1`: Indicates an error

**`set_gripper_state(flag, speed, _type_1=None, is_torque=None)`**

- **function**: Adaptive gripper enable

- **Parameters**:

  - `flag (int) `: 0 - open 1 - close, 254 - release

  - `speed (int)`: 0 ~ 100

  - `_type_1 (int)`:

    - `1` : Adaptive gripper (default state is 1)

    - `2` : A nimble hand with 5 fingers

    - `3` : Parallel gripper

    - `4` : Flexible gripper
  - `is_torque (int)`: Whether the gripper is force-controlled. This parameter can be omitted if no type parameter is specified. (**Note: This parameter is only supported when the end-end Atom firmware version is ≥ 6.5**)

    - `0`: Non-force-controlled gripper

    - `1`: Force-controlled gripper
- **Return value**：
  - `1`: complete

**`set_gripper_value(gripper_value, speed, gripper_type=None, is_torque=None)`**

- **function**: Set the gripper value

- **Parameters**:

  - `gripper_value (int) `: 0 ~ 100

  - `speed (int)`: 0 ~ 100

  - `gripper_type (int)`:

    - `1` : Adaptive gripper (default state is 1)

    - `3` : Parallel gripper

    - `4` : Flexible gripper
  - `is_torque (int)`: Whether the gripper is force-controlled. This parameter can be omitted if no type parameter is specified. (**Note: This parameter is only supported when the end-end Atom firmware version is ≥ 6.5**)

    - `0`: Non-force-controlled gripper

    - `1`: Force-controlled gripper
- **Return value**：
  - `1`: complete

**`get_gripper_value(gripper_type=None)`**

- **Function:** Get the current position data information of the gripper
- **Parameter description:**
  - `gripper_type`: gripper type, the default is adaptive gripper
    - `1`: adaptive gripper
    - `3`: parallel gripper
    - `4`: flexible gripper
- **Return value:** Gripper data information

**`set_HTS_gripper_torque(torque)`**

- **Function:** Set adaptive gripper torque

- **Parameter description:**
  - `torque`: 150 ~ 900

- **Return value:** 0 - Setting failed; 1 - Setting successful

**`get_HTS_gripper_torque()`**

- **Function:** Get adaptive gripper torque

- **Return value:** 150 ~ 900

**`get_gripper_protect_current()`**

- **Function:** Get the gripper protection current
- **Return value:** 1 ~ 500

**`init_gripper()`**

- **Function:** Initialize the gripper
- **Return value:** 0 - Initialization failed; 1 - Initialization successful

**`set_gripper_protect_current(current)`**

- **Function:** Set the gripper protection current
- **Parameter description:**
  - `current`: 1 ~ 500
- **Return value:** 0 - Initialization failed; 1 - Initialization successful

### Example

```python
from pymycobot.mycobot280 import MyCobot280
import time
#Enter the above code to import the packages required for the project

def gripper_test(mc):
print("Start check IO part of api\n")
# Check if the gripper is moving
flag = mc.is_gripper_moving()
print("Is gripper moving: {}".format(flag))
time.sleep(1)
# Set the current position to (2048).
# Use it when you are sure you need it.
# Gripper has been initialized for a long time. Generally, there
# is no need to change the method.
# mc.set_gripper_ini()
# Set joint point 1 and let it rotate to the position 2048
mc.set_encoder(1, 2048, 20)
time.sleep(2)
# Set six joint positions and let the robot arm rotate to this position at a speed of 20
mc.set_encoders([1024, 1024, 1024, 1024, 1024, 1024], 20)
time.sleep(3)

# Let the gripper reach the 100 state at a speed of 70
mc.set_gripper_value(100, 70)
time.sleep(3)
# Let the gripper reach the 0 state at a speed of 70
mc.set_gripper_value(0, 70)
time.sleep(3)

# Set the state of the gripper to open the claw quickly at a speed of 70
mc.set_gripper_state(0, 70)
time.sleep(3)

# Set the state of the gripper to close the claw quickly at a speed of 70
mc.set_gripper_state(1, 70)
time.sleep(3)

# Get the value of the gripper
print("")
print(mc.get_gripper_value())

if __name__ == "__main__":
# MyCobot280 class initialization requires two parameters:
    # The first is a serial string, such as:
        # linux: "/dev/ttyUSB0"
        # windows: "COM3"
        # The second is the baud rate:
        # M5 version: 115200

    # Example:
        # mycobot-M5:
            # linux:
            # mc = MyCobot280("/dev/ttyAMA0", 1000000)
            # windows:
            # mc = MyCobot280("COM3", 115200)

# Initialize a MyCobot280 object
# Below is the object code for M5 version
mc = MyCobot280('COM3', 115200)
# Move it to zero
mc.set_encoders([2048, 2048, 2048, 2048, 2048, 2048], 20)
time.sleep(3) 
gripper_test(mc) 
```