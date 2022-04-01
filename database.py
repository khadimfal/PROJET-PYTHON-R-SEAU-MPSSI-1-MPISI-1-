#!/usr/bin python3
import mysql.connector
from mysql.connector import Error

def Verifier(liste) -> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='USER',
                                            user='root',
                                            password='root')

        sql_select_Query = f"select * from user where mail = '{liste[2]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 0

    except mysql.connector.Error as e:
        return False

def Inscription(list) -> list:
    if Verifier(list) == False:
        return False

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='USER',
                                            user='root',
                                            password='root')

        mySql_insert_query = f"""INSERT INTO user(nom, mail, password) 
                            VALUES 
                            ('{list[0]}', '{list[1]}', '{list[2]}') """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
        return True

    except mysql.connector.Error as error:
        return False


def Connexion(liste)-> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='USER',
                                            user='root',
                                            password='root')

        sql_select_Query = f"select * from user where mail = '{liste[0]}' AND password = '{liste[1]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 1

    except mysql.connector.Error as e:
        return False

"""""
nom = 'bamba'
mail = 'bamba@iredmail.com'
password = 'root'

liste = [nom,mail,password]

if Inscription(liste) == True:
    print("Inscription reussie")
else:
    print("Echec de l'inscription")

liste1 = [mail,password]
if Connexion(liste1) == True:
    print("Connexion reussie")
else:
    print("Echec de la connexion")
"""""
