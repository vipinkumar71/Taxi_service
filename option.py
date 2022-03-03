"""starting point for the project"""
from booking import Booking
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
        print("3.Vehicle")
        print("4. Booking")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            Destination().display_options()
        elif selected_input == 3:
            Vehicle().display_options()
        elif selected_input == 4:
            Booking().get_list()
        else:
            self.OPTION_MAP.get(selected_input)()
