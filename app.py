# Must install flask and flask-mysqldb

from flask import Flask 
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['TESTING'] = False
app.config['MYSQL_USER'] =  "sql3333301"
app.config['MYSQL_PASSWORD'] = "lnpBdKy9qu"
app.config['MYSQL_HOST'] = "sql3.freemysqlhosting.net"
app.config['MYSQL_DB'] = "sql3333301"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')
    return "Hello From dummy API! DONE!"

if __name__ == "__main__":
    app.run()