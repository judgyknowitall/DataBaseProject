# FLASK: student API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.student import *


# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "database.W2020", "mytutor")
cursor = db.cursor()


# Create a new Mytutor student account
@app.route("/student", methods=['POST'])
def students_new():

    # Retrieve parameters
    sid = request.args['SUserName']
    name = request.args['SName']
    psw = request.args['SPassword']
    msg = "Success!"

    # Execute on DB
    cursor.execute(new_student(sid, name, psw))
    db.commit()
    return jsonify("Success!"), 200

# select or edit a specific student
@app.route("/student/<sid>", methods=['GET', 'PUT', 'DELETE'])
def students_getAndEdit(sid):

    # Find a student by username
    if request.method == 'GET':
        cursor.execute(get_student(sid))
        db.commit()
        return jsonify(cursor.fetchall()), 200
    
    # Used to update an existing student
    elif request.method =='PUT':

        # Retrieve parameters
        name = request.args['SName']
        psw = request.args['SPassword']

        # Execute on DB
        cursor.execute(edit_student(sid, name, psw))
        db.commit()
        return jsonify("Success!"), 200
    
    # Delete an existing Mytutor student account
    else:
        # Retrieve parameters
        psw = request.args['SPassword']

        # Execute on DB
        cursor.execute(delete_student(sid, psw))
        db.commit()
        return jsonify("Success!"), 200