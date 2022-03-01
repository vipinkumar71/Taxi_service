"""starting point for the project"""
from user import User
from destination import Destination
from booking import Booking
from vehicle import Vehicle

OPTIONS_MAP = {
    1: User().show_options,
    2: Destination().show_options,
    3: Booking().show_options,
    4: Vehicle().show_options
}


def show_options():
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
    show_options()
    option_router()
