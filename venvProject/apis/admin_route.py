# FLASK: admin API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.admin import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()


##### Admin Routes #####
@app.route("/admin", methods=['GET','POST'])
def getPost_admins():
    if request.method == 'POST':
        aid = request.args['AUserName']
        name = request.args['AName']
        password = request.args['APassword']
        cursor.execute(post_admin(aid,name,password))
        db.commit()
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else: 
        cursor.execute(get_admin())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

@app.route("/admin/<aid>", methods=['GET', 'PUT'])
def get_admin(aid):
    if request.method == 'PUT':
        name = request.args['AName']
        password = request.args['APassword']
        cursor.execute(put_admin(aid,name,password))
        db.commit()
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else:
        cursor.execute(get_oneAdmin(aid))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200    
