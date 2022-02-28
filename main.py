"""starting point for the project"""
from user import User
from destination import Destination
from booking import Booking
from vehicle import Vehicle

OPTIONS_MAP = {
    1: User().display_option,
    2: Destination().display_option,
    3: Booking().display.option,
    4: Vehicle().display.option
}


def display_options():
    """options in the taxi service system """
    print("welcome to taxi service System")
    print("Select your option")
    print("1.User ")
    print("2.Destination ")
    print("3.Booking ")
    print("4.Vehicle ")


def option_router():
    """routes option according to the input"""
    selected_option = int(input("Enter your option:"))
    return OPTIONS_MAP.get(selected_option)()


if __name__ == '__main__':
    display_options()
    option_router()
