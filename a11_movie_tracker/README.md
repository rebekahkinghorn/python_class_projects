# Movie Watchlist Tracker
A Python class assignment that uses Peewee and SQLite to save and manage a movie watchlist.

## Features
- Add movies with their release years.
- View all saved movies.
- Mark movies as watched and give them a rating.
- View movies rated 4 or higher.
- Delete movies from the watchlist.

## Requirements
- Python 3
- Peewee

Install Peewee from your terminal:

pip install peewee

## Run
Open a terminal in this folder and enter:

python a11_movie_tracker.py

The program creates a `movies.db` file the first time it runs.
Your movie list is saved in that file between sessions.

## Notes
This assignment was written in 2024 and accepts release years
from 1889 through 2024. Enter numbers when prompted for numeric
input and use existing movie IDs when updating or deleting movies.
Invalid input may cause the program to stop.