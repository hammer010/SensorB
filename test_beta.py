from pyA20.gpio import gpio
from pyA20.gpio import port

#import RPi.GPIO as GPIO
import dht22
import time
import datetime

# initialize GPIO
#gpio.setwarnings(False)
#gpio.setmode(GPIO.BCM)
PIN2 = port.PA6
gpio.init()
#gpio.cleanup()

# read data using pin 14
instance = dht22.DHT22(pin=PIN2)

print("Start program")
i = 0

while i < 10 :
    while True:
        result = instance.read()
        if result.is_valid():
            list_temp = []
            list_temp.append(result.temperature)
            list_hum = []
            list_hum.append(result.humidity)
            print list_temp
            print list_hum
            i = i + 1
            print i
            time.sleep(5)
print("etat des listes")
print list_temp
print list_hum
