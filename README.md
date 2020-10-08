# pyController
[![PyPI version shields.io](https://img.shields.io/pypi/v/pyPS4Controller.svg)](https://pypi.python.org/pypi/pyPS4Controller/) 
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyPS4Controller.svg)](https://pypi.python.org/pypi/pyPS4Controller/)
##
<img src="https://github.com/jbiams77/pyController/blob/master/documents/AcE2c.png?raw=true" width="50%">

## Architecture
<img src="https://github.com/jbiams77/pyController/blob/master/documents/SoftwareArchitecture.JPG?raw=true" width="60%">


## Installation
From terminal, run update:

`sudo apt-get update`


`pip3 install pyController`

# Implementation

There are three requirements needed to implement the pyController.
## 1. Define Callbacks
The pyController exists in a thread allowing user code to execute while awaiting a controller command. When a user defined controller feature changes states, it interrupts with a callback. The callback is a functor the user defines. This function is user named and user defined. It will perform the routine that corresponds with the button mapping of the user choice. 

Ex. If the user wanted an LED to turn on when **Circle** is pressed, than the function could be defined as follows:

```
def Led_Callback():
  if(Circle.pressed):
    LED1.ON()
   else:
    LED.OFF()
```
## 2. Create the controller feature.
The flexibility of this controller implementation means controller feautres are off by default. An interruption will only occur if the user utilizes a button, joystick, or trigger. This increases the performance of user code by minimizing uneccessary interruptions. A controller feautre is an object initialized by the **ControllerFeauture** class. The feature itself is an enumeration that *must* match the enumeration. These enumerations are hard mapped to the PS4 controller button laytout. 
| Buttons   |   Analog    |
|-----------|-------------|
|  CROSS    |   L3_LEFT   |
|  CIRCLE   |   L3_RIGHT  |
|  TRIANGLE |   L3_UP     |
|  SQUARE   |   L3_DOWN   |
|    L1     |      L2     |
|    R1     |      R2     |
|   SHARE   |   R3_LEFT   |
|  OPTIONS  |   R3_RIGHT  |
|   HOME    |   R3_UP     |
|    L3     |   R3_DOWN   |
|    R3     |   DPAD_LEFT |
|           |  DPAD_RIGHT |
|           |   DPAD_UP   |
|           |   DPAD_DOWN |
