from sense_hat import SenseHat
import time
import config
from getData import get_enviromental_data
from drawBack import draw_background

sense = SenseHat()


def temp_draw(tempNum):
    if tempNum == 1:
        sense.set_pixel(1, 6, (0, 0, 48))
        sense.set_pixel(1, 5, (0, 0, 0))
        sense.set_pixel(1, 4, (0, 0, 0))
        sense.set_pixel(1, 3, (0, 0, 0))
        sense.set_pixel(1, 2, (0, 0, 0))
        sense.set_pixel(2, 6, (0, 0, 48))
        sense.set_pixel(2, 5, (0, 0, 0))
        sense.set_pixel(2, 4, (0, 0, 0))
        sense.set_pixel(2, 3, (0, 0, 0))
        sense.set_pixel(2, 2, (0, 0, 0))
    elif tempNum == 2:
        sense.set_pixel(1, 6, (0, 0, 48))
        sense.set_pixel(1, 5, (0, 0, 48))
        sense.set_pixel(1, 4, (0, 0, 0))
        sense.set_pixel(1, 3, (0, 0, 0))
        sense.set_pixel(1, 2, (0, 0, 0))
        sense.set_pixel(2, 6, (0, 0, 48))
        sense.set_pixel(2, 5, (0, 0, 48))
        sense.set_pixel(2, 4, (0, 0, 0))
        sense.set_pixel(2, 3, (0, 0, 0))
        sense.set_pixel(2, 2, (0, 0, 0))
    elif tempNum == 3:
        sense.set_pixel(1, 6, (0, 0, 48))
        sense.set_pixel(1, 5, (0, 0, 48))
        sense.set_pixel(1, 4, (0, 0, 48))
        sense.set_pixel(1, 3, (0, 0, 0))
        sense.set_pixel(1, 2, (0, 0, 0))
        sense.set_pixel(2, 6, (0, 0, 48))
        sense.set_pixel(2, 5, (0, 0, 48))
        sense.set_pixel(2, 4, (0, 0, 48))
        sense.set_pixel(2, 3, (0, 0, 0))
        sense.set_pixel(2, 2, (0, 0, 0))
    elif tempNum == 4:
        sense.set_pixel(1, 6, (0, 0, 48))
        sense.set_pixel(1, 5, (0, 0, 48))
        sense.set_pixel(1, 4, (0, 0, 48))
        sense.set_pixel(1, 3, (0, 0, 48))
        sense.set_pixel(1, 2, (0, 0, 0))
        sense.set_pixel(2, 6, (0, 0, 48))
        sense.set_pixel(2, 5, (0, 0, 48))
        sense.set_pixel(2, 4, (0, 0, 48))
        sense.set_pixel(2, 3, (0, 0, 48))
        sense.set_pixel(2, 2, (0, 0, 0))
    elif tempNum == 5:
        sense.set_pixel(1, 6, (0, 0, 48))
        sense.set_pixel(1, 5, (0, 0, 48))
        sense.set_pixel(1, 4, (0, 0, 48))
        sense.set_pixel(1, 3, (0, 0, 48))
        sense.set_pixel(1, 2, (0, 0, 48))
        sense.set_pixel(2, 6, (0, 0, 48))
        sense.set_pixel(2, 5, (0, 0, 48))
        sense.set_pixel(2, 4, (0, 0, 48))
        sense.set_pixel(2, 3, (0, 0, 48))
        sense.set_pixel(2, 2, (0, 0, 48))
    else:
        sense.set_pixel(1, 6, (0, 0, 0))
        sense.set_pixel(1, 5, (0, 0, 0))
        sense.set_pixel(1, 4, (0, 0, 0))
        sense.set_pixel(1, 3, (0, 0, 0))
        sense.set_pixel(1, 2, (0, 0, 0))
        sense.set_pixel(2, 6, (0, 0, 0))
        sense.set_pixel(2, 5, (0, 0, 0))
        sense.set_pixel(2, 4, (0, 0, 0))
        sense.set_pixel(2, 3, (0, 0, 0))
        sense.set_pixel(2, 2, (0, 0, 0))

def humid_draw(humidNum):
    if humidNum == 1:
        sense.set_pixel(5, 6, (0, 0, 48))
        sense.set_pixel(5, 5, (0, 0, 0))
        sense.set_pixel(5, 4, (0, 0, 0))
        sense.set_pixel(5, 3, (0, 0, 0))
        sense.set_pixel(5, 2, (0, 0, 0))
        sense.set_pixel(6, 6, (0, 0, 48))
        sense.set_pixel(6, 5, (0, 0, 0))
        sense.set_pixel(6, 4, (0, 0, 0))
        sense.set_pixel(6, 3, (0, 0, 0))
        sense.set_pixel(6, 2, (0, 0, 0))
    elif humidNum == 2:
        sense.set_pixel(5, 6, (0, 0, 48))
        sense.set_pixel(5, 5, (0, 0, 48))
        sense.set_pixel(5, 4, (0, 0, 0))
        sense.set_pixel(5, 3, (0, 0, 0))
        sense.set_pixel(5, 2, (0, 0, 0))
        sense.set_pixel(6, 6, (0, 0, 48))
        sense.set_pixel(6, 5, (0, 0, 48))
        sense.set_pixel(6, 4, (0, 0, 0))
        sense.set_pixel(6, 3, (0, 0, 0))
        sense.set_pixel(6, 2, (0, 0, 0))
    elif humidNum == 3:
        sense.set_pixel(5, 6, (0, 0, 48))
        sense.set_pixel(5, 5, (0, 0, 48))
        sense.set_pixel(5, 4, (0, 0, 48))
        sense.set_pixel(5, 3, (0, 0, 0))
        sense.set_pixel(5, 2, (0, 0, 0))
        sense.set_pixel(6, 6, (0, 0, 48))
        sense.set_pixel(6, 5, (0, 0, 48))
        sense.set_pixel(6, 4, (0, 0, 48))
        sense.set_pixel(6, 3, (0, 0, 0))
        sense.set_pixel(6, 2, (0, 0, 0))
    elif humidNum == 4:
        sense.set_pixel(5, 6, (0, 0, 48))
        sense.set_pixel(5, 5, (0, 0, 48))
        sense.set_pixel(5, 4, (0, 0, 48))
        sense.set_pixel(5, 3, (0, 0, 48))
        sense.set_pixel(5, 2, (0, 0, 0))
        sense.set_pixel(6, 6, (0, 0, 48))
        sense.set_pixel(6, 5, (0, 0, 48))
        sense.set_pixel(6, 4, (0, 0, 48))
        sense.set_pixel(6, 3, (0, 0, 48))
        sense.set_pixel(6, 2, (0, 0, 0))
    elif humidNum == 5:
        sense.set_pixel(5, 6, (0, 0, 48))
        sense.set_pixel(5, 5, (0, 0, 48))
        sense.set_pixel(5, 4, (0, 0, 48))
        sense.set_pixel(5, 3, (0, 0, 48))
        sense.set_pixel(5, 2, (0, 0, 48))
        sense.set_pixel(6, 6, (0, 0, 48))
        sense.set_pixel(6, 5, (0, 0, 48))
        sense.set_pixel(6, 4, (0, 0, 48))
        sense.set_pixel(6, 3, (0, 0, 48))
        sense.set_pixel(6, 2, (0, 0, 48))
    else:
        sense.set_pixel(5, 6, (0, 0, 0))
        sense.set_pixel(5, 5, (0, 0, 0))
        sense.set_pixel(5, 4, (0, 0, 0))
        sense.set_pixel(5, 3, (0, 0, 0))
        sense.set_pixel(5, 2, (0, 0, 0))
        sense.set_pixel(6, 6, (0, 0, 0))
        sense.set_pixel(6, 5, (0, 0, 0))
        sense.set_pixel(6, 4, (0, 0, 0))
        sense.set_pixel(6, 3, (0, 0, 0))
        sense.set_pixel(6, 2, (0, 0, 0))


while not config.get_emergency_bool():
    temp, humid = get_enviromental_data()
    if config.get_lcd_on_bool() == False:
        draw_background()
        config.set_lcd_on_bool(True)
    elif config.get_lcd_on_bool() == True:


        if temp < 20:
            temp_draw(1)
        elif temp >= 20 and temp < 40:
            temp_draw(2)
        elif temp >= 40 and temp < 60:
            temp_draw(3)
        elif temp >= 60 and temp < 80:
            temp_draw(4)
        elif temp >= 80:
            temp_draw(5)
        else:
            temp_draw()

        if humid < 20:
            humid_draw(1)
        elif humid >= 20 and humid < 40:
            humid_draw(2)
        elif humid >= 40 and humid < 60:
            humid_draw(3)
        elif humid >= 60 and humid < 80:
            humid_draw(4)
        elif humid >= 80:
            humid_draw(5)
        else:
            humid_draw()
    