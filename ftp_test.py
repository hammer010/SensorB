from ftplib import FTP
ftp = FTP('192.168.1.70', 'pi', 'raspberry')

etat = ftp.getwelcome()
print "Etat : ",etat

ftp.cwd("/home/pi/Bureau")



print ftp.dir()

ftp.close()
