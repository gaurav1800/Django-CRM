import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password123'
)

# preparing cursor object
cursorObject = dataBase.cursor()

# creating a database
cursorObject.execute('CREATE DATABASE testdb')


print("Database created!")

