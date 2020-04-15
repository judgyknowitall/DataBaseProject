# FLASK: school API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.school import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()


##### School Routes #####
@app.route("/school", methods=['GET','POST'])
def getPost_school():
    if request.method == 'POST':
        sname = request.args.get('SchoolName')
        pcode = request.args.get('PostalCode')
        cursor.execute(post_school(sname,pcode))
        db.commit()
        return jsonify("Success"), 200
    elif request.method == 'GET' and len(request.args) != 0:
        pcode = request.args.get('PostalCode')
        cursor.execute(get_someSchools(pcode))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else: 
        cursor.execute(get_schools())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

@app.route("/school/<sname>", methods=['GET', 'PUT', 'DELETE'])
def getPutDelete_school(sname):
    if request.method == 'PUT':
        pcode = request.args.get('PostalCode')
        cursor.execute(put_school(sname,pcode))
        db.commit()
        return jsonify("Success"), 200
    elif request.method == 'DELETE':
        cursor.execute(delete_school(sname))
        db.commit()
        return jsonify("Success"), 200 
    else:
        cursor.execute(get_school(sname))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200    