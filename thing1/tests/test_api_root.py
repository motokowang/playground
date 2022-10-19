from thing1.thing1 import create_app
import pytest
from flask import Blueprint, Flask, request, render_template
from flask_cors import CORS, cross_origin

'''
GIVEN:  /api blueprint setup
WHEN:   Client calls /api
THEN:   200 OK
'''
def test_api_root(client):
    response = client.get('/api')
    assert 200 == response.status_code 
