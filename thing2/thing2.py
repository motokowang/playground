# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from email.encoders import encode_7or8bit
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import requests
# -----
import pandas as pd
import json
import subprocess as sp


from os import listdir, mkdir
from os.path import isfile, join
import os

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def route_root(name=None):
    return 'hello there from thing2'


@app.route('/hello', methods=['POST', 'GET'])
@cross_origin()
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)