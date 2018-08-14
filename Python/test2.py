from Rass import *
from time import sleep
from time import time
#setPin function example (highly redundant)
#setPin(oldPin, newPin) or outPin(pRF, 27) etc.
outPin = setPin(outPin, outPin)
#moved to Rass.py
"""
def get_distance():
    GPIO.output(outPin, True)
    sleep(0.00001)
    GPIO.output(outPin, False)
    while(GPIO.input(inPin)) == 0:
        pulse_start = time()
    while(GPIO.input(inPin)) == 1:
        pulse_end = time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print(distance)
"""
#actual code
for i in range(100):
    get_distance(Rass.outPin, Rass.inPin, printDist = True)
    sleep(1)
