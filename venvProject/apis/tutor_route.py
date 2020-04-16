# FLASK: student API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.tutor import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()


# Get tutors or create a new tutor
@app.route("/tutor", methods=['GET', 'POST'])
def tutor_getAndNew():

    # GET methods
    if request.method == 'GET':

        # Find all tutors for a specific subject 
        if len(request.args) != 0:
            exp = request.args['SubjectExpertise']
            cursor.execute(getExpert_tutor(exp))
        
        # Used to get the list of all tutors
        else:
            cursor.execute(getAll_tutor())
        
        return jsonify(cursor.fetchall()), 200

    # POST method: Used to create a new tutor account 
    else:
        # Retrieve parameters
        tid = request.args['TUserName']
        name = request.args['TName']
        psw = request.args['TPassword']
        bg = request.args['Background']
        msg = "Success!"

        # Execute on DB
        cursor.execute(new_tutor(tid, name, psw, bg))
        db.commit()
        return jsonify("Success!"), 200


# select or edit a specific tutor
@app.route("/tutor/<tid>", methods=['GET', 'PUT', 'DELETE'])
def tutor_getAndEdit(tid):

    # Get all details of a specific tutor  
    if request.method == 'GET':
        cursor.execute(get_tutor(tid))
        return jsonify(cursor.fetchall()), 200
    
    # PUT methods
    elif request.method == 'PUT':

        # Modify the tutor’s police check and approval result
        if "AUserName" in request.args:
            # Retrieve parameters AUserName, APassword, PoliceCheck, Result
            aid = request.args['AUserName']
            police = request.args['PoliceCheck']
            rslt = request.args['Result']

            # Execute on DB
            cursor.execute(approve_tutor(tid, aid, police, rslt))

        # Edit a specific tutor account
        else:
            # Retrieve parameters
            name = request.args['TName']
            psw = request.args['TPassword']
            bg = request.args['Background']

            # Execute on DB
            cursor.execute(edit_tutor(tid, name, psw, bg))
        
        # Commit changes
        db.commit()
        return jsonify("Success!"), 200
    
    # Used to delete a specific tutor account 
    else:
        # Retrieve parameters
        psw = request.args['TPassword']

        # Execute on DB
        cursor.execute(delete_tutor(tid, psw))
        db.commit()
        return jsonify("Success!"), 200