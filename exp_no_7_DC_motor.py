import RPi.GPIO as GPIO
import time
from Adafruit_IO import *

ADAFRUIT_IO_USERNAME = "sumeet119"
ADAFRUIT_IO_KEY = "aio_JYjA10uE6HYZ3A4FppLesM7J1pDp"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)  #en 1,2     5
GPIO.setup(26,GPIO.OUT)  #en 3,4     7
GPIO.setup(23,GPIO.OUT)  #dir 1 A    11
GPIO.setup(24,GPIO.OUT)  #dir 1 B    8
GPIO.setup(21,GPIO.OUT)  #dir 2 A    9
GPIO.setup(22,GPIO.OUT)  #dir 2 B    25
P = GPIO.PWM(29,100)
Q = GPIO.PWM(26,100)

test=aio.feeds("dir")
Duty=aio.feeds("speed")

while 1:
    data = aio.receive(test.key)
    PWM = aio.receive(Duty.key)
    print(data.value)
    print(PWM.value)
    if data.value == "1":
        P.start(int(PWM.value))
        Q.start(int(PWM.value))
        GPIO.output(23,1)
        GPIO.output(24,0)
        GPIO.output(21,1)
        GPIO.output(22,0)
    if data.value == "0":
        P.start(int(PWM.value))
        Q.start(int(PWM.value))
        GPIO.output(23,0)
        GPIO.output(24,1)
        GPIO.output(21,0)
        GPIO.output(22,1)

