"""starting point for the project"""

from login import Login
from registration import Registration

OPTIONS_MAP = {
    1: Login().display_options,
    2: Registration().display_options
}


def display_options():
    """options in the taxi service system """
    print("1:Login")
    print("2:Register here")


def option_router():
    """routes option according to the input"""
    selected_option = int(input("Enter your option:"))
    return OPTIONS_MAP.get(selected_option)()


if __name__ == '__main__':
    display_options()
    option_router()
