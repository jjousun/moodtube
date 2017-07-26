import os
import spotipy
import sys
import spotipy.util as util
import logging
from dotenv import load_dotenv
import re
from models import db, Youtuber, Song

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# chunk all songs into 100 for spotify
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

my_songs = Youtuber.query.get(1).songs

chunked_songs = chunker(my_songs, 100)

def stringify_ids(object_list):
    output = ""
    for object in object_list:
        if object.spotify_id != "Null":
            output += object.spotify_id + ","
    return output

for chunk in chunked_songs:
    query_ids = stringify_ids(chunk)

    audio_features_search = sp.audio_features(query_ids)

    for result in audio_features_search:
        local_db_song = Song.query.filter_by(spotify_id=result["id"])

        for match in local_db_song:
            match.mood = result["valence"]
            print("My song = {0} query song = {1}".format(match.spotify_id, result["id"]))
            db.session.commit()
