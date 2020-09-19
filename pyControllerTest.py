import pyController.controller as ps4
import time


def L3_LEFT_callback():
    # do something with the left wheel here
    print(f"pressed: {L3_LEFT_feature.value}")


def L3_RIGHT_callback():
    print(f"pressed: {L3_RIGHT_feature.value}")


def L3_UP_callback():    
    print(f"pressed: {L3_UP_feature.value}")


def L3_DOWN__callback():    
    print(f"pressed: {L3_DOWN_feature.value}")

interface = "/dev/input/js0"

L3_LEFT_feature = ps4.ControllerFeature(ps4.Analog.L3_LEFT, L3_LEFT_callback)
L3_RIGHT_feature = ps4.ControllerFeature(ps4.Analog.L3_RIGHT, L3_RIGHT_callback)
L3_UP_feature = ps4.ControllerFeature(ps4.Analog.L3_UP, L3_UP_callback)
L3_DOWN_feature = ps4.ControllerFeature(ps4.Analog.L3_DOWN, L3_DOWN__callback)

controller_features = [L3_LEFT_feature, L3_RIGHT_feature, L3_UP_feature, L3_DOWN_feature]
blue_tooth = ps4.ControllerBlueTooth(controller_features, interface)
blue_tooth.start_thread()

def main():
    while True:
        print("main")
        time.sleep(10)

if __name__ == "__main__":
    # execute only if run as a script
    main()
