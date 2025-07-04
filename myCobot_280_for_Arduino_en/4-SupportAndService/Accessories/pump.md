# Vertical Suction Pump V2.0

**Applicable models**: myCobot 280, myPalletizer 260, mechArm 270

**Product Image**

> ![pi](../../resource\4-SupportAndService\Accessories\pump/P1.png)

**Specifications**

| Name | myCobot Vertical Suction Pump V2.0 |
| ------------ | ------------------------------------------------------------------------------------------ |
| Model | myCobot_suctionPump_V2.0_grey |
| Material | ABS injection molding |
| Color | White |
| Dimensions | Suction Pump Box: 72x52x37 Suction Pump End: 63x24.5x26.7 |
| Number of Suction Cups | 1 |
| Suction Cup Size | Diameter 20mm |
| Suction Weight | 150g |
| Power Source Equipment | Suction pump box |
| Service life | One year |
| Fixing method | Lego connector |
| Control interface | IO control |
| Use environment requirements | Normal temperature and pressure |
| Applicable equipment | ER myCobot 280 series, ER myPalletizer 260 series, ER mechArm 270 series, ER myBuddy 280 series |

**Suction pump**: Used for adsorbing objects

**Introduction**

- Suction pump, that is, vacuum adsorption pump, has one suction nozzle and one exhaust nozzle. It has the advantages of simple structure, small size, easy use, low noise, and good self-priming ability. By controlling the suction pump kit as the end effector of the robot arm, the function of adsorbing objects is performed.

- Suction pump accessories: power cord x1, Dupont wire x10, one-input and two-output connection wire x1, several Lego tech parts

**Working principle**

- When sucking objects: the air pump starts to suck air and adsorbs the objects and then stops, and there will be no air leakage in a short time.
- When putting down the objects: the electronic valve starts, the air release valve opens, and air enters the vacuum suction cup to separate from the sucked objects.

**Applicable objects**

- Paper/plastic sheets
- Flat and smooth objects
- Cards, etc.

> ![Suction pump 2.0 wiring diagram](../../resource\4-SupportAndService\Accessories\pump/P2.jpg)

**Installation and use**

- Check whether the accessories package is complete: Lego connectors, Dupont wires, double-head suction pump
> ![](../../resource\4-SupportAndService\Accessories\pump/P2.jpg)

- Double-head suction pump installation:

Structural installation:

Insert the Lego connector into the reserved socket on the suction pump:

> ![](../../resource\4-SupportAndService\Accessories\pump/P3.jpg)

Align the suction pump with the connector plugged in with the socket at the end of the robotic arm and insert it:

> ![](../../resource\4-SupportAndService\Accessories\pump/P4.jpg)

- Electrical connection:

Select the male-female DuPont wire and insert the female end into the socket marked with pins on the suction pump box:

> Male-female DuPont wire:
> ![](../../resource\4-SupportAndService\Accessories\pump/P5.jpg)
> Note the correspondence between the DuPont wire colors and pins in the figure:
> ![](../../resource\4-SupportAndService\Accessories\pump/P4.jpg)

1. Insert the male end into the robot base pin according to the given correspondence:
![](../../resource\4-SupportAndService\Accessories\pump/P7.jpg)

> The left side is the suction pump pin and the right side is the robot pin
> GND -> GND
> 5V -> 5V
> G2 -> 21
> G5 -> 20

- Programming development:
> Use python to program the suction pump

> The code is as follows:

- 280-AR version:

```python
from pymycobot import MyCobot280
import time

# Initialize a MyCobot280 object
arm = MyCobot280('COM3', 115200) # The baud rate is 115200 by default, and some boards are 1000000, please modify it according to the actual situation

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

- 280-Pi version:

```python
from pymycobot import MyCobot280
from pymycobot import PI_PORT, PI_BAUD # When using the Raspberry Pi version of mycobot, you can reference these two variables to initialize MyCobot280
import time
import RPi.GPIO as GPIO

# Initialize a MyCobot280 object
mc = MyCobot280(PI_PORT, PI_BAUD)

# Initialize
GPIO.setmode(GPIO.BCM)
# Pins 20/21 control the solenoid valve and the deflation valve respectively
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# Turn on the suction pump
def pump_on():
# Open the solenoid valve
GPIO.output(20, 0)

# Stop the suction pump
def pump_off():
# Close the solenoid valve
GPIO.output(20, 1)
time.sleep(0.05)
# Open the deflation valve
GPIO.output(21, 0)
time.sleep(1)
GPIO.output(21, 1)
time.sleep(0.05)

pump_off()
time.sleep(3)
pump_on()
time.sleep(3)
pump_off()
time.sleep(3)
GPIO.cleanup() # Release the pin channel
```