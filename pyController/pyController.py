import time
import os
import struct
import threading

#Test PyCharm Built in Git

class ControllerFeature:

    def __init__(self, pressed = False, analog_raw_value = 0.0,
                 value = 0, ramp_up_time = 0, ramp_down_time = 0,
                 velocity_max = 10
                 ):
        self.pressed = pressed
        self.analog_raw_value = analog_raw_value
        self.value = value
        self.ramp_up_time = ramp_up_time
        self.ramp_down_time = ramp_down_time
        self.velocity_max = velocity_max



class ControllerBlueTooth:

    def __init__(self, controller_feature_list, interface='/dev/input/js0' ):
        self.interface = interface
        self.bluetooth_connected = False
        self.controller_features = controller_feature_list
        self.format = "LhBB"

    def connect(self):
        while not self.bluetooth_connected:
            if os.path.exists(self.interface):
                self.bluetooth_connected = True


    def read_stream(self):

    def sort_data(self):



interface = "/dev/input/js0"
L1_Trigger = ControllerFeature()
L2_Trigger = ControllerFeature()

controller_features = [L1_Trigger, L2_Trigger]
blueToothThread = ControllerBlueTooth(interface, controller_features, interface)



interface = "/dev/input/js0"
print("Waiting for interface: {} to become available . . .".format(interface))
if os.path.exists(interface):
    print("Successfully bound to: {}.".format(interface))
else:
    print("DOESN'T EXIST GET A LIFE!!")
_file = open(interface, "rb")
file1 = open("rawStream.txt", "w")
file2 = open("textStream.txt", "w")
while True:
    try:
        event = _file.read(8)
        (*tv_sec, value, button_type, button_id) = struct.unpack("LhBB", event)
        L = "button_id: {} button_type: {} value: {}\n".format(button_id, button_type, value)
        file1.writelines(str(event))
        file2.writelines(L)
        time.sleep(0.1)
    except KeyboardInterrupt:
        file1.close()
        raise




