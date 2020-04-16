# FLASK: tutors API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.tutors import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()


# New tutors and get tutors relationships
@app.route("/tutors", methods=['POST', 'GET'])
def tutors_newAndGet():

    # GET methods
    if request.method == 'GET':
    
        # Get tutors relationships for a specific tutor
        if 'TUserName' in request.args:
            tid = request.args.get('TUserName')
            cursor.execute(get_tutorsTutor(tid))

        # Get tutors relationship for a specific student
        else:
            sid = request.args.get('SUserName')
            cursor.execute(get_tutorsStudent(sid))

        # Execute on DB
        return jsonify(cursor.fetchall())

    # Create a new tutors relationship
    if request.method == 'POST':
        #Retrieve parameters
        tid = request.args.get('TUserName')
        sid = request.args.get('SUserName')
        start = request.args.get('StartDate')

        # Execute on DB 
        cursor.execute(getAll_tutors())
        # Check if it's the first payment in db
        if cursor.rowcount == 0:
            cursor.execute(new_tutors(tid, sid, start, True))
        else:
            cursor.execute(new_tutors(tid, sid, start))
        
        db.commit()
        return jsonify("Success!")

# Edit an existing tutors relationship
@app.route("/tutors/<tutId>", methods=['PUT', 'DELETE'])
def tutors_Edit(tutId):

    # Add an end date to an existing tutors relationship
    if request.method == 'PUT':
        end = request.args.get('EndDate')
        cursor.execute(end_tutors(tutId, end))

    # Delete an existing tutors relationship
    elif request.method == 'DELETE':
        cursor.execute(delete_tutors(tutId))

    db.commit()
    return jsonify("Success!")