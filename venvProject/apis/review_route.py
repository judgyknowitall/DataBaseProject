# FLASK: review API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.review import *


# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "database.W2020", "mytutor")
cursor = db.cursor()


# New review or view reviews
@app.route("/review", methods=['GET','POST'])
def reviews_newAndView():

    # Used to get all reviews of a tutor
    if request.method == 'GET':
        tid = request.args['TUserName']
        cursor.execute(get_reviewByTID(tid))
        return jsonify(cursor.fetchall()), 200

    # Create a new review
    elif request.method == 'POST':

        # Retrieve parameters
        tid = request.args['TUserName']
        sid = request.args['SUserName']
        rating = request.args['Rating']
        comment = request.args['Comment']

        #Execute on DB
        cursor.execute(new_review(tid,sid,rating,comment))
        db.commit()
        return jsonify("Success!"), 200


# Edit a specific student
@app.route("/review/<tid>/<sid>", methods=['PUT', 'DELETE'])
def reviews_getAndEdit(tid, sid):

    # PUT methods
    if request.method == 'PUT':

        # Edit accuracy of existing review
        if len(request.args) == 1:

            # Retrieve parameters
            acc = request.args['Accuracy']

            #Execute on DB
            cursor.execute(edit_reviewAcc(tid,sid,acc))
      
        # Edit an existing review
        else:

            # Retrieve parameters
            rating = request.args['Rating']
            comment = request.args['Comment']

            #Execute on DB
            cursor.execute(edit_review(tid, sid, rating, comment))

    # Delete and existing review 
    elif request.method == 'DELETE':
        cursor.execute(delete_review(tid,sid))

    db.commit()
    return jsonify("Success!"), 200

    