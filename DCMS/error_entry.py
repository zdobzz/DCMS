import time
import config
import createDB
import datetime
from getData import get_enviromental_data

create_mainError = """
INSERT INTO
    mainError (date, error_code, error_message)
VALUES
    (?, ?, ?)
"""

create_dataEmergency = """
INSERT INTO
    dataEmergency (date, emergency_code, emergency_message)
VALUES
    (?, ?, ?)
"""

# DATETIME, INTEGER, STRING

def insert_mainError(date, code, message):
    createDB.execute_query(config.get_connection_errors, create_mainError, (date, code, message))

def insert_dataEmergency(date, code, message):
    createDB.execute_query(config.get_connection_errors, create_dataEmergency, (date, code, message))