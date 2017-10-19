from ftplib import FTP
host = "192.168.1.70" # adresse du serveur FTP
user = "pi" # votre identifiant
password = "raspberry" # votre mot de passe
connect = ftp.ftplib(host,user,password) # on se connecte

etat = connect.getwelcome() # grâce à la fonction getwelcome(), on récupère le "message de bienvenue"
print "Etat : ", etat # ici, on l'affiche, cette ligne est facultative mais si vous ne l'affichez pas, c'est bête :p





connect.quit() # où "connect" est le nom de la variable dans laquelle vous avez déclaré la connexion !
