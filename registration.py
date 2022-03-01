"""Registration related information"""

from config import get_db_cursor
from login import Login


class Registration:
    """Utility for Registration"""
    table = "registration"

    def __init__(self):
        pass

    def registration_option_map(self):
        return {
            1: self.get_list,
            2: self.add,

        }

    def display_options(self):
        """All the display option for the registration here"""
        print("1. Existed UserName")
        print("2. Create username and password")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            username = input("Create your username:")
            emailid = input("Enter your Email id:")
            password = input("Set Your Password :")
            confirm_password = input("Confirm your password:")
            self.registration_option_map().get(selected_input)(username, emailid, password, confirm_password)
        else:
            self.registration_option_map().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.table}")
        for registration in cursor.fetchall():
            print(f"{registration[0]}-----{registration[1]}--{registration[2]}")
        connection.close()
        print("You got your list")

    def add(self, username, emailid, password, confirm_password):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO  {self.table}(username,emailid,password,confirm_password) VALUES('{username}','{emailid}',md5('{password}'),md5('{confirm_password}'))")
        connection.commit()
        connection.close()
        print("Successfully Register User")
