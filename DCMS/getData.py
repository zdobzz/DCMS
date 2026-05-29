#!/usr/bin/env python3

# Imports
from sense_hat import SenseHat
import time

# Variables
sense = SenseHat()


def get_enviromental_data():
    # Read Sensor data
    temp = round(sense.get_temperature(),2)
    humid = round(sense.get_humidity(),2)
    return temp, humid

def get_average_enviromental_data():
    avgTemp_total = 0.00
    avgHumid_total = 0.00
    for i in range(10):
        temp, humid = get_enviromental_data()
        avgTemp_total+=temp
        avgHumid_total+=humid
        time.sleep(0.3)
        
    temp_average = round(avgTemp_total / 10,2)
    humid_average = round(avgHumid_total / 10,2)
    return temp_average, humid_average


if __name__ == "__main__":
    x = get_average_enviromental_data()
    #x = get_enviromental_data()
    #x, y = get_enviromental_data()
    #avgTemp_total+=x
    #print(avgTemp_total)
    print(x)
    #print(avgTemp_total,avgHumid_total)