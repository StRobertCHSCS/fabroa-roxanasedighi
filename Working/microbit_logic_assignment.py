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

#running pins
pin0.write_analog(1)
pin1.write_analog(1)
pin2.write_analog(1)

if moisture_sensor.read_analog() > 17:
    display.scroll("Your plant is in good condition.")
    music.play(music.NYAN)
    display.show(Image.HAPPY)

elif button_a.get_presses() or button_b.get_presses():
    display.scroll("Water your plant every two days.")
    music.play(music.JUMP_DOWN)

else:
    display.scroll("you need to change the soil of the plant.")
    led_red.write_digital(1)
    display.show(Image.SAD)
        