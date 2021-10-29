
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from flask_migrate import Migrate
from dotenv import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5432/wordcount_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import *

@app.route('/')
def home():
    return "Yo, how you doing?"

@app.route('/<name>')
def hello_name(name):
    return "Yo, {}!".format(name)

#if __name__ == "__main__":
    #app.run(debug=True)
