'''
This is a BLUEPRINT
'''

from decimal import Decimal
from flask import Blueprint, Flask, request, render_template
from flask_cors import CORS, cross_origin
import thing1.thing1

# -----
import pandas as pd
import json
from sqlalchemy import *
import pymysql

api_blueprint = Blueprint('api_blueprint', __name__)

'''
GET /api/
'''
@api_blueprint.route('/', methods=['POST', 'GET'], strict_slashes=False)
@cross_origin()
def route_root(name=None):
    return f'hello there from thing1 with __name__={ __name__ }'


'''
GET /api/student/<int:student_id>
'''
@api_blueprint.route('/student/<int:student_id>', methods=['GET', 'POST'], strict_slashes=False)
@cross_origin()
def route_student(student_id: int):
#    engine = create_engine('mysql+pymysql://root:yet_another_leaked_credential@bouncycastle:3306/playground',
#                            echo=True)
    df = pd.read_sql_query('select * from marks', thing1.thing1.engine)
    return df[df.student_id == student_id].to_json()


'''
This is for instructors to upload student grades
params:
    json
    {
        course_id {
            (student_id, assignment_id, marks, date),
        }
    }
'''
@api_blueprint.route('/class_record', methods=['POST'], strict_slashes=False)
@cross_origin()
def route_class_record():
    
    student_id = request.json['student_id']
    assignment_id = request.json['assignment_id']
    marks = request.json['marks']
    
    if not (student_id and assignment_id and marks):
        return 'Missing stuff'
    
    engine = create_engine('mysql+pymysql://root:yet_another_leaked_credential@bouncycastle:3306/playground',
                           echo=True)
    with engine.connect() as コネ:
        メタ = MetaData(engine)
        marks_tbl = Table('marks', メタ, autoload=True, autoload_with=engine)
        
        sql = marks_tbl.insert().values(student_id=student_id, assignment_id=assignment_id, marks=marks)
        コネ.execute(sql)

    return f'inserted: student_id: { student_id }, assignment_id: { assignment_id }, marks: { marks }'

'''
This is for instructors to upload student grades
params:
    json
    {
        course_id {
            (student_id, assignment_id, marks, date),
        }
    }
'''
@api_blueprint.route('/class_records', methods=['GET', 'POST'], strict_slashes=False)
@cross_origin()
def route_class_records():
    db_conn = create_engine('mysql+pymysql://root:yet_another_leaked_credential@bouncycastle:3306/playground',
                            echo=True)
    
    sql_insert_values = str()
    class_records = list(request.json['class_records'])
    for record in class_records:
        sql_insert_values += record + ','
        
    print(f'---- { class_records.values() }')
    
    return list(class_records.values())


#if __name__ == '__main__':
 #   app.run(host='0.0.0.0', port=7776)