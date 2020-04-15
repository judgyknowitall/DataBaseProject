# FLASK: main API function

from flask import Flask, jsonify, request
import pymysql

#from helperFunctions import student

app = Flask(__name__)


# Home
@app.route("/")
def home():
    return jsonify("Welcome to MyTutor DataBase!"), 200

# Error Handling TODO
'''
@app.errorhandler(Exception)
def handle_exception(e):
    # Default message
    msg = 'An error has occured!'

    # Internal error
    if isinstance(e, pymysql.err.InternalError):
        msg = "Internal Error!"

    # Return message
    return jsonify(msg), 500
'''

# Import other APIs
import student_route        # STUDENT APIs
import admin_route          # ADMIN APIs
import tutor_route          # TUTOR APIs

#################################################################


if __name__ == "__main__":
    app.run(debug=False)