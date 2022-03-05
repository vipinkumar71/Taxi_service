"""Booking related information """
from config import get_db_cursor


class Booking:
    tb_table = "booking"

    def __init__(self):
        pass

    def booking_option_map(self):
        return {
            1: self._add,
            2: self._get_list,
            3: self._delete,
            4: self._update
        }

    def display_options(self):
        """All the display option for the Booking """
        print("Please Recharge Before Booking")
        print("1.Booking")
        print("2.Show Booking")
        print("3.Cancel Booking")
        print("4.Edit your booking")

        selected_input = int(input("Enter your option:"))
        if selected_input == 1:
            user_id = int(input("Enter user id:"))
            vehicle_id = int(input("Enter vehicle id:"))
            destination_id = int(input("Enter destination id:"))
            self.booking_option_map().get(selected_input)(user_id, vehicle_id, destination_id)
        elif selected_input == 3:
            id = int(input("Enter your id:"))
            self.booking_option_map().get(selected_input)(id)
        elif selected_input == 4:
            user_id = int(input("Enter user id:"))
            destination_id = int(input("Enter destination id:"))
            vehicle_id = int(input("Enter vehicle id:"))
            id = int(input("Enter your id:"))
            self.booking_option_map().get(selected_input)(user_id,destination_id,vehicle_id,id)
        else:
            self.booking_option_map().get(selected_input)()

    def _add(self, user_id, vehicle_id, destination_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO  {self.tb_table}(user_id,vehicle_id,destination_id) VALUES('{user_id}','{vehicle_id}',{destination_id});")
        connection.commit()
        connection.close()
        print("Successfully added record")

    def _get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.tb_table}")
        for booking in cursor.fetchall():
            print(f"{booking[0]}---{booking[1]}:{booking[2]}:{booking[3]}")
        connection.close()
        print("You got your list")

    def _delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE from {self.tb_table} WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully Delete 1 record")

    def _update(self, user_id, destination_id, vehicle_id,id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {self.tb_table} SET user_id ='{user_id}', destination_id='{destination_id}',vehicle_id='{vehicle_id}' WHERE id ={id};")
        connection.commit()
        connection.close()
        print("Successfully Updated 1 record")
