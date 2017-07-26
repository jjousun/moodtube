#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from dotenv import load_dotenv
from models import *
import pandas as pd
from sqlalchemy import create_engine, desc
app = application

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config.from_object('config')
db = SQLAlchemy(app)

# #load dotenv in the base root
# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)
# # where you're going to use the environmental variables, first import os
# # then os.environ['SPOTIFY_CLIENT_ID'] to access that key/value you want

# db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", request=request.method)

@app.route('/db')
def df_from_files():
    # df = pd.read_sql(db.session.query(Song).order_by(desc(Song.id)).statement, db.session.bind)
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)

    testtest = df.dropna().to_html
    return render_template("test.html", tables=[testtest(classes='all_songs_ordered')], titles=['All My Songs in Order'])


@app.route('/json')
def to_json():
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)
    response = df.dropna().to_json()
    return render_template("json.html", response=response)

@app.route('/graph')
def make_graph():
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)
    response2 = df.dropna()
    response2 = response2.to_dict('records')

    # print(response2)

    df = pd.read_csv('./data/bottom_moods.csv')
    downers = df.to_html

    df = pd.read_csv('./data/top_moods.csv')
    uppers = df.to_html

    return render_template("graph.html", data=response2, tables=[downers(classes='lowest_valences'),uppers(classes="highest_valences")], titles=['','Lowest Moods Songs','Highest Moods Songs'])

if __name__ == '__main__': # Erica separated this into a file called run.py
    app.run(debug=False) #remove this option for production
