#!/bin/bash
rm -rf levelupapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations poppedapi
python3 manage.py migrate poppedapi
python3 manage.py loaddata flicks
python3 manage.py loaddata genres
python3 manage.py loaddata moods
python3 manage.py loaddata users
python3 manage.py loaddata flick_cast_crews
python3 manage.py loaddata flick_genres
python3 manage.py loaddata flick_moods
python3 manage.py loaddata flick_recommended_bys
python3 manage.py loaddata friend_requests
python3 manage.py loaddata friends
python3 manage.py loaddata user_flicks
python3 manage.py loaddata user_genres
