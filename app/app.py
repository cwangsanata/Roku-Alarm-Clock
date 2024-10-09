import os
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

from app import create_app
from . import schedule_runner

app = create_app()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    schedule_runner.run()
    app.run(debug=True)