"""Log in related information"""

from config import get_db_cursor


class Login:
    """Utility for log_in"""
    table = "login"

    def __init__(self):
        pass

    def login_option_map(self):
        return {
            1: self.get_list,
            2: self.add,
        }

    def display_options(self):
        """All the display option for the registration here"""
        print("1. Username")
        print("2.Enter username and Password")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            username = input("Enter your username:")
            password = input("Enter Your Password :")
            self.login_option_map().get(selected_input)(username, password)
        else:
            self.login_option_map().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.table}")
        for login in cursor.fetchall():
            print(f"{login[0]}-----{login[1]}--{login[2]}")
        connection.close()
        print("You got your list")

    def add(self, username, password):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO  {self.table}(username,password) VALUES('{username}',md5('{password}'))")
        connection.commit()
        connection.close()
        print("Successfully Login User")
