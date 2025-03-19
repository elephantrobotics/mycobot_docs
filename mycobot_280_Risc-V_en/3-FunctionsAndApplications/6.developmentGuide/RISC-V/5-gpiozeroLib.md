# gpiozero library usage

MyCobot 280 Risc-V is not currently compatible with the `RPi.GPIO` library, so the `gpiozero` library is required to control GPIO devices. `gpiozero` is a simple and easy-to-use GPIO control library that supports a variety of GPIO device operations.

### **Install the gpiozero library**

Use the following command to install the `gpiozero` library (it is recommended to install it in a virtual environment):

```
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple gpiozero==2.0.3
```

- **`--index-url`**: Specify to download the precompiled Python package from the pip source of Spacemit.

### **Give GPIO devices read and write permissions**

By default, GPIO devices have limited access permissions. In order to allow ordinary users to access the GPIO device, you need to modify the permissions of the device file:

```
sudo chmod a+rw /dev/gpiochip0
```

### **gpiozero usage tutorial**

For detailed usage of the `gpiozero` library, please refer to the following document:

**[Using GPIO from Python](https://bianbu.spacemit.com/development/python#%E4%BB%8E-python-%E4%BD%BF%E7%94%A8-gpio)**

### **Test code**

The following is a simple test code for controlling the suction pump and the exhaust valve:

```python
import time
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device
from gpiozero import LED

# Explicitly specify the GPIO device file
Device.pin_factory = LGPIOFactory(chip=0) # Use /dev/gpiochip0

# Initialize the device controlled by GPIO
pump = LED(71) # Use the LED class to control GPIO 71 (suction pump)
valve = LED(72) # Use the LED class to control GPIO 72 (deflation valve)

# Turn on the suction pump
pump.on()
print("Suction pump is turned on")

# Wait for 3 seconds
time.sleep(3)

# Turn off the suction pump
pump.off()
print("Suction pump is turned off")
time.sleep(0.05)

# Turn on the deflation valve
valve.on()
print("Deflation valve is turned on")
time.sleep(1)

# Close the vent valve
valve.off()
print("The vent valve is closed")
time.sleep(0.05)
```

During the test, pay attention to the following points:

- GPIO pin number: Make sure the GPIO pin number used is consistent with the actual hardware connection.
- Permission issue: If you are prompted with insufficient permissions or cannot open the device when running the code, make sure that the permissions of `/dev/gpiochip0` are set correctly.
- Hardware connection: Make sure that the suction pump and the exhaust valve are correctly connected to the GPIO pins.