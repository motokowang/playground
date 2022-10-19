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
def test_engine_exists(client):
    create_app()
    assert thing1.thing1.engine is not None
