The purpose of this application, is to create and test basic functionality for the data centre managment service (DCMS)

This is the first release

NOTE: This program uses python 3, make sure it is installed
To start the program, enter into a terminal created via the main folder the command: python3 main.py

Scripts:
alarm.py is a subprocesses and is responsible for the emergency warning systems if the sensors detect abnormal data returns
config.py is the collection of various global variables and their getters and setters
createDB.py manages the creation of the database files useing SQLLite
display.py is a subprocesses and is responsible for the display of temperature and humidity date recieved from the sensors onto the lcd display on the Sense HAT
drawBack.py manages the drawing of the white lcd's in the Sense HAT LCD panel and only runs when the lcd's are clear so as to save on processing power
error_entry.py manges the entry of errors (including emergencies) to the errors database file
getData.py manages the data collection from the sensors of the current and average temperature and humidity
logData.py is a subprocesses and manages the logging of sensor data including the time of collection to a database file
main.py is the Script that starts off the program, it creates the database files then starts the four subprocesses: alarm.py, display.py, logData.py, menu.py
menu.py is a subprocesses and displays a menu for the user and handles user input from that point on

Additional files:
logs is the folder that stores the database files
logs/dataLog.sqlite is the database that stores sensor data
logs/errors.sqlite is the databse that stores errors when they get sent there
ReadMe.txt is this file


tempfix: run in terminal:  python3 alarm.py ; python3 display.py & python3 logData.py & python3 menu.py