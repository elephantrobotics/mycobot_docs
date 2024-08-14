# IO control
IO is the input and output of data. There are multiple pins on the Basic and Atom of our robot arm. The input and output modes can be set through the following function interface.

* **myCobot：**

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\io/mycobotIO.jpg" style="zoom: 67%;" />

## myCobot

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
- **Return value: ** None

**get_tof_distance()**

- **Function: ** Get the detected distance (external distance detector is required)
- **Return value: ** Detected distance value, unit is mm

### Atom IO

**set_pin_mode(pin_no, pin_mode)**

- **Function: ** Set the state mode of the specified pin in atom
- **Parameter description: **
- `pin_no` (int): The specific pin number on the top of the robot
- `pin_mode` (int): Limited to 0~2
- 0 is set to running state
- 1 is set to stop state
- 2 is set to pull-up mode
- **Return value: ** None

**set_digital_output(pin_no, pin_signa)**

- **Function: ** Set the working state of the end pin number

- **Parameter description: **
- `pin_no`( `int`) The number marked at the end of the device only takes the digital part
- `pin_signal`( `int`): Enter 0 to set it to running state, enter 1 to stop state

- **Return value: ** None

**get_digital_input(self, pin_no)**

- **Function: ** Get the working state of the end pin number

- **Parameter description: ** `pin_no`: Indicates the specific pin number at the end of the robot

- **Return value: ** `pin_signal`( `int`) When the returned value is 0, it means running in working state, and 1 means stop state

### Case use

**The default serial port name of mycobot 280-JetsonNano version is "/dev/ttyTHS1" and the baud rate is 1000000，Note to change the serial port number and baud rate of the following program**.

* **MyCobot 280 version: **

```python
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD #When using the Raspberry Pi version of mycobot, you can reference these two variables to initialize MyCobot
import time
#Enter the above code to import the required packages for the project

# MyCobot class initialization requires two parameters:
# The first is the serial port string, such as:
# linux: "/dev/ttyAMA0"
# windows: "COM3"
# The second is the baud rate:
# M5 version: 115200
#
# For example:
# mycobot-M5:
# linux:
# mc = MyCobot("/dev/ttyAMA0", 1000000)
# windows:
# mc = MyCobot("COM3", 115200)
# mycobot-raspi:
# mc = MyCobot(PI_PORT, PI_BAUD)
#
# Initialize a MyCobot object
# The following is the object creation code for the windows version
mc = MyCobot("/dev/ttyTHS1", 1000000)

for count in range(5):
# Set a loop
mc.set_basic_output(2,0)
# Put basic2 into working state
mc.set_basic_output(5,0)
# Put basic position 5 into working state
time.sleep(2)
# Wait for two seconds
mc.set_basic_output(2,1)
# Stop basic position 2 from working
mc.set_basic_output(5,1)
# Stop basic position 2 from working
```