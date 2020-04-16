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

    # Request Parameters
    aid = request.args.get('AUserName')
    sid = request.args.get('SUserName')
    tid = request.args.get('TUserName')

    # Executer on DB
    cursor.execute(new_moderates(aid, sid, tid))
    db.commit()
    return jsonify("Success!")


# Search for review moderator
@app.route("/admin/moderates/<sid>/<tid>", methods=['GET'])
def moderates_getModerator(sid, tid):
    cursor.execute(get_moderator(sid, tid))
    return jsonify(cursor.fetchall())

# Get all reviews moderated by an admin
@app.route("/admin/<aid>/moderates", methods=['GET'])
def moderates_getReviews(aid):
    cursor.execute(get_moderatedReview(aid))
    return jsonify(cursor.fetchall())