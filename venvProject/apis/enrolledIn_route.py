# FLASK: enrolled_in API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.enrolledIn import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()

##### enrolled_in Routes #####
@app.route("/enrolled_in", methods=['GET','POST'])
def getPost_enrolled_in():
    if request.method == 'POST':
        sname = request.args.get('SUserName')
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        cursor.execute(post_enrolled_in(sname,cname,cnum))
        db.commit()
        return jsonify("Success"), 200
    elif request.method == 'GET' and len(request.args) != 0: 
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        cursor.execute(get_cEnrolled_in(cname,cnum))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else: 
        cursor.execute(get_enrolled_in())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

@app.route("/enrolled_in/<sname>", methods=['GET', 'DELETE'])
def getDelete_enrolled_in(sname):
    if request.method == 'DELETE':
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        cursor.execute(delete_enrolled_in(sname,cname,cnum))
        db.commit()
        return jsonify("Success"), 200 
    else:
        cursor.execute(get_sEnrolled_in(sname))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200    