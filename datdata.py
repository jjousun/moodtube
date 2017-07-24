from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import *
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# for instances in db.session.query(Song).order_by(Song.id):
#     print(instances.id, instances.title, instances.mood)

def to_json():
    # response = json.dumps(response.text, sort_keys = True, indent = 4, separators = (',', ': '))
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)
    # response = df.dropna().to_json('data/songs.json', orient='records')
    data = df.dropna().to_json()
    return data
