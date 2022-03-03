"""User related crud operations will be done here"""

from config import get_db_cursor
from option import Option


class User:
    """User class to handle operation related to users"""
    db_table = 'user'

    def __init__(self):
        pass

    OPTIONS_MAP = {
        1: Option().display_options

    }

    def user_option_map(self):
        return {
            1: self.login,
            2: self.register
        }

    def display_options(self):
        """options in the taxi service system """
        print("1:Login")
        print("2:Register here")

        selected_input = int(input("Select option: "))
        if selected_input == 1:
            username = input("Enter unique username: ")
            password = input("Enter password: ")
            self.user_option_map().get(selected_input)(username, password)
        else:
            username = input("Enter unique username: ")
            password = input("Enter password: ")
            self.user_option_map().get(selected_input)(username, password)

    def register(self, username, password):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO {self.db_table}(username, password) VALUES("{username}", "{password}")')
        connection.commit()
        connection.close()

    def login(self, username, password):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f'SELECT id FROM {self.db_table} WHERE username="{username}" AND password="{password}"')
        data = cursor.fetchall()
        if not data:
            print("Authentication failed")
        else:
            print("User Logged in successfully")
            Option().display_options()
