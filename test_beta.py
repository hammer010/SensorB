print("Demarrage programme")
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

def average(list): 
    if (list!= []): return float(sum(list)) / len(list)

# read data using pin 14
instance = dht22.DHT22(pin=PIN2)

i = 0
list_temp = []
list_hum = []

while True :
    result = instance.read()
    if result.is_valid():
        
        list_temp.append(result.temperature)
        list_hum.append(result.humidity)
        i = i + 1
        print("Mesure N*" + str(i) + " effectuee")
        time.sleep(2)
    if i == 10 : 
        break

print("Horodatage: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
print("Temperature: " + str(average(list_temp)) + " C")
print("Humidite: " + str(average(list_hum)) + " %")

fichier = open("sensorA.txt", "w")
fichier.write(datetime.datetime.now().strftime("%H:%M"))
fichier.write("\n" + str(average(list_temp)))
fichier.write("\n" + str(average(list_hum)))
fichier.close()
print("Sauvegarde des resultats effectuee")
print("Fin programme")
