# FLASK: payment API functions

from flask import Flask, jsonify, request
import pymysql

from __main__ import app
from helpers.payment import *
from db_connect.db_connection import connect


# Open database connection
db = connect()
cursor = db.cursor()

