from ftplib import FTP
ftp = FTP('192.168.1.70', 'pi', 'raspberry')

etat = connect.getwelcome() 
print "Etat : ", etat 

print ftp.dir()

