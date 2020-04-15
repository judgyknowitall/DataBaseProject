# FLASK: canTutor API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.canTutor import *


# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "mypass", "mytutor")
cursor = db.cursor()

##### Can Tutor Routes #####
@app.route("/can_tutor", methods=['GET','POST'])
def getPost_can_tutor():
    if request.method == 'POST':
        tid = request.args['TUserName']
        cname = request.args['CName']
        cnum = request.args['CNumber']
        cursor.execute(post_canTutor(tid,cname,cnum))
        db.commit()
        return jsonify("Success"), 200
    else: 
        cursor.execute(get_canTutor())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

@app.route("/can_tutor/<tid>", methods=['GET', 'DELETE'])
def getPut_can_tutor(tid):
    if request.method == 'DELETE':
        cname = request.args['CName']
        cnum = request.args['CNumber']
        cursor.execute(delete_canTutor(tid,cname,cnum))
        db.commit()
        return jsonify("Success"), 200 
    else:
        cname = request.args['CName']
        cnum = request.args['CNumber']
        cursor.execute(get_oneTutor(tid,cname,cnum))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200    