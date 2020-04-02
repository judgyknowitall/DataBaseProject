# Create a new database

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "database.W2020"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")