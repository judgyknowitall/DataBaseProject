from flask import Flask, jsonify, request
import pymysql

from helperFunctions import student, admin

app = Flask(__name__)


# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "mypass", "mytutor")
cursor = db.cursor()

# HOME ###################################################################

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

# STUDENT ################################################################

# Create a new Mytutor student account
@app.route("/student", methods=['POST'])
def students_new():

    # Retrieve parameters
    sid = request.args['SUserName']
    name = request.args['SName']
    psw = request.args['SPassword']
    msg = "Success!"

    # Execute on DB
    cursor.execute(student.new_student(sid, name, psw))
    db.commit()
    return jsonify("Success!"), 200


@app.route("/student/<sid>", methods=['GET', 'PUT', 'DELETE'])
def students_getAndEdit(sid):

    # Get all students
    if request.method == 'GET':
        cursor.execute(student.get_student(sid))
        db.commit()
        return jsonify(cursor.fetchall()), 200
    
    # Used to update an existing student
    elif request.method =='PUT':

        # Retrieve parameters
        name = request.args['SName']
        psw = request.args['SPassword']

        # Execute on DB
        cursor.execute(student.edit_student(sid, name, psw))
        db.commit()
        return jsonify("Success!"), 200
    
    # Delete an existing Mytutor student account
    else:
        # Retrieve parameters
        psw = request.args['SPassword']

        # Execute on DB
        cursor.execute(student.delete_student(sid, psw))
        db.commit()
        return jsonify("Success!"), 200

#################################################################

##### Admin Routes #####
@app.route("/admin", methods=['GET','POST'])
def getPost_admins():
    if request.method == 'POST':
        aid = request.args['AUserName']
        name = request.args['AName']
        password = request.args['APassword']
        cursor.execute(admin.post_admin(aid,name,password))
        db.commit()
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else: 
        cursor.execute(admin.get_admin())
        myresult = cursor.fetchall()
        return jsonify(myresult), 200

@app.route("/admin/<aid>", methods=['GET', 'PUT'])
def get_admin(aid):
    if request.method == 'PUT':
        name = request.args['AName']
        password = request.args['APassword']
        cursor.execute(admin.put_admin(aid,name,password))
        db.commit()
        myresult = cursor.fetchall()
        return jsonify(myresult), 200
    else:
        cursor.execute(admin.get_oneAdmin(aid))
        myresult = cursor.fetchall()
        return jsonify(myresult), 200    


if __name__ == "__main__":
    app.run(debug=False)