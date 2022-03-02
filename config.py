"""
All the project related configuration will be in this file
"""
import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "taxi_service"

try:
    from .local_settings import *
except ImportError:
    pass


def get_db_cursor():
    connection = mysql.connector.connect(
        host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE

    )
    return connection
