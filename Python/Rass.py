# importing libreries
import RPi.GPIO as GPIO
import time

# Declaring variables
# pin right forward
pRF = 17
# pin right backwards
pRB = 27

# pin left forward
pLF = 6
# pin right backwards
pLB = 5
#ultrasonic input pin
inPin = 23
#ultrasonic output pin
outPin = 24

#initialize GPIO pins on startup
def __init__(_pRF, _pRB, _pLF, _pLB, _inPin, _outPin):
    # Setting GPIO pins Access mode
    GPIO.setmode(GPIO.BCM)
    # Activating GPIO pins
    GPIO.setup(_pRF, GPIO.OUT)
    GPIO.setup(_pRB, GPIO.OUT)
    GPIO.setup(_pLF, GPIO.OUT)
    GPIO.setup(_pLB, GPIO.OUT)
    GPIO.setup(_inPin, GPIO.IN)
    GPIO.setup(_outPin, GPIO.OUT)
    print("Rass initialized!\nThank you for giving me life, humans!")
#generic pin setting function. returns the new pin number. also turns the pin off for safety
def setPin(pin, newPin, output=True, outputOnNewPin = False):
    GPIO.output(pin, GPIO.LOW)
    if output == True:
        GPIO.setup(pin, GPIO.OUT)
    else:
        GPIO.setup(pin, GPIO.IN)
    if outputOnNewPin == True:
        GPIO.output(pin, GPIO.HIGH)
    return newPin
#gets the distance as read by the ultrasonic sensor
def getDistance(outputPin, inputPin, cacheClearTime = 0.00001, pulseDurationMult = 17150, roundTo = 2, printDist = False):
    GPIO.output(outputPin, True)
    time.sleep(cacheClearTime)
    GPIO.output(outputPin, False)
    while(GPIO.input(inputPin)) == 0:
        pulse_start = time.time()
    while(GPIO.input(inputPin)) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * pulseDurationMult
    distance = round(distance, roundTo)
    if printDist == True:
        print(distance)
    return distance
# right W1heel Forwards
def rightWheelForwards():
    GPIO.output(pRF, GPIO.HIGH)
    GPIO.output(pRB, GPIO.LOW)

# right wheel Stop
def rightWheelStop():
    GPIO.output(pRF, GPIO.LOW)
    GPIO.output(pRB, GPIO.LOW)

# right Wheel Backwards
def rightWheelBackwards():
    GPIO.output(pRF, GPIO.LOW)
    GPIO.output(pRB, GPIO.HIGH)

#left wheel

# Left Wheel Backwords
def leftWheelBackwards():
    GPIO.output(pLF, GPIO.LOW)
    GPIO.output(pLB, GPIO.HIGH)

# Left wheel Stop
def leftWheelStop():
    GPIO.output(pLF, GPIO.LOW)
    GPIO.output(pLB, GPIO.LOW)

# Left Wheel Forwords
def leftWheelForwards():
    GPIO.output(pLF, GPIO.HIGH)
    GPIO.output(pLB, GPIO.LOW)

# movemnts

def forwards():
    rightWheelForwards()
    leftWheelForwards()

def backwards():
    rightWheelBackwards()
    leftWheelBackwards()


def left():
    rightWheelForwards()
    leftWheelStop()

def right():
    rightWheelStop()
    leftWheelForwards()

def stop():
    rightWheelStop()
    leftWheelStop()

#destructor
def __del__():
    GPIO.cleanup()

__init__(pRF,pRB,pLF,pLB,inPin,outPin)