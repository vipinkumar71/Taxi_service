"""vehicle class to handle operation related vehicle """
from config import get_db_cursor


class Vehicle:
    db_table = "vehicle"

    def __init__(self):
        pass

    def vehicle_option_map(self):
        return {
            1: self._get_list,
            2: self._add,
            3: self._update,
            4: self._delete

        }

    def display_options(self):
        """options in the taxi service system """
        print("Book Your Cab")
        print("1.Vehicle Type")
        print("2.Add Vehicle Type")
        print("3.Update Vehicle type")
        print("4.Delete Vehicle type")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            vehicle_type = input("Enter Vehicle Name:")
            self.vehicle_option_map().get(selected_input)(vehicle_type)
        elif selected_input == 3:
            vehicle_type = input("Enter Vehicle Name:")
            id = int(input("Enter Vehicle id:"))
            self.vehicle_option_map().get(selected_input)(vehicle_type, id)
        elif selected_input == 4:
            vehicle_type = input("Enter Vehicle Name:")
            id = int(input("Enter Vehicle id:"))
            self.vehicle_option_map().get(selected_input)(vehicle_type, id)
        else:
            self.vehicle_option_map().get(selected_input)()

    """ADD CRUD operations """

    def _get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.db_table}")
        for vehicle in cursor.fetchall():
            print(f"{vehicle[0]}-----{vehicle[1]}")
        connection.close()
        print("You got your list")

    def _add(self, vehicle_type):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.tb_table}(vehicle_type) VALUES('{vehicle_type}')")
        connection.commit()
        connection.close()
        print("Successfully added records")

    def _update(self, vehicle_type, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.db_table} SET vehicle_type ='{vehicle_type}' WHERE id ={id};")
        connection.commit()
        connection.close()
        print("Successfully Updated 1 record")

    def _delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE from {self.db_table} WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully Delete 1 record")
