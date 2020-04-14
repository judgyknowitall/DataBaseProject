from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# Open database connection (host, user, psw, db, [port=3306,...])
db = pymysql.connect("localhost", "root", "database.W2020", "testDB")
cursor = db.cursor()


@app.route("/")
def dummy_api():
    cursor.execute("SELECT * FROM admin")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    return jsonify(myresult), 200


if __name__ == "__main__":
    app.run()