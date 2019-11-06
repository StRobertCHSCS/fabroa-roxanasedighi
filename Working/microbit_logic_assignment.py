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
    #running temeprature sensor
    temp = temperature()

    if moisture_sensor.read_analog() > 17:
        display.scroll("Your plant is in good condition.")
        music.play(music.NYAN)
        display.show(Image.HAPPY)

    elif button_a.get_presses() or button_b.get_presses():
        display.scroll("Water your plant every two days.")
        display.scroll("The microbit temperature is" + str(temp) + "C.")
        music.play(music.JUMP_DOWN)

    else:
        display.scroll("you need to change the soil of the plant.")
        music.play(music.WAWAWAWAA)
        display.show(Image.SAD)
        led_red.write_digital(1)