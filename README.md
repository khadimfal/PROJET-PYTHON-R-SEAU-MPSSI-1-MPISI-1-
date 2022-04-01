# PROJET-PYTHON-R-SEAU-MPSSI-1-MPISI-1-
Ci-dessous, nous résumerons tous les codes mis au niveau de notre dossier mis sur Github.
•	Tout d’abord, nous avons Analyseur_Packet.py :
Dans ce fichier, nous avons un code qui va nous permettre d’analyser les paquets et ensuite les envoyer par mail.
•	Ensuite pour l’installation de MySQL, de IREDMAIL ainsi que toutes leurs dépendances, nous avons créé un script python qui va nous les gérer. Ce script se trouve dans le fichier INSTALL_ALL_DEPENDENCIES.sh. Il englobe tout ce que INSTALL_IREDMAIL_DEPENDENCIES.sh et INSTALL_MYSQL.sh doivent faire.
•	le serveur est relié  á la base de données grâce database.py.
Chacun de ses fichiers a un rôle prédéfini á jouer.
client.py permettra au client de donner ses coordonnées c’est á dire son prénom, son nom, son mail et son mot de passe afin de pouvoir se connecter au serveur. Ces données seront stockées au niveau de la base de données par le serveur. 
Lors de la connexion du client, le serveur vérifiera si les coordonnées sont dans la base de données.Si les cordonnées sont correctes il va permettre la connexion. Si non la connexion échouera et le client devra forcément donner les bonnes coordonnées pour se connecter.
•	Et enfin filtre11.pcap combien le filtre wireshark.
