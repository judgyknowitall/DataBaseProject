# FLASK: offers API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.offers import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()

##### Offers Routes #####
@app.route("/offers", methods=['GET','POST'])
def getPost_offer():
    if request.method == 'POST':
        sname = request.args.get('SchoolName')
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        cursor.execute(post_offer(sname,cname,cnum))
        db.commit()
        return jsonify("Success"), 200
    elif request.method == 'GET' and len(request.args) != 0: 
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        cursor.execute(get_cOffers(cname,cnum))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else: 
        cursor.execute(get_offers())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

@app.route("/offers/<sname>", methods=['GET', 'DELETE'])
def getDelete_offer(sname):
    if request.method == 'DELETE':
        cname = request.args.get('CName')
        cnum = request.args.get('CNumber')
        cursor.execute(delete_offer(sname,cname,cnum))
        db.commit()
        return jsonify("Success"), 200 
    else:
        cursor.execute(get_sOffers(sname))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200    