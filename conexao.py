import mysql.connector

def abrir(db):
    return mysql.connector.connect(user="root", password="root", host="127.0.0.1", database=db)
