import Adafruit_DHT
import time
from Adafruit_IO import *
ADAFRUIT_IO_USERNAME = "sumeet119"
ADAFRUIT_IO_KEY = "aio_JYjA10uE6HYZ3A4FppLesM7J1pDp"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        aio.send("tap",temperature);
        aio.send("hava",humidity);
    if humidity is None and temperature is None:
        {print("Sensor failure. Check wiring.")}
    time.sleep(2);
    
    
