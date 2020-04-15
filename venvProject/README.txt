# Requirements:
    - pip3 
    - python3

<<<<<<< Updated upstream
=======
Set up:
0. Make sure your python 3 installation is added to your path (for Windows)
1. pip3 install virtualenv (test using [virtualenv --version])
2. virtualenv venv 
3. source venv/bin/activate (or [venv\Scripts\activate] in windows)
4. pip3 install flask
5. pip3 install pymysql
6. python3 app.py
7. deactivate
>>>>>>> Stashed changes

# Set up (in venvProject folder):
    ## LINUX
        run: $./setup.sh
    ## WINDOWS 
        double click setup.bat


# Regular usage:
     ## LINUX
        run: $./runDBserver.sh
    ## WINDOWS 
        double click runDBserver.bat   


References:
https://www.tutorialspoint.com/python3/python_database_access.htm
https://docs.python-guide.org/dev/virtualenvs/