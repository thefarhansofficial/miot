import RPi.GPIO as GPIO
from Adafruit_IO import *

ADAFRUIT_IO_USERNAME = "sumeet119"
ADAFRUIT_IO_KEY = "aio_JYjA10uE6HYZ3A4FppLesM7J1pDp"
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

test = aio.feeds("button")
#print(test)
while 1:
    data = aio.receive(test.key)
    print(data.value)
    if data.value == "1":
        GPIO.output(19,1)
        GPIO.output(22,1)
    if data.value == "0":
        GPIO.output(19,0)
        GPIO.output(22,0)