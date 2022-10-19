from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import sqlalchemy


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base


'''
Blueprints
'''
from thing1.thing1.api import api_blueprint
# from thing1._{module name}_ import _{blueprint}_
# ...

'''
This is the Flask app factory.
'''
def create_app(config_name='docker'):
    
    '''
    1. This is our Flask app object for our app factory
    '''
    app = Flask(__name__)
    
    
    '''
    2. Engine
    '''
    global engine
    
    if config_name == 'docker':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yet_another_leaked_credential@bouncycastle:3306/playground'
    elif config_name == 'pytest':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yet_another_leaked_credential@127.0.0.1:3306/playground'
    else:
        raise Exception("Invalid config_name specified for create_app(). Valid config_names are 'docker' and 'pytest'")
    engine = init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    
    
    '''
    3. For each BLUEPRINT, we'll import and then register it to our app.
    '''
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    return app



engine = None
db_session = scoped_session(lambda: create_session(bind=engine))
  
Base = declarative_base()



def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    
    return engine


def init_db():
    Base.metadata.create_all(bind=engine)