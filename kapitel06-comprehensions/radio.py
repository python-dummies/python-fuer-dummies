#!/usr/bin/env python3
"""
Radio Playlist
==============

Übung zu List-, Dictionary-, und Set Comprehensions.
"""

playlist = '''
R.E.M. - Man on the Moon
R.E.M. - Losing my Religion
Bon Jovi - Living on a Prayer
Phil Collins - Another Day In Paradise
Phil Collins - In the Air Tonight
Pet Shop Boys - West End Girls
'''

# Playlist zeilenweise auftrennen
# Zeilen am Bindestrich aufgrennen
rotation = [
    line.split(' - ')
    for line
    in playlist.split('\n')
    if line
]

unique_artists = {
    artist for artist, song in rotation
}

print(unique_artists)
