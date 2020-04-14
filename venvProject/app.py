from flask import Flask, jsonify, request
import pymysql

from helperFunctions import *

app = Flask(__name__)


# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "database.W2020", "mytutor")
cursor = db.cursor()


# Home
@app.route("/")
def home():
    return jsonify("Welcome to MyTutor DataBase!"), 200


# Get all students
@app.route("/student/<user>", methods=['GET'])
def get_students(user):
    cursor.execute(student.get_student(user))
    return jsonify(cursor.fetchall()), 200


if __name__ == "__main__":
    app.run(debug=False)