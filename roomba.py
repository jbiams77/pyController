#!/usr/bin/env python

'''
This is an example of how to initiate the left joystick and the cross button on a PS4 Bluetooth
Controller.
'''


import PiMotor
import RPi.GPIO as GPIO
import controller as ps4
import time

#Name of Individual MOTORS 
left_wheel  = PiMotor.Motor("MOTOR3",1)
right_wheel = PiMotor.Motor("MOTOR1",1)


'''
1) Create user defined functions that will serve as a call-back for the controller features.
'''

def Left_Button():
    if(L1.pressed):
        right_wheel.forward(100)
    else:
        right_wheel.stop()
    

def Right_Button():
    if(R1.pressed):
        left_wheel.forward(100)
    else:
        left_wheel.stop()
        
def Back_Button():
    if(BACK.pressed):
        right_wheel.reverse(100)
        left_wheel.reverse(100)
    else:
        right_wheel.stop()
        left_wheel.stop()

def Forward_Button():
    if(FORWARD.pressed):
        right_wheel.forward(100)
        left_wheel.forward(100)
    else:
        right_wheel.stop()
        left_wheel.stop()

def Rotate_Right():
    if(CIRCLE.pressed):
        right_wheel.forward(100)
        left_wheel.reverse(100)
    else:
        right_wheel.stop()
        left_wheel.stop()
    
def Rotate_Left():
    if(SQUARE.pressed):
        right_wheel.reverse(100)
        left_wheel.forward(100)
    else:
        right_wheel.stop()
        left_wheel.stop()

def call_back():       
    #print("Forward {}".format(val_to_pwr(L3_UP.value)))
    Move(val_to_pwr(L3_UP.value), val_to_pwr(L3_DOWN.value), val_to_pwr(L3_LEFT.value), val_to_pwr(L3_RIGHT.value))

def val_to_pwr(value):
    if(value is 0):
        return 0
    else:
        return (value/32768)*100

def Move(Forward_Power, Reverse_Power, Left_Power, Right_Power):
    
    # Reverse
    if (Reverse_Power is not 0):
        # Right
        if (Right_Power > 50):
            left_wheel.reverse(100)
            right_wheel.stop()
        # Left
        elif (Left_Power > 50):
            right_wheel.reverse(100)
            left_wheel.stop()
        else:
            left_wheel.reverse(100)
            right_wheel.reverse(100)
    # Forward
    elif (Forward_Power is not 0):
                # Right
        if (Right_Power > 50):
            left_wheel.forward(100)
            right_wheel.stop()
        # Left
        elif (Left_Power > 50):
            right_wheel.forward(100)
            left_wheel.stop()
        else:
            left_wheel.forward(100)
            right_wheel.forward(100)
    # Stop
    else : 
        left_wheel.stop()
        right_wheel.stop()

# this is the standard interface used by the Raspbery Pi when a bluetooth controller is connected.
interface = "/dev/input/js0"

# Create the controller feature objects and pass the enumerations of which feature is being
# activated and pass the user defined functor from above.
L1    = ps4.ControllerFeature(ps4.Buttons.L1, Left_Button)
R1   = ps4.ControllerFeature(ps4.Buttons.R1, Right_Button)
BACK   = ps4.ControllerFeature(ps4.Buttons.CROSS, Back_Button)
CIRCLE   = ps4.ControllerFeature(ps4.Buttons.CIRCLE, Rotate_Right)
SQUARE   = ps4.ControllerFeature(ps4.Buttons.SQUARE, Rotate_Left)   
FORWARD = ps4.ControllerFeature(ps4.Buttons.TRIANGLE, Forward_Button)
L3_UP = ps4.ControllerFeature(ps4.Analog.L3_UP, call_back)
L3_DOWN = ps4.ControllerFeature(ps4.Analog.L3_DOWN, call_back)
L3_LEFT = ps4.ControllerFeature(ps4.Analog.L3_LEFT, call_back)
L3_RIGHT = ps4.ControllerFeature(ps4.Analog.L3_RIGHT, call_back)

# Create a  list of the controller features
controller_features = [L1, R1, BACK, CIRCLE, SQUARE, FORWARD, L3_UP, L3_DOWN, L3_LEFT, L3_RIGHT]

# create the bluetooth handler object and pass the list of controller
# features as well as the interface.
blue_tooth = ps4.ControllerBlueTooth(controller_features, interface)

# The controller operates in its own thread allowing the user to define their own operations
# without
blue_tooth.start_thread()



# This can be whatever the user wants but for now just shows that the controller
# runs within its own thread.
def main():
    while True:
        x=1
        time.sleep(10)

if __name__ == "__main__":
    # execute only if run as a script
    main()