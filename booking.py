"""Booking related information """
from config import get_db_cursor


class Booking:
    db_table = "booking"

    def __init__(self):
        pass

    def booking_option_map(self):
        return {
            1: self._get_list,
        }

    def display_options(self):
        """All the display option for the Booking """
        print("Please Recharge Before Booking")
        print("1.Show booking")

    def _get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.db_table}")
        for booking in cursor.fetchall():
            print(f"{booking[0]}-----{booking[1]}:{booking[2]}:{booking[3]}")
        connection.close()
        print("You got your list")
