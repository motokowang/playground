from thing1.thing1 import create_app
import pytest
from flask import Blueprint, Flask, request, render_template
from flask_cors import CORS, cross_origin
import thing1.thing1

'''
GIVEN:  /api blueprint setup
        Student with id 0 exists in database PLAYGROUND with at least 1 entry of their marks
WHEN:   Client calls /api/student/0
THEN:   200 OK
'''
def test_api_student_0(client):
    response = client.get('/api/student/0')
    assert 200 == response.status_code 