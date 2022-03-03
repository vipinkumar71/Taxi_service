"""starting point for the project"""
from destination import Destination
from vehicle import Vehicle


class Option:
    OPTION_MAP = {

    }

    def display_options(self):
        """options in the taxi service system """
        print("welcome to taxi service System")
        print("Select your option")
        print("1.User ")
        print("2.Destination ")
        print("3.Booking ")
        print("4.Vehicle ")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            Destination().display_options()
        elif selected_input == 4:
            Vehicle().display_options()
        else:
            self.OPTION_MAP.get(selected_input)()
