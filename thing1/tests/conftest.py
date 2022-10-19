#from thing1.thing1 import create_app
import pytest

from decimal import Decimal
from flask import Blueprint, Flask, request, render_template
from flask_cors import CORS, cross_origin
import requests

# -----
import pandas as pd
import json
from sqlalchemy import *
import pymysql

from thing1.thing1 import create_app
import thing1.thing1




@pytest.fixture
def app():
    app = create_app(config_name='pytest')
    app.config.update({
        "TESTING": True,
    })
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope='session')
def connection():
    return thing1.thing1.engine.connect()
