#!/usr/bin/env python3

# Imports
import time
import config
from getData import get_average_enviromental_data

#menu loop
while True:
    print('1) get current average temperate and humidty\n2) settings\n3) exit')
    option = input()
    if option == '1':
        #pull needed data from getData.py
        temp, humid = get_average_enviromental_data()
        print('Current temperature average is: ' + str(temp) + '°C\nCurrent average humidity is: ' + str(humid) + '%')
        time.sleep(0.5)
    elif option == '2':
        while True:
            print('1) set maximum temperature\n2) set minimum temperature\n3) set maximum humidity\n4) set minimum humidity\n5) exit to main menu')
            inner_option = input()
            if inner_option == '1':
                print('current maximum temperature is: ' + config.get_temp_max + '°C\nPlease enter a new temperature (excluding the \'°C\'): ')
                userInput = input()
                if isinstance(userInput, float):
                    config.set_temp_max(round(userInput,2))
                elif isinstance(userInput, int):
                    userInput = float(userInput)
                    config.set_temp_max(round(userInput,2))
                else:
                    print('incorrect input, please enter a correct value for temperature, returning to settings menu.')
            elif inner_option == '2':
                print('current minimum temperature is: ' + config.get_temp_min + '°C\nPlease enter a new temperature (excluding the \'°C\'): ')
                userInput = input()
                if isinstance(userInput, float):
                    config.set_temp_min(round(userInput,2))
                elif isinstance(userInput, int):
                    userInput = float(userInput)
                    config.set_temp_min(round(userInput,2))
                else:
                    print('incorrect input, please enter a correct value for temperature, returning to settings menu.')
            elif inner_option == '3':
                print('current maximum humidity is: ' + config.get_humid_max + '%\nPlease enter a new humidity (excluding the \'%\'): ')
                userInput = input()
                if isinstance(userInput, float) and userInput >= 0.0 and userInput <= 100.0:
                    config.set_humid_max(round(userInput,2))
                elif isinstance(userInput, int) and userInput >= 0 and userInput <= 100:
                    userInput = float(userInput)
                    config.set_humid_max(round(userInput,2))
                else:
                    print('incorrect input, please enter a correct value for humdity, make sure also that it is between 0 and 100 returning to settings menu.')
            elif inner_option == '4':
                print('current minimum humidity is: ' + config.get_humid_min + '%\nPlease enter a new humidity (excluding the \'%\'): ')
                userInput = input()
                if isinstance(userInput, float) and userInput >= 0.0 and userInput <= 100.0:
                    config.set_humid_min(round(userInput,2))
                elif isinstance(userInput, int) and userInput >= 0 and userInput <= 100:
                    userInput = float(userInput)
                    config.set_humid_min(round(userInput,2))
                else:
                    print('incorrect input, please enter a correct value for humdity, make sure also that it is between 0 and 100 returning to settings menu.')
            elif option == '5':
                break
            else:
                print('user input not recognised, please try again!')
            time.sleep(0.5)
    elif option == '3':
        break
    else:
        print('user input not recognised, please try again!')
    time.sleep(0.5)