import time
import os
import struct
import threading
from enum import IntEnum

# TODO: Convert print statements to logging for debugging
'''    
  Button Type 1 enumerations
'''
class Buttons(IntEnum):
    CROSS = 0
    CIRCLE = 1
    TRIANGLE = 2
    SQUARE = 3
    L1 = 4
    R1 = 5
    SHARE = 8
    OPTIONS = 9
    HOME = 10
    L3 = 11
    R3 = 12

'''    
  Button Type 2 enumerations
'''
class Analog(IntEnum):
    L3_LEFT = 0
    L3_RIGHT = 1
    L3_UP = 10
    L3_DOWN = 11
    L2 = 20
    R3_LEFT = 30
    R3_RIGHT = 31
    R3_UP = 40
    R3_DOWN = 41
    R2 = 50
    DPAD_LEFT = 60
    DPAD_RIGHT = 61
    DPAD_UP = 70
    DPAD_DOWN = 71


class ControllerFeature:
    """
    Each controller component is broken into objects, ex. Square, L1, R2

    NOTE: ControllerFeatures must exist in Button OR Analog enumerations

    Args:
        name(IntEnum): The distinct controller feature, ex. Circle
        callback(Function): Functor that acts as event callback
    """
    def __init__(self, name, callback):
        self.name = self.is_name_valid(name)
        self.callback = callback
        self.pressed = False                    # Indicates button is pressed
        self.value = 0                          # Value of analog feature

    # Verify the name exist in
    def is_name_valid(self, name):
        if name in Buttons or name in Analog:
            return name
        else:
            print("{} is not in Buttons or Analog enumeration".format(name))
            return None



class ControllerBlueTooth:
    """
    Manages BlueTooth connection and unpacks controller dat.

    Args:
        controller_feature_list(List): List of used controller features
        interface(String): Bluetooth connection/device node
    """
    def __init__(self, controller_feature_list, interface='/dev/input/js0'):
        self.interface = interface
        self.bluetooth_connected = False
        self.controller_features = controller_feature_list
        self.format = "LhBB"
        self.event_size = struct.calcsize(self.format)
        self.bluetooth_stream = None
        self.bluetooth_thread = None
        self.type1_mapping = {}
        self.type2_mapping = {}

        for feature in controller_feature_list:
            if feature.name in Buttons:
                # Button features added to type 1 mapping
                self.type1_mapping[feature.name] = feature
            else:
                # Analog features added to type 2 mapping
                self.type2_mapping[feature.name] = feature


    def start_thread(self):
        self.bluetooth_thread = threading.Thread(target=self.read_and_unpack, daemon=True)
        self.bluetooth_thread.start()

    def connect(self):
        print("Waiting for interface: {} to become available . . .".format(self.interface))
        while not self.bluetooth_connected:
            if os.path.exists(self.interface):
                time.sleep(.1)
                self.bluetooth_connected = True
                print("Successfully bound to: {}.".format(self.interface))
                self.bluetooth_stream = open(self.interface, "rb")

    def on_disconnect_callback(self):
        print("Controller has been disconnected")
        self.bluetooth_connected = False
        self.connect()
        self.start_thread()
        
    def read_and_unpack(self):
        self.connect()
        while self.bluetooth_connected:
            self.event = self.read_stream()
            self.unpack_data()
            time.sleep(0.1)
    
    def read_stream(self):
        try:
            return self.bluetooth_stream.read(self.event_size)
        except IOError:
            self.on_disconnect_callback()
            exit(1)

    # TODO: sort_data will unpack the value, button_type, and button_id into controller feautures
    def unpack_data(self):
        (*tv_sec, value, button_type, button_id) = struct.unpack("LhBB", self.event)

        if button_type == 1 and button_id in self.type1_mapping:
            if value is 1:
                self.type1_mapping[button_id].pressed = True
            else:
                self.type1_mapping[button_id].pressed = False
            self.type1_mapping[button_id].callback()
        elif button_type == 2 and button_id in self.type2_mapping:
            if value > 0:
                self.type2_mapping[(button_id * 10) + 1].value = value
                self.type2_mapping[(button_id*10)+1].callback()
            else:
                self.type2_mapping[(button_id * 10)].value = value
                self.type2_mapping[(button_id*10)].callback()

# print("button_id: {} button_type: {} value: {}\n".format(button_id, button_type, value))
