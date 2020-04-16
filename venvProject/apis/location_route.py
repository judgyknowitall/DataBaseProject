# FLASK: location API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.location import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()

# New payment or get payments to a tutor
@app.route("/location", methods=['GET','POST'])
def location():

    # Retrieve parameters
    dist = request.args.get('District')
    city = request.args.get('City')
    country = request.args.get('Country')

    # Find locations
    if request.method == 'GET':
        cursor.execute(get_location(dist, city, country))
        return jsonify(cursor.fetchall())

    # Create new location in database
    elif request.method == 'POST':
        pc = request.args.get('PostalCode')
        cursor.execute(new_location(pc, dist, city, country))
        db.commit()
        return jsonify("Success!")
