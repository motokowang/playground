from thing1.thing1 import create_app
import pytest


'''
GIVEN:  -
WHEN:   create_app(config_name='docker') called
THEN:   An app can be created for use with DOCKER environment
'''
def test_config_throw_exception():
    with pytest.raises(Exception) as e_info:
        exception_thrown_app = create_app(config_name='invalid entry')