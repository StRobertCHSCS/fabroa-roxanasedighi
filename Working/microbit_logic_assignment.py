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
micro_servo = pin3

while True:
    if moisture_value.write_digital() == 17:
        print("Your plant is in good condition.")
        music.play(music.JUMP_UP)
        display.show(Image.HAPPY)

    elif button_a.is_pressed:
         moisture_sensor >= 5 and moisture_sensor <= 12:
            print("Water your plant every two days.")
            music.play(music.JUMP_DOWN)
            sensor.temperature()

    else:
        print("you need to change the soil of the plant.")
        display.show(Image.SAD)
        led_red.write_digital(0)
        servo1.angle(45)   from microbit import *
micro_servo = pin3
micro_servo.write_angle(90)
