"""Destination related information"""

from config import get_db_cursor


class Destination:
    """Destination class to handle operation related to destination"""
    db_table = 'destination'

    def __init__(self):
        pass

    def destination_option_map(self):
        return {
            1: self.get_list,
            2: self.add,
            3: self.update,
            4: self.delete
        }

    def display_options(self):
        """All the display option for the destination here"""
        print("1.Destination name and charges")
        print("2.Add destination and charges")
        print("3.Update destination and charges")
        print("4 Delete destination and charges")

        selected_input = int(input("Select option: "))
        if selected_input == 2:
            destination_name = input("Enter Destination Name: ")
            destination_charges = input("Enter Destination charges: ")
            self.destination_option_map().get(selected_input)(destination_name, destination_charges)
        elif selected_input == 3:
            destination_name = input("Enter Destination Name: ")
            destination_charges = input("Enter Destination charges: ")
            id = int(input("Enter your id:"))
            self.destination_option_map().get(selected_input)(destination_name, destination_charges,id)
        elif selected_input==4:
            id =int(input("Enter your id:"))
            self.destination_option_map().get(selected_input)(id)
        else:
            self.destination_option_map().get(selected_input)()

    """ADD CRUD operations"""

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.db_table}")
        for destination in cursor.fetchall():
            print(f"{destination[0]}-----{destination[1]}:{destination[2]}")
        connection.close()
        print("You got your list")

    def add(self, destination_name, destination_charges):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO  {self.db_table}(destination_name,destination_charges) VALUES('{destination_name}','{destination_charges}');")
        connection.commit()
        connection.close()
        print("Successfully added record")

    def update(self, destination_name, destination_charges, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE {self.db_table} SET destination_name ='{destination_name}', destination_charges='{destination_charges}' WHERE id ={id};")
        connection.commit()
        connection.close()
        print("Successfully Updated 1 record")

    def delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE from {self.db_table} WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully Delete 1 record")
