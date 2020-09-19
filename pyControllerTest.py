import pyController.controller as ps4
import time


def cross_callback():
    print("I'm playing a game, and you pressed cross")
    print(f"pressed: {cross_feature.pressed}")


def square_callback():
    print("I'm playing a game, and you pressed square")
    print(f"pressed: {square_feature.pressed}")


interface = "documents/test.txt"
cross_feature = ps4.ControllerFeature(ps4.Buttons.CROSS, cross_callback)
square_feature = ps4.ControllerFeature(ps4.Buttons.SQUARE, square_callback)

controller_features = [cross_feature, square_feature]
blue_tooth = ps4.ControllerBlueTooth(controller_features, interface)
blue_tooth.start_thread()

def main():
    while True:
        print("main")
        time.sleep(10)

if __name__ == "__main__":
    # execute only if run as a script
    main()
