# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

# -----
import pandas as pd
import json

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def route_root(name=None):
    return 'hello there from thing1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7776)