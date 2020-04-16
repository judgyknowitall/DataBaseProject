# FLASK: studentMeetsIn API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.studentMeetsIn import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()



# Create a new studentMeetsIn or delete/get an existing relationship
@app.route("/student/studentMeetsIn", methods=['GET', 'POST', 'DELETE'])
def studentMeetsIn_newOrDeleteOrGet():

    pc = request.args.get('PostalCode')

    # Get students in location
    if request.method == 'GET':

        # Retrieve parameters
        dist = request.args.get('District')
        city = request.args.get('City')
        country = request.args.get('Country')

        # Execute on DB
        cursor.execute(get_studentsInLoc(pc, dist, city, country))
        return jsonify(cursor.fetchall())
    
    # Post a new studentMeetsIn
    elif request.method == 'POST':
        sid = request.args.get('SUserName')
        cursor.execute(new_studentMeetsIn(sid, pc))

    # Delete an existing studentMeetsIn
    elif request.method == 'DELETE':
        sid = request.args.get('SUserName')
        cursor.execute(delete_studentMeetsIn(sid,pc))
    
    db.commit()
    return jsonify('Success!')


# Get locations a student meets in
@app.route("/student/<sid>/studentMeetsIn", methods=['GET'])
def studentMeetsIn_getLocation(sid):

    cursor.execute(get_locOfStudent(sid))
    return jsonify(cursor.fetchall())
