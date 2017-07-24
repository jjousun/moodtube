import os
import spotipy
import sys
import spotipy.util as util
import logging
from dotenv import load_dotenv
import re
from models import db, Youtuber, Song

# APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='',client_secret='')

my_songs = Youtuber.query.get(1).songs

for song in my_songs:
    try:
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        results = sp.search(q=song.title)

        spotify_id = results['tracks']['items'][0]['id']

        song.spotify_id = spotify_id
        db.session.commit()

    except IndexError: # This song could not be found in Spotify; set spotify_id to "Null"
        song.spotify_id = "Null"
        db.session.commit()
