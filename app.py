#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from models import Song
from flask import Flask, request, render_template, jsonify
# from stock_scraper import get_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello World!"
    # return "Method used: %s" % request.method
    return render_template("index.html", request=request.method)

# @app.route('/tuna')
# def tuna():
#     return '<h2>Tuna is good</h2>'

if __name__ == '__main__':
    app.run(debug=True) #remove this option for production
