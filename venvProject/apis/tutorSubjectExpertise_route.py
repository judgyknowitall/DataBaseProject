# FLASK: student API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.tutorSubjectExpertise import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()


# Create a new subject expertise for a tutor
@app.route("/tutor/tutorSubjectExpertise", methods=['POST'])
def subjexpert_new():
    tid = request.args.get('TUserName')
    subj = request.args.get('SubjectExpertise')
    cursor.execute(new_subjExp(tid,subj))
    db.commit()
    return jsonify("Success!"), 200


# Get the subject expertise of a tutor
@app.route("/tutor/<tid>/tutorSubjectExpertise", methods=['GET'])
def subjexpert_getSubj(tid):
    cursor.execute(get_subjExp(tid))
    return jsonify(cursor.fetchall()), 200


# Search for tutors with subject expertise
@app.route("/tutor/tutorSubjectExpertise/<subj>", methods=['GET'])
def subjexpert_getTut(subj):
    cursor.execute(get_tutorsPerSubjExp(subj))
    return jsonify(cursor.fetchall()), 200
