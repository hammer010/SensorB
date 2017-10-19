from ftplib import FTP
ftp = FTP('192.168.1.70', 'pi', 'raspberry')

etat = ftp.getwelcome()
print "Etat : ",etat

ftp.cwd("/home/pi/Bureau")

# Ouverture Fichier
fichier = "/home/orangepi/develop/build/test.txt"
file = open(fichier,'rb')

# Envoi Fichier
ftp.storbinary('STOR '+'test.csv', file)
ftp.retrlines('LIST')
print ftp.dir()

ftp.close()
