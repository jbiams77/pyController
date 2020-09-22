'''
This is an example of how to initiate the left joystick and the cross button on a PS4 Bluetooth
Controller.
'''

import pyController.controller as ps4
import time

'''
1) Create user defined functions that will serve as a call-back for the controller features.
'''

def L3_LEFT_callback():
    # These functions can be user defined and named. These functions are passed as functors and
    # will only be called when a controller event has occured.
    print("Moved {NAME} by {VALUE}.".format(NAME="L3_LEFT", VALUE=L3_LEFT_feature.value))


def L3_RIGHT_callback():
    print("Moved {NAME} by {VALUE}.".format(NAME="L3_RIGHT", VALUE=L3_RIGHT_feature.value))


def L3_UP_callback():    
    print("Moved {NAME} by {VALUE}.".format(NAME="L3_UP", VALUE=L3_UP_feature.value))


def L3_DOWN__callback():    
    print("Moved {NAME} by {VALUE}.".format(NAME="L3_DOWN", VALUE=L3_DOWN_feature.value))

def CROSS_callback():
    print("Moved {NAME} by {VALUE}.".format(NAME="CROSS", VALUE=CROSS_feature.pressed))
    
    
# this is the standard interface used by the Raspbery Pi when a bluetooth controller is connected.
interface = "/dev/input/js0"

# Create the controller feature objects and pass the enumerations of which feature is being
# activated and pass the user defined functor from above.
L3_LEFT_feature = ps4.ControllerFeature(ps4.Analog.L3_LEFT, L3_LEFT_callback)
L3_RIGHT_feature = ps4.ControllerFeature(ps4.Analog.L3_RIGHT, L3_RIGHT_callback)
L3_UP_feature = ps4.ControllerFeature(ps4.Analog.L3_UP, L3_UP_callback)
L3_DOWN_feature = ps4.ControllerFeature(ps4.Analog.L3_DOWN, L3_DOWN__callback)
CROSS_feature = ps4.ControllerFeature(ps4.Buttons.CROSS, CROSS_callback)

# Create a  list of the controller features
controller_features = [L3_LEFT_feature, L3_RIGHT_feature, L3_UP_feature, L3_DOWN_feature, CROSS_feature]

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
        print("Thread tests")
        time.sleep(10)

if __name__ == "__main__":
    # execute only if run as a script
    main()
