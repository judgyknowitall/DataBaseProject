# Create a new database

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="database.W2020",
    database="test"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM admin")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)