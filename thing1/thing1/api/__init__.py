'''
This is a BLUEPRINT
'''

from decimal import Decimal
from flask import Blueprint, Flask, jsonify, request, render_template
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
    df = pd.read_sql_query('select * from marks', thing1.thing1.engine)
    return df[df.student_id == student_id].to_json()



'''
This is for bulk upload
params:
    json
    {
        course_id {
            (student_id, assignment_id, marks, date),
        }
    }
'''
@api_blueprint.route('/bulk_upload', methods=['POST'], strict_slashes=False)
@cross_origin()
def route_bulk_upload():
    
    d = dict(request.json)

#    for l in json_list:
#        d = dict(l)
    ext_course_id = d['class_sis_id']
    course_name = d['class_name']
    teacher_name = d['teacher_name']
    students_dict = list(d['students'])
    
    # Teacher
    with thing1.thing1.engine.connect() as conn:
        meta = MetaData(thing1.thing1.engine)
        teacher_tbl = Table('teacher', meta, autoload=True, autoload_with=thing1.thing1.engine)
        sql = teacher_tbl.insert().values(teacher_name=teacher_name)
        conn.execute(sql)
    
        # todo vulnerability
        df = pd.read_sql_query(f'select teacher_id from teacher where teacher_name = "{ teacher_name }"', thing1.thing1.engine)
        new_teacher_id = int(df['teacher_id'][0])
    
    # Course
    with thing1.thing1.engine.connect() as conn:
        meta = MetaData(thing1.thing1.engine)
        course_tbl = Table('course', meta, autoload=True, autoload_with=thing1.thing1.engine)
        sql = course_tbl.insert().values(ext_course_id=ext_course_id, course_name=course_name, teacher_id=new_teacher_id)
        conn.execute(sql)

        # todo vulnerability
        df = pd.read_sql_query(f'select course_id from course where ext_course_id = "{ ext_course_id }"', thing1.thing1.engine)
        new_course_id = int(df['course_id'][0])


    # Student
    for s in students_dict: #list
        print(s['sis_id'])
        ext_student_id = int(s['sis_id'])
        student_name = s['name']
        with thing1.thing1.engine.connect() as conn:
            meta = MetaData(thing1.thing1.engine)
            student_tbl = Table('student', meta, autoload=True, autoload_with=thing1.thing1.engine)
            sql = student_tbl.insert().values(ext_student_id=ext_student_id, student_name=student_name)
            conn.execute(sql)
            
            # Student Enrollment

            # todo vulnerability
            df = pd.read_sql_query(f'select student_id from student where ext_student_id = "{ ext_student_id }"', thing1.thing1.engine)
            new_student_id = int(df['student_id'][0])

            enrollment_tbl = Table('enrollment', meta, autoload=True, autoload_with=thing1.thing1.engine)
            sql = enrollment_tbl.insert().values(student_id=new_student_id, class_id=new_course_id)
            conn.execute(sql)

    return ''







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
    
    with thing1.thing1.engine.connect() as コネ:
        メタ = MetaData(thing1.thing1.engine)
        marks_tbl = Table('marks', メタ, autoload=True, autoload_with=thing1.thing1.engine)
        
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