#!/usr/bin/env python3
"""
Textdateien als Argument übergeben
==================================

Beispiel:

 $  python3 chars.py haiku.txt

"""
import sys

# Wir wollen nur an den zweiten Parameter des Programms
script, path, *_ = sys.argv

# Die Datei wird geöffnet und gelesen
with open(path) as file:
    # Den Text komplett einlesen
    text = file.read()

    # Buchstaben einlesen und in Kleinbuchstaben konvertierten.
    # Leerzeichen ignorieren
    characters = (c.lower() for c in text if not c == ' ')

    # Buchstaben hintereinaner ausgeben
    for character in characters:
        print(character, end=' ')
