import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import device_bp, video_bp, alarm_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath("./templates"))
    # app.config.from_object('config.Config') 

    # db.init_app(app) 
    # migrate.init_app(app, db) 

    app.register_blueprint(device_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(alarm_bp)

    return app