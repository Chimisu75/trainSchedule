import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE regulation")

print("Ca marche chef !")