"""User related crud operations will be done here"""
from config import get_db_cursor


class User:
    """User class to handle operation related to users"""
    db_table = 'user'

    def __init__(self):
        pass

    def register(self):
        username = input("Enter unique username: ")
        password = input("Enter password: ")
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO {self.db_table}(username, password) VALUES("{username}", "{password}")')
        connection.commit()
        connection.close()

    def login(self):
        username = input("Enter unique username: ")
        password = input("Enter password: ")
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f'SELECT id FROM {self.db_table} WHERE username="{username}" AND password="{password}"')
        data = cursor.fetchall()
        if not data:
            print("Authentication failed")
        else:
            print("User Logged in successfully")

