# moodtube

This app allows a user to analyze the mood of a user's music-related YouTube Watch History. 
Displays an interactive graph and two charts in the browser.

Inspiration from youtube-history. Flask 0.12.2, written in Python 3.6 with d3.js data visualization and a PostgreSQL database. Uses youtube-dl, spotipy.

A working version of this app can be found here: (moodtube)[moodtube.org/graph]

## Installation
Clone this repo into a project folder you created locally.

You will need to get Spotify secret keys to plug into this app: https://developer.spotify.com/web-api/authorization-guide/

Set up a virtualenv:
 
`$ python3 -m venv pickanynameforyourvirtualenvhere`

Install Python 3.6 and pip if you don't have them already.

Install dependencies by running:

`$ pip install -r requirements.txt`

Activate your virtual environment: 

`$ source ./bin/activate`

Scrape YouTube Watch history by running:

`$ python3 youtube_history.py`

Set up your local database in the interactive Python shell:

`$ from yourapplication import db`
`$ db.create_all()`

Start your local server:

`$ python3 application.py`

To see the project, point your browser to: "http://127.0.0.1:5000/"

## Notes
This app is a student project for the Ada Developers Academy's capstone requirement. There are still features to be implemented and bugs to fix. 
