#!/bin/bash
python3 apis/db_connect/db_connSetup.py
read -n1 -r -p "Press any key to continue..." key
pip3 install virtualenv
virtualenv venv 
source venv/bin/activate
pip3 install flask
pip3 install pymysql
pip3 install simplejson
deactivate