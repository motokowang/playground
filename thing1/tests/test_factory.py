from thing1.thing1 import create_app
import pytest


'''
GIVEN:  
        
WHEN:   
THEN:   
'''
def test_config():
    assert create_app()
    #assert create_app(config_name='dev')
    #assert create_app({'TESTING': True}).testing


 

# Unit Tests
#test = [({'student_id':3, 'assignment_id':0, 'marks':50}, True)]
#
#@pytest.mark.parametrize('data, expected', test)
#def test_insert_student_marks(data, expected):
#    route_class_record(data)
#    df = pd.read_json(route_student(data))
#    print(df[data])
#    
#   print(test, expected)
#   assert route_student(data) == expected