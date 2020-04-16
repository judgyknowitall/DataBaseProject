# FLASK: main API function

from flask import Flask, jsonify, request
import pymysql


app = Flask(__name__)


# Import other APIs
import student_route        # STUDENT APIs
import admin_route          # ADMIN APIs
import tutor_route          # TUTOR APIs
import review_route         # REVIEW APIs

#################################################################

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
import admin_route                  # ADMIN APIs
import student_route                # STUDENT APIs
import tutor_route                  # TUTOR APIs
import tutorSubjectExpertise_route  # TUTOR_SUBJECT EXPERTISE APIs
import moderates_route              # MODERATES APIs
import payment_route                # PAYMENT APIs
import tutors_route                 # TUTORS APIs
import review_route                 # REVIEW APIs
import location_route               # LOCATION APIs
#import studentMeetsIn_route         # STUDENTMEETSIN APIs
import tutorMeetsIn_route           # TUTORMEETSIN APIs
import course_route                 # COURSE APIs
#import enrolledIn_route             # ENROLLEDIN APIs
import canTutor_route               # CANTUTOR APIs
import school_route                 # SCHOOL APIs
#import offers_route                 # OFFERS APIs

#################################################################


if __name__ == "__main__":
    app.run(debug=False)