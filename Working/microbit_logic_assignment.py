'''
-------------------------------------------------------------------------------
Name:		microbit_logic_assignment.py
Purpose:	measuring soil moisture

Author:	Sedighi.R

Created:	date in 30/10/2019
------------------------------------------------------------------------------
'''

from microbit import *
import music

#defining pins
passive_buzzer = pin0
moisture_sensor = pin1
led_red = pin2

while True:
    if moisture_sensor.read_analog() == 17:
        print("Your plant is in good condition.")
        music.play(music.NYAN)
        display.show(Image.HAPPY)

    elif button_a.is_pressed or 5 <= moisture_sensor <= 12:
        print("Water your plant every two days.")
        music.play(music.JUMP_DOWN)
        display.scroll(temperature()) == 18

    else:
        print("you need to change the soil of the plant.")
        display.show(Image.SAD)
        led_red.write_digital(1)
        