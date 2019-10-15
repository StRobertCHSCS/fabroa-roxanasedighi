from microbit import *
import music

# assign pins
pir_sensor = pin0
led_red = pin1
sound = pin2

while True:
    # check if motion detected
    if pir_sensor.read_digital():
       led_red.write_digital(1)
       music.play('f3:4', pin=sound)
    else:
        led_red.write_digital(0)