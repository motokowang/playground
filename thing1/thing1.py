# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

# -----
import pandas as pd
import json
#import mysql.connector as sql
import sqlalchemy
import pymysql

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def route_root(name=None):
    return 'hello there from thing1'

@app.route('/student/<int:student_id>', methods=['GET'])
@cross_origin()
def route_student(student_id: int):
    db_conn = sqlalchemy.create_engine('mysql+pymysql://root:yet_another_leaked_credential@bouncycastle:3306/playground')
    df = pd.read_sql_query('select * from marks', db_conn)
    return df[df.student_id == student_id].to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7776)