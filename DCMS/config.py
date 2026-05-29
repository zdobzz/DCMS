#!/usr/bin/env python3

# imports
import createDB

# max temperature get and set
global_max_temp = 60

def set_temp_max(temp):
    global global_max_temp
    global_max_temp = temp

def get_temp_max():
    return global_max_temp

# min temperature get and set
global_min_temp = 0

def set_temp_min(temp):
    global global_min_temp
    global_min_temp = temp

def get_temp_min():
    return global_min_temp

# max humidity get and set
global_max_humid = 10

def set_humid_max(temp):
    global global_max_humid
    global_max_humid = temp

def get_humid_max():
    return global_max_humid

# min humidity get and set
global_min_humid = 60

def set_humid_min(temp):
    global global_min_humid
    global_min_humid = temp

def get_humid_min():
    return global_min_humid

# emergency takeover variable
emergency = False

def set_emergency_bool(emBool):
    global emergency
    emergency = emBool

def get_emergency_bool():
    return emergency

# lcd on boolean for checking if background has been drawn (saves on processing power)
lcd_on = False

def set_lcd_on_bool(lcdBool):
    global lcd_on
    lcd_on = lcdBool

def get_lcd_on_bool():
    return lcd_on


# database's
# errors database
global connection_errors
connection_errors = None

def get_connection_errors():
    return connection_errors

# data logging database
global connection_data
connection_data = None

def get_connection_data():
    return connection_data