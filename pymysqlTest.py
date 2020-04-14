#!/usr/bin/python3

import pymysql

# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost","root","database.W2020","testDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()