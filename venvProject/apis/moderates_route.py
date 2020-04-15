# FLASK: moderates API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.moderates import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()


# Create a new moderates relation
@app.route("/admin/moderates", methods=['POST'])
def moderates_new():

# Search for review moderator

# Get all reviews moderated by an admin