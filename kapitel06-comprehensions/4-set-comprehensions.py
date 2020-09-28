#!/usr/bin/env python3
"""
Set Comprehensions
==================

Beschreiben Sie Datentransformationen mit einer eleganten Syntax.
Das Ergebnis ist ein Set (eine Menge mit eindeutigen Elementen).
"""


numbers = [8, 1, 10, 2, 4, 1, 4, 4, 10, 5]
print('numbers:', numbers)

# Projektion: Ein Set (Schweifklammern)
# Selektion: Alle Zahlen kleiner 5
small_unique = {i for i in numbers if i < 5}

# Nur eindeutige Zahlen vorhanden:
print('small_unique:', small_unique)


# Radio Playlist:
playlist = '''R.E.M. - Man on the Moon
R.E.M. - Losing my Religion
Bon Jovi - Living on a Prayer
Phil Collins - Another Day In Paradise
Phil Collins - In the Air Tonight
Pet Shop Boys - West End Girls'''

playlist = [
    line.split(' - ')
    for line
    in playlist.split('\n')
]

unique_artists = {
    artist for artist, song in playlist
}

print(unique_artists)

diversitaet = len(unique_artists) / len(playlist)
# Je kleiner dieser Wert, desto langweiliger der Radiosender.
print("Musikalische Diversität:", diversitaet)
# Fun fact: Die Adult-Contemporary Sender rund um Heidelberg
# haben einen Wert von etwa .20!
