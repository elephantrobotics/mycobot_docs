## IO control
IO is the input and output of data. There are multiple pins on the Basic and Atom of our robot arm. The input and output modes can be set through the following function interface.

* **myCobot：**

<img src="../../../resource/3-FunctionsAndApplications/6.developmentGuide/python/io/mycobotIO.jpg" style="zoom: 67%;" />

### Basic IO

**get_basic_input(pin_no)**

- **Function:** Get the working status of the bottom pin number
- **Parameter description:** `pin_no`: Indicates the specific pin number at the bottom of the robot
- **Return value:** `pin_signal`( `int`) When the returned value is 0, it means it is running in the working state, and 1 means it is stopped

**set_basic_output(pin_no, pin_signal)**

- **Function:** Set the working status of the bottom pin number
- **Parameter description:**
  - `pin_no`( `int`) The number marked on the bottom of the device only takes the digital part
  - `pin_signal`( `int`): Input 0 means set to running state, input 1 means stop state
- **Return value:** 1

**get_tof_distance()**

- **Function:** Get the detected distance (external distance detector is required)
- **Return value:** Detected distance value, unit is mm

### Atom IO

**set_pin_mode(pin_no, pin_mode)**

- **Function:** Set the state mode of the specified pin in atom
- **Parameter description:**
  - `pin_no` (int): The specific pin number on the top of the robot
  - `pin_mode` (int): Limited to 0~2
    - 0 is set to running state
    - 1 is set to stop state
    - 2 is set to pull-up mode
- **Return value:** 1

**set_digital_output(pin_no, pin_signa)**

- **Function:** Set the working state of the end pin number

- **Parameter description:**
  - `pin_no`( `int`) The number marked at the end of the device only takes the digital part
  - `pin_signal`( `int`): Enter 0 to set it to running state, enter 1 to stop state

- **Return value:** 1

**get_digital_input(self, pin_no)**

- **Function:** Get the working state of the end pin number

- **Parameter description:** `pin_no`: Indicates the specific pin number at the end of the robot

- **Return value:** `pin_signal`( `int`) When the returned value is 0, it means running in working state, and 1 means stop state

### Case use

* **MyCobot 280-Arduino version:**

```python
from pymycobot.mycobot280 import MyCobot280
import time
#Enter the above code to import the required packages for the project

# MyCobot280 class initialization requires two parameters:
    # The first is the serial port string, such as:
        # linux: "/dev/ttyUSB0"
        # windows: "COM3"
        # The second is the baud rate:
        # Arduino version: 1000000

    # For example:
        # mycobot-Arduino:
            # linux:
            # mc = MyCobot280("/dev/ttyUSB0", 1000000)
            # windows:
            # mc = MyCobot280("COM3", 1000000)

# Initialize a MyCobo280 object
# The following is the object creation code for the windows version
arm = MyCobot280('COM3', 1000000)

# Turn on the pump
def pump_on():
    arm.set_digital_output(33, 0)
    time.sleep(0.05)

# Stop the pump
def pump_off():
    arm.set_digital_output(33, 1)
    time.sleep(0.05)
    arm.set_digital_output(23, 0)
    time.sleep(1)
    arm.set_digital_output(23, 1)
    time.sleep(0.05)

for i in range(2):
    pump_on()
    time.sleep(2)
    pump_off()
    time.sleep(2)
```