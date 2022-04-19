import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
# a=find_dotenv("art_shop/.env") make sure the paths also exsist in the container, 
load_dotenv() #default: looks in project root 




def create_app(test_config=None):
    #creates and configures the app
   
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=f'{os.getenv("SECRET")}',
        SQLALCHEMY_DATABASE_URI=f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,

    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    print(os.getenv("DB_URI"))


    #@app.route('/')
    #def hello():
      #  return "hello"

    return app

