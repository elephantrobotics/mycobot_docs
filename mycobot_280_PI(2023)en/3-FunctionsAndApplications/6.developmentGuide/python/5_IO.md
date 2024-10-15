## IO control
IO is the input and output of data. There are multiple pins on the Basic and Atom of our robot arm. The input and output modes can be set through the following function interface.

* **myCobot：**

<img src="../../../resource\3-FunctionsAndApplications\6.developmentGuide\python\io/mycobotIO.jpg" style="zoom: 67%;" />

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

- **Parameter description: **
- `pin_no`( `int`) The number marked at the end of the device only takes the digital part
- `pin_signal`( `int`): Enter 0 to set it to running state, enter 1 to stop state

- **Return value:** 1

**get_digital_input(self, pin_no)**

- **Function:** Get the working state of the end pin number
- **Parameter description:** `pin_no`: Indicates the specific pin number at the end of the robot
- **Return value:** `pin_signal`( `int`) When the returned value is 0, it means running in working state, and 1 means stop state

### Raspberry Pi - GPIO

When your robot is a Raspberry Pi version, you can use the following API

**Usage:**

Enter the code import at the beginning of the file:

```python
from pymycobot import MyCobot280
import RPi.GPIO as GPIO
```

**gpio_init()**

- **Function:** Initialize the GPIO module and set the BCM mode
- **Return value:** 1

**set_gpio_mode**

- **Function:** Set the Raspberry Pi GPIO pin mode
- **Parameter**
- `mode` (`str`) Input: "BCM" or "BOARD" to enter the corresponding mode

**set_gpio_output(pin_no, state)**

- **Function:** Set the pin to high or low level
- **Parameter description:**
- `pin`( `int`) Pin number
- `state`: 0 is set to low level 1 is set to high level (low level of suction pump starts working, high level stops working)
- **Return value:** 1

**get_gpio_in(pin_no)**

- **Function:** Get pin level status
- **Parameter description:**
- `pin_no`( `int`) Pin number
- **Return value:** 0 is low level 1 is high level

### Case use

```python
from pymycobot.mycobot import MyCobot280
import time
import RPi.GPIO as GPIO
#Enter the above code to import the packages required for the project

# MyCobot class initialization requires two parameters: serial and baud rate

# Initialize a MyCobot object
# Below is Raspberry Pi version of the object code
mc = MyCobot("/dev/ttyAMA0", 1000000)

# Initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
# Turn on the pump
GPIO.output(20, 0)

# Wait 2 seconds
time.sleep(2)
# Turn off the pump
GPIO.output(20，1)
time.sleep(0.05)
GPIO.output(21，0)
time.sleep(1)
GPIO.output(21，1)
time.sleep(0.05)
```