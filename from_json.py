# -*- coding: utf-8 -*-
import os
import json
import pprint
import re
from models import db, Youtuber, Song

me = Youtuber.query.get(1)

for file in os.listdir("./data/raw"):
    try:
        with open('./data/raw/' + file) as data_file:
            data = json.load(data_file)

        if data['categories'] == ['Music']:
            my_video = {
            'title': data['title'],
            }
            title = my_video['title']

            my_video["title"] = re.sub("[\(\[].*?[\)\]]", "", title)

            words = my_video["title"].split()

            for ch in ["lyrics", "LYRICS", "Lyrics", "ft.", "ft", "FT", "FT.", "Ft.", "Ft", "FEAT.", "FEAT", "featuring", "Featuring", "FEATURING", "HQ", "HD"]:
                if ch in words:
                    words.remove(ch)

            my_video["title"] = " ".join(words)

            my_video["title"] = re.sub(',','', my_video["title"])

            new_song = Song(title = my_video["title"])
            db.session.add(new_song)
            db.session.commit()
            me.songs.append(new_song)

    except:
        print("This song didn't work: {0}".format(my_video["title"]))
