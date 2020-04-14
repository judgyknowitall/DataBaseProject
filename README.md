# DataBaseProject
CPSC 471 Team Project

Team Members:
Kaynen M.
Zahra G.
Sam P.

Board: Asana
Communication: Slack


# Prerequisites:
- MySQL 8+
- MySQL Workbench
- Node JS V12+
OPTIONAL
- Python 3
- MySQL connector for python
    (install using [pip3 install mysql-connector-python])
- PopSQL


# Execute:
To run this database locally: 
1. Install the latest version of Node
2. Install the latest version of MySQL and configure the server authentication to use "Legacy mode" instead of "strong password"
3. Run SQL Workbench and sign into a server, root is fine
4. In the server if a Query window is not already open in the main window, click on "Query" and "New Tab To Current Server"
5. Drag or load the startDatabase SQL text file into the query window
6. Click on "Query" and "Execute (All Or Selection)"
7. Similarly drag the mytutor_db_script file and, after selecting the newly created scheme, "mytutor", run that (Makes the tables for database), then the mytutordata file (Populates the tables with fake data)
8. Run Command Prompt on Windows/Bash on Unix systems and use the command "npm install -g xmysql"
9. After done installing use the command "xmysql -h localhost -u [mysqlUsername] -p [mysqlPassword] -d mytutor" replacing [mysqlusername] with your server (i.e. root), and [mysqlpassword] with your password for the server.
11. Now use any tool (Reccomend Postman) to send REST API requests to http://localhost:3000/api/ at the appropriate endpoints (Valid requests described in report.pdf)
12. Press [CNTRL+C] to close server

Transforming RM diagram: SQL
using: python3 pyTest.py 


# Useful Links and Citations:
- https://www.youtube.com/watch?v=3vsC05rxZ8c
- https://www.w3schools.com/python/python_mysql_getstarted.asp
- https://dev.mysql.com/downloads/connector/python/
- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
