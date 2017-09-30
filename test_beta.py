import stats
# Use: statistics.mean(liste)
 
from stats import mean
# Use: mean(liste)
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

print("Program is running")
i = 0
list_temp = []
list_hum = []

while True :
    result = instance.read()
    if result.is_valid():
        
        list_temp.append(result.temperature)
        list_hum.append(result.humidity)
        i = i + 1
        print(i)
        time.sleep(1)
    if i == 10 : 
        break

average_temp = mean(list_temp)
average_hum = mean(list_hum)
print(average_temp)
print(average_hum)

