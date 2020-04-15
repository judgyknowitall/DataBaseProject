# FLASK: payment API functions

from flask import Flask, jsonify, request
import simplejson
import pymysql

from __main__ import app
from helpers.payment import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()

# New payment or get payments to a tutor
@app.route("/payment", methods=['GET','POST'])
def payment_newAndget():

    # Used to get all the payments made to a specific tutor past a certain date
    if request.method == 'GET':
        # Retrieve parameters
        tid = request.args['TUserName']
        date = request.args['PaymentDate']

        #Execute on DB
        cursor.execute(get_paymentsToTutor(tid, date))
        return jsonify(cursor.fetchall()), 200
    
    # Used to create a new payment
    elif request.method == 'POST':
        # Retrieve parameters
        amnt = request.args['Amount']
        sid = request.args['SUserName']
        tid = request.args['TUserName']

        # Execute on DB
        cursor.execute(getAll_payments())
        # Check if it's the first payment in db
        if cursor.rowcount == 0:
            cursor.execute(new_payment(amnt,sid,tid,True))
        else:
            cursor.execute(new_payment(amnt,sid,tid))
        
        db.commit()
        return jsonify("Success!"), 200


# Get payments by student
@app.route("/payment/<user>", methods=['GET'])
def payment_getForStudent(user):

    # Common parameter
    date = request.args['PaymentDate']

    # Used to get all the payments made by a specific student past a certain date
    if len(request.args) == 1:

        cursor.execute(get_paymentsFromStudent(user, date))
        return jsonify(cursor.fetchall()), 200
    
    # Used to get all the payments made by a specific student to a tutor past a certain date
    else:
        tid = request.args['TUserName']
        cursor.execute(get_paymentsFromSToT(user,tid,date))
        return jsonify(cursor.fetchall()), 200
        