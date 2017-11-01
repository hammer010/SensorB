print("Demarrage programme")
from ftplib import FTP
from pyA20.gpio import gpio
from pyA20.gpio import port

#import RPi.GPIO as GPIO
import dht22
import time
import datetime

# Connexion serveur FTP
ftp = FTP('192.168.1.70', 'pi', 'raspberry')
etat = ftp.getwelcome()
print "Etat : ",etat

# initialize GPIO
#gpio.setwarnings(False)
#gpio.setmode(GPIO.BCM)
PIN2 = port.PA6
gpio.init()
#gpio.cleanup()

def average(list): 
    if (list!= []): return float(sum(list)) / len(list)
while true
    # read data using pin 14
    instance = dht22.DHT22(pin=PIN2)

    i = 0
    list_temp = []
    list_hum = []

    while true :
        result = instance.read()
        if result.is_valid():
        
        list_temp.append(result.temperature)
        list_hum.append(result.humidity)
        i = i + 1
        print("Mesure N*" + str(i) + " effectuee")
        time.sleep(6)
    if i == 10 : 
        break

    print("Horodatage: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
    print("Temperature: " + str(average(list_temp)) + " C")
    print("Humidite: " + str(average(list_hum)) + " %")

# Creation fichier de resultats
    fichier = open("sensorA.txt", "w")
    fichier.write(datetime.datetime.now().strftime("%H:%M"))
    fichier.write("\n" + str(average(list_temp)))
    fichier.write("\n" + str(average(list_hum)))
    fichier.close()

# Envoi resultats vers serveur FTP
    ftp.cwd("/var/www/html")
    fichier = "/home/orangepi/develop/DHT22-Python-library-Orange-PI/sensorA.txt"
    file = open(fichier,'rb')
    ftp.storbinary('STOR '+'sensorA.txt', file)
    ftp.retrlines('LIST')
    print ftp.dir()
    ftp.close()

# Fin du programme
print("Sauvegarde des resultats effectuee")
print("Attente 5 min")
time.sleep(300)
