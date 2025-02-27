# CPSC 471: Group 11 Project
# Python script to initialize Schema
# Must run with (from project/):    
#   python3 -m dataBaseProj.myTutor_db.initializeDB.py
# TODO

# Citations: 
# https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python/19473206


#imports
import sys
import mysql.connector

from ..venvProject.apis.db_connect import db_connection


#Open and execute an SQL script
def executeMySql(filename, cur):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # Extract (and ignore) comments
        if (command.find("/*")):
            command = command.split("*/")[-1]
        if (command.find("--")):
            command = command.split('\n')[0]
        # Try to execute command
        try:
            cur.execute(command)
        except mysql.connector.Error:
            print("Command skipped")


# Main function
def main():

    db = db_connection.connect()

    mycursor = db.cursor()
    executeMySql("createSchema.sql",mycursor)       # Create Schema
    print("DataBase created") #TEST

    # Connect to newly created DataBase
    db = mysql.connector.connect(
        host="localhost",
        user=username,
        passwd=password,
        database="mytutor"
    )

    mycursor = db.cursor()
    executeMySql("createTables.sql",mycursor)       # Create Tables
    print("Tables created")
    executeMySql("insertData.sql",mycursor)         # Insert Tables


    print("Database Initialization complete")


# Run main
main()