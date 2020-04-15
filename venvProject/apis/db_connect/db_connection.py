# Function to centralize database connection


import pymysql
import os,os.path

# Read variables for database connection
def read_dbVars():

    # Open and read the file as a single buffer
    path = os.path.join(os.getcwd(),"apis/db_connect")
    fd = open("%s/db.txt"%(path), 'r')
    Lines = fd.read().split('\n')
    fd.close()

    return Lines

# Open and execute an SQL script
def connect():

    Lines = read_dbVars()

    # Extract database information from file
    host = Lines[0]
    user = Lines[1]
    psw = Lines[2]
    db = Lines[3]


    # Open database connection (host, user, psw, db, [port=3306,...])
    db = pymysql.connect(host, user, psw, db)
    
    return db