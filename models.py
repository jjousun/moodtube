from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

relationship_table=db.Table('relationship_table',
                             db.Column('youtuber_id', db.Integer,db.ForeignKey('youtuber.id'), nullable=False),
                             db.Column('song_id',db.Integer,db.ForeignKey('song.id'),nullable=False),
                             db.PrimaryKeyConstraint('youtuber_id', 'song_id') )

class Youtuber(db.Model):
    __tablename__ = "youtuber"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    songs=db.relationship('Song', secondary=relationship_table, backref='youtuber')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Song(db.Model):
    __tablename__ = "song"
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    spotify_id = db.Column('spotify_id', db.String)
    mood = db.Column('mood', db.Float)
    youtubers=db.relationship('Youtuber', secondary=relationship_table, backref='song' )

    def __init__(self, title):
        self.title = title
        self.spotify_id = None
        self.mood = None

    def __repr__(self):
        return '<id {}>'.format(self.id)
