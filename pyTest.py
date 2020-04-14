# Create a new database

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="database.W2020"
)

mycursor = db.cursor()

#mycursor.execute("SELECT ")