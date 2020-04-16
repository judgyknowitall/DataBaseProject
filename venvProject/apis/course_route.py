# FLASK: course API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.course import *
from db_connect.db_connection import connect

# Open database connection
db = connect()
cursor = db.cursor()

##### Course Routes #####
@app.route("/course", methods=['GET', 'PUT', 'POST', 'DELETE'])
def getPutPostDelete_course():
    if request.method == 'PUT':
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        level = request.args.get('Level')
        sub = request.args.get('Subject')
        cursor.execute(put_course(cname,cnum,level,sub))
        db.commit()
        return jsonify("Success"), 200
    elif request.method == 'POST':
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        level = request.args.get('Level')
        sub = request.args.get('Subject')
        cursor.execute(post_course(cname,cnum,level,sub))
        db.commit()
        myresult = cursor.fetchall()
        return jsonify("Success"), 200
    elif request.method == 'DELETE':
        cname = request.args['CName']
        cnum = request.args['CNumber']
        cursor.execute(delete_course(cname,cnum))
        db.commit()
        return jsonify("Success"), 200 
    elif request.method == 'GET' and len(request.args) != 0:
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        level = request.args.get('Level')
        sub = request.args.get('Subject')
        cursor.execute(get_someCourses(cname,cnum,level,sub))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else: 
        cursor.execute(get_courses())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

    