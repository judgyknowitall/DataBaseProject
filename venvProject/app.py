from flask import Flask, jsonify, request
import pymysql

#import helperz.py

app = Flask(__name__)


# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "database.W2020", "mytutor")
cursor = db.cursor()


@app.route("/")
def dummy_api():
    cursor.execute("SELECT * FROM admin")
    myresult = cursor.fetchall()
    return jsonify(myresult), 200

@app.route("/student")
def get_students():
    cursor.execute("SELECT * FROM student")
    myresult = cursor.fetchall()
    return jsonify(myresult), 200


if __name__ == "__main__":
    app.run(debug=False)