from thing1.thing1 import create_app
import pytest


'''
GIVEN:  -
WHEN:   create_app(config_name='pytest') called
THEN:   An app can be created for use with DOCKER environment
'''
def test_config_pytest():
    pytest_app = create_app(config_name='pytest')
    assert pytest_app is not None