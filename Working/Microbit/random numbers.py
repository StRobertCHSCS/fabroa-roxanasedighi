from microbit import *
import random

answer = random.randrange(100) + random.random()
display.scroll(str(answer))