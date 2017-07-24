#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import *
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_pyfile('config.py')
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
    # return "Hello World!"
    # return "Method used: %s" % request.method
    dataset=[5, 6, 23, 1, 7]
    return render_template("index.html", request=request.method, data=dataset)

@app.route('/db')
def df_from_files():
    # all_songs = db.session.query(Song).order_by(Song.id)
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)
    # df = pd.read_sql_table(Song)
    # for row in all_songs:
    #     # return '<br>'.join(str(row) for row in rows)
    #     # print(instances.id, instances.title, instances.mood)
    #     all_songs.append(row)

    # return '<p> %s' % all_songs
    # return jsonify(all_songs)
    testtest = df.dropna().to_html
    return render_template("test.html", tables=[testtest(classes='all_songs_ordered')], titles=['All My Songs in Order'])

@app.route('/json')
def to_json():
    # response = json.dumps(response.text, sort_keys = True, indent = 4, separators = (',', ': '))
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)
    response = df.dropna().to_json()
    return render_template("json.html", response=response)

@app.route('/graph')
def make_graph():
    # response = json.dumps(response.text, sort_keys = True, indent = 4, separators = (',', ': '))
    df = pd.read_sql(db.session.query(Song).order_by(Song.id).statement, db.session.bind)
    # response2 = df.dropna().to_json()
    response2 = df.dropna()
    # response2 = response2.values.T.tolist()
    response2 = response2.to_dict('records')
    print(response2)
    return render_template("graph.html", data=response2)

if __name__ == '__main__': # Erica separated this into a file called run.py
    app.run(debug=True) #remove this option for production
