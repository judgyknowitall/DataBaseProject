#!/bin/bash
pip3 install virtualenv
virtualenv venv 
source venv/bin/activate
pip3 install flask
pip3 install pymysql
deactivate