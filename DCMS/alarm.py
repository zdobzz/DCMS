#!/usr/bin/env python3

# Imports
from sense_hat import SenseHat
import time
import config
import datetime
from error_entry import insert_dataEmergency
from getData import get_enviromental_data

RED = (255, 0, 0)
BLUE = (0, 0, 255)
sense = SenseHat()

def red_alarm():
    sense.clear(RED)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)
    sense.clear(RED)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)

def blue_alarm():
    sense.clear(BLUE)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)
    sense.clear(BLUE)
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)

def log_emergency(code):
    date = datetime.datetime.now()
    if code == 1:
        msg = "Temperature too high"
    elif code == 2:
        msg = "Temperature too low"
    elif code == 3:
        msg = "humidity too high"
    elif code == 4:
        msg = "humidity too low"
    insert_dataEmergency(date, code, msg)

#emergency alarms in order of importance
while True:
    temp, humid = get_enviromental_data()
    emergency_check = False
    if temp > config.get_temp_max:
        config.set_emergency_bool(True)
        time.sleep(0.5)
        red_alarm()
        sense.show_message("DANGER! Temperature is too high: " + str(temp) + "°C", text_colour=RED)
        emergency_check = True
        log_emergency(1)
    elif humid < config.get_humid_max:
        config.set_emergency_bool(True)
        time.sleep(0.5)
        red_alarm()
        sense.show_message("DANGER! Humidity is too high: " + str(humid) + "%", text_colour=RED)
        emergency_check = True
        log_emergency(3)
    elif humid < config.get_humid_min:
        config.set_emergency_bool(True)
        time.sleep(0.5)
        blue_alarm()
        sense.show_message("DANGER! Humidity is too low: " + str(humid) + "%", text_colour=BLUE)
        emergency_check = True
        log_emergency(4)
    elif temp < config.get_temp_min:
        config.set_emergency_bool(True)
        time.sleep(0.5)
        blue_alarm()
        sense.show_message("DANGER! Temperature is too low: " + str(temp) + "°C", text_colour=BLUE)
        emergency_check = True
        log_emergency(2)
    else:
        emergency_check = False
    sense.clear()
    if emergency_check == False:
        config.set_emergency_bool(False)
        config.set_lcd_on_bool(False)
        time.sleep(2)
    else:
        time.sleep(0.5)
    
    