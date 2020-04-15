# DataBaseProject
CPSC 471 Team Project

Group 11 Team Members:
Kaynen M.
Zahra G.
Sam P.

Board: Asana
Communication: Slack


# Prerequisites:
- MySQL 8+
- MySQL Workbench
- Python 3
- Pip 3


# Execute:
To run this database locally: 
1. Run SQL Workbench and sign into a server, root is fine
2. In the server if a Query window is not already open in the main window, click on "Query" and "New Tab To Current Server"
3. Drag or load createSchema.sql into the query window
4. Click on "Query" and "Execute (All Or Selection)"
5. Similarly drag createTables.sql and, after selecting the newly created scheme, "mytutor", run that (Makes the tables for database), then insertData.sql (Populates the tables with fake data)
6. Enter the venvProject directory and follow the README steps to run API server
7. Now use any tool (Recommend Postman) to send REST API requests to http://localhost:5000/ at the appropriate endpoints (Valid requests described in report.pdf)
8. Press [CTRL+C] to close server


# Useful Links and Citations:
- https://www.youtube.com/watch?v=3vsC05rxZ8c
- https://www.w3schools.com/python/python_mysql_getstarted.asp
- https://dev.mysql.com/downloads/connector/python/
- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
