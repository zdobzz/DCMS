import time
import config
import createDB
import datetime
from getData import get_enviromental_data

create_sensor1 = """
INSERT INTO
    sensor1 (date, temperature, humidity)
VALUES
    (?, ?, ?)
"""

def insert_data(temp, humid, date):
    createDB.execute_query(config.get_connection_data(), create_sensor1, (date, temp, humid))

while True:
    temp, humid = get_enviromental_data()
    date = datetime.datetime.now()
    insert_data(temp, humid, date)
    # placeholder time so as to not fill up the database
    time.sleep(600)
    # placeholder time for testing purposes
    #time.sleep(10)