#!/usr/bin/env python3

# Imports
from sense_hat import SenseHat
import time
from getData import get_average_enviromental_data
import createDB
from subprocess import *
import config

sense = SenseHat()
sense.clear()

# create databases
config.connection_errors = createDB.create_connection("errors.sqlite")
config.connection_data = connection_data = createDB.create_connection("dataLog.sqlite")

connection_errors = config.get_connection_errors()
connection_data = config.get_connection_data()

# populate databases
create_source1_table = """
CREATE TABLE IF NOT EXISTS source_1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    temperature FLOAT,
    humidity FLOAT 
);
"""
createDB.execute_query(connection_data, create_source1_table)

create_mainErrors_table = """
CREATE TABLE IF NOT EXISTS source_1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    error_code INTEGER,
    error_message STRING
);
"""
createDB.execute_query(connection_errors, create_mainErrors_table)

create_dataEmergencies_table = """
CREATE TABLE IF NOT EXISTS source_1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME,
    emergency_code INTEGER,
    emergency_message STRING
);
"""
createDB.execute_query(config.get_connection_errors(), create_dataEmergencies_table)


#TODO fix this, can't figure out how to call other scripts?
#subprocess.run("python3 alarm.py & python3 display.py & python3 logData.py & python3 menu.py")
#exec(open("alarm.py").read())
#subprocess.call("alarm.py")
