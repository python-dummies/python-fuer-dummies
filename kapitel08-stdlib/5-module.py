#!/usr/bin/env python3
"""
Module importieren
==================

Imports dürfen überall stehen, wo ein Statement erlaubt ist.
Normalerweise parkt man sie am Anfang einer Python-Datei.
"""

# Einfacher Import des Moduls
import datetime

# Aufruf einer Funktion
print(datetime.datetime.now())

# Imporieren der Objekte datetime, date
# Aufgepasst, das Objekt `datetime` heißt genau wie das Modul.
# Beim Import `from datetime import datetime` verweist der Name
# `datetime` auf die Klasse, nicht auf das Modul!
from datetime import datetime, date
today = date.today()
print('Heute ist ', datetime.strftime(today, '%A, %d. %B %Y'))

# Beim Importieren kann es zu Namenskonflikten kommen:
from datetime import time
from time import time
print(time())

# Aliases anlegen mit from ... import .. as
from datetime import time as time_of_day
from time import time as timestamp

print(time_of_day(12, 45))
print(timestamp())

# Import mit Wildcard:
from textwrap import *
long_text = 'Dieser Text ist eindeutig zu lang!'
# Shorten ist als `textwrap.shorten` definiert
short_text = shorten(long_text, width=24, placeholder=' ...')
print(short_text)