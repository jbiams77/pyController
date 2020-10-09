# pyController
[![PyPI version shields.io](https://img.shields.io/pypi/v/pyPS4Controller.svg)](https://pypi.python.org/pypi/pyPS4Controller/) 
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyPS4Controller.svg)](https://pypi.python.org/pypi/pyPS4Controller/)
##

# About
This tool functions as a controller management service that allows anyone to easily integrate a bluetooth wireless PS4 controller with their personal project. While this code only works with a PS4 controller layout, there are future plans to expand this to more bluetooth controller pending popularity. The code has been verified with the following controller but should work with any bluetooth PS4 controller:

https://www.amazon.com/gp/product/B07WDK245R/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1

# PS4 Button Layout
<img src="https://github.com/jbiams77/pyController/blob/master/documents/AcE2c.png?raw=true" width="50%">


## Architecture
<img src="https://github.com/jbiams77/pyController/blob/master/documents/SoftwareArchitecture.JPG?raw=true" width="60%">


## Installation
From terminal, run update:

`sudo apt-get update`


`pip3 install pyController`

# Implementation

There are three requirements needed to implement the pyController.
## 1. Import pyController
Import the pyController file. Importing it as ps4 will help remember this is strictly for a bluetooth ps4 button mapping.

`import controller as ps4`

## 2. Define Callbacks
The pyController exists in a thread allowing user code to execute while awaiting a controller command. When a user defined controller feature changes states, it interrupts with a callback. The callback is a functor the user defines. This function is user named and user defined. It will perform the routine that corresponds with the button mapping of the user choice. 

Ex. If the user wanted an LED to turn on when **Circle** is pressed, than the function could be defined as follows:

```
def Led_Callback():
  if(Circle.pressed):
    LED1.ON()
   else:
    LED.OFF()
```
## 3. Create the controller feature.
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

Creating the controller feature object means calling the contstructor with the enumeration mapped feature and call back function pointer (functor). The following is an example that could be used with the LED function in step 1. 
`
Circle_Button   = ps4.ControllerFeature(ps4.Buttons.CIRCLE, Led_Callback)
`
## 4 Create a  list of the controller features
Add the objects to a list that allows the bluetooth manger to connect controller events to user defined callbacks.
`
controller_features = [Circle_Button]
`

## 5. Create the bluetooth object
Make a bluetooth objects that passes the list of user defined controller feature objects for ControllerBlueTooth to manage. 
`
blue_tooth = ps4.ControllerBlueTooth(controller_features, interface)
`

## 6. Start the bluetooth thread

`
blue_tooth.start_thread()
`
