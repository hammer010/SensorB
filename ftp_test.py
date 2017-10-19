from ftplib import FTP
ftp = FTP('192.168.1.70', 'pi', 'raspberry')
print ftp.dir()
