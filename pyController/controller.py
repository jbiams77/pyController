import time
import os
import struct
import threading

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

    def __init__(self, controller_feature_list, interface='/dev/input/js0'):
        self.interface = interface
        self.bluetooth_connected = False
        self.controller_features = controller_feature_list
        self.format = "LhBB"
        self.event_size = struct.calcsize(self.format)
        self.bluetooth_stream = None
        self.connect()
        self.bluetooth_thread = None

    def start_thread(self):
        self.bluetooth_thread = threading.Thread(target=self.read_and_sort, daemon=True)
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
        
    def read_and_sort(self):
        while self.bluetooth_connected:
            self.event = self.read_stream()
            self.sort_data()
            time.sleep(0.1)
    
    def read_stream(self):
        try:
            return self.bluetooth_stream.read(self.event_size)
        except IOError:
            self.on_disconnect_callback()
            exit(1)

    # TODO: sort_data will unpack the value, button_type, and button_id into controller feautures
    def sort_data(self):
        (*tv_sec, value, button_type, button_id) = struct.unpack("LhBB", self.event)
        print("button_id: {} button_type: {} value: {}\n".format(button_id, button_type, value))
