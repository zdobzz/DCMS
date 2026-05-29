#!/usr/bin/env python3

# Imports
import os
import sqlite3
from sqlite3 import Error

# connect to the database
def create_connection(db_name):
    path = "logs"
    connection = None
    #check if the logs folder exists, if not, create it
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        #combine the folder with the database name to have a path to the database
        db_path = os.path.join(path, db_name)
        #connect to (and create if not exists) the database
        connection = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# create the code nessacary to query the database
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")