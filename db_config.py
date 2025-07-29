import mysql.connector

def getDB():
    mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="aditya_cse"
    )
    return mydb