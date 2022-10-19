from thing1.thing1 import create_app
import pytest
from flask import Blueprint, Flask, request, render_template
from flask_cors import CORS, cross_origin
import thing1.thing1

'''
GIVEN:  
        
WHEN:   
THEN:   
'''
def test_post_api_class_record(client):
    response = client.post('/api/class_record',
                           json={
                               "student_id":"3","assignment_id":"12","marks":"100"
                           })
    assert 200 == response.status_code 