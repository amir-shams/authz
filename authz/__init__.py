from flask import Flask                    #create web server
from flask_marshmallow import Marshmallow  #rabete beyne resource va model va controler 
from flask_migrate import Migrate          #convert db cod to table database 
from flask_restful import Api              #create rest
from flask_sqlalchemy import SQLAlchemy    #create orm
from authz.config import Config

db = SQLAlchemy()
ma = Marshmallow()
mg = Migrate()
api = Api()

# from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # load configs from env variables .
    db.init_app(app)
    ma.init_app(app)
    mg.init_app(app, db)
    api.init_app(app)
    return app
