# FLASK: tutorMeetsIn API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.tutorMeetsIn import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()



# Create a new tutorMeetsIn or delete/get an existing relationship
@app.route("/tutor/tutorMeetsIn", methods=['GET', 'POST', 'DELETE'])
def tutorMeetsIn_newOrDeleteOrGet():

    pc = request.args.get('PostalCode')

    # Get Tutors in location
    if request.method == 'GET':

        # Retrieve parameters
        dist = request.args.get('District')
        city = request.args.get('City')
        country = request.args.get('Country')

        # Execute on DB
        cursor.execute(get_tutorsInLoc(pc, dist, city, country))
        return jsonify(cursor.fetchall())
    
    # Post a new tutorMeetsIn
    elif request.method == 'POST':
        tid = request.args.get('TUserName')
        cursor.execute(new_tutorMeetsIn(tid, pc))

    # Delete an existing tutorMeetsIn
    elif request.method == 'DELETE':
        tid = request.args.get('TUserName')
        cursor.execute(delete_tutorMeetsIn(tid,pc))
    
    db.commit()
    return jsonify('Success!')


# Get locations a tutor meets in
@app.route("/tutor/<tid>/tutorMeetsIn", methods=['GET'])
def tutorMeetsIn_getLocation(tid):

    cursor.execute(get_locOfTutor(tid))
    return jsonify(cursor.fetchall())
