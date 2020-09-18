import pyController.controller as ps4
import time

interface = "/dev/input/js0"
L1_Trigger = ps4.ControllerFeature()
L2_Trigger = ps4.ControllerFeature()

controller_features = [L1_Trigger, L2_Trigger]
blue_tooth = ps4.ControllerBlueTooth(controller_features, interface)
blue_tooth.start_thread()

while True:
    print("main")
    time.sleep(10)
