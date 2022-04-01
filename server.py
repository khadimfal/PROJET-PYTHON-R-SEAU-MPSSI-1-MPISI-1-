#!/usr/bin python3
import socket
import time
import json
import database

def Inscription(client:socket, buffer:int):
    liste = list()
    req = "Veuillez entrer votre nom complet  de famille svp : " #1
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))


    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre mot de passe svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Inscription(liste) == True:
        req = "Inscription reussie !!!"
        client.send(req.encode("utf-8")) #2
    else:
        req = "Echec de lors de l'inscription !!!"
        client.send(req.encode("utf-8")) #2

def Connexion(client:socket,buffer:int):
    liste = list()
    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre mot de passe svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Connexion(liste) == True:
        req = "Connexion reussie !!!"
        client.send(req.encode("utf-8")) #2
    else:
        req = "Echec de lors de la connexion !!!"
        client.send(req.encode("utf-8")) #2

def openServer(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((host, port))  # Écoute sur le port 50000
    serveur.listen(5)

    client, infosClient = serveur.accept()
    print("Client connecté. Adresse " + infosClient[0])  

    while True:    
        
        reponse = "Veuillez choisir 1 pour vous inscrire ,2 pour vous connecter, 3 pour quitter "
        client.send(reponse.encode("utf-8"))
        time.sleep(2)

        requete = client.recv(buffer)
        requete_decode = requete.decode("utf-8")

        if requete_decode == "1":
            Inscription(client,buffer)

        elif requete_decode == "2":
            Connexion(client,buffer)

        elif requete_decode == "3":         
            req = "Au revoir !!!"
            client.send(req.encode("utf-8")) #2
            client.close()
            break

    serveur.close()
           
    


if __name__ == "__main__":
    
    openServer('192.168.10.1', 50000)

