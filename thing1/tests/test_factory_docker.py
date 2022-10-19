from thing1.thing1 import create_app
import pytest


'''
GIVEN:  -
WHEN:   create_app(config_name='docker') called
THEN:   An app can be created for use with DOCKER environment
'''
def test_config_docker():
    docker_app = create_app(config_name='docker')
    assert docker_app is not None