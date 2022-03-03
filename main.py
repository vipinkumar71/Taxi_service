"""starting point for the project"""

from user import User

OPTIONS_MAP = {
    1: User().display_options,

}


def display_options():
    """options in the taxi service system """
    print("1.Taxi services")


def option_router():
    """routes option according to the input"""
    selected_option = int(input("Enter your option:"))
    return OPTIONS_MAP.get(selected_option)()


if __name__ == '__main__':
    display_options()
    option_router()
