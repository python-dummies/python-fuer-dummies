#!/usr/bin/env python3
"""
Sydney
======

Prüft, wieviel Uhr es in Australien ist.

Hinweis: Mit der Sommerzeit nehmen wir es hier nicht so genau.

Heidelberg: https://de.wikipedia.org/wiki/UTC%2B1
Sydney: https://de.wikipedia.org/wiki/UTC%2B10
https://en.wikipedia.org/wiki/Central_European_Time
"""

import datetime


# Zeitverschiebung für Sydney
offset_heidelberg = datetime.timedelta(hours=2)

# Zeitzone für Heidelberg
germany = datetime.timezone(offset_heidelberg)

# Zeitverschiebung für Sydney
offset_sydney = datetime.timedelta(hours=10)

# Zeitzone für Sydney
australia = datetime.timezone(offset_sydney)

# Uhrzeit Heidelberg
time_heidelberg = datetime.datetime.now(germany)

# Uhrzeit Sydney
time_sydney = time_heidelberg.astimezone(australia)

# Uhrzeit ausgeben
print('Heidelberg:', time_heidelberg.strftime('%X %z %Z'))
print('Syndey:', time_sydney.strftime('%X %z %Z'))

# Kann ich Andy noch anrufen?
morning = datetime.time(9, 30)
evening = datetime.time(20, 00)

if morning < time_sydney.time() < evening:
    print('Andy is available!')
else:
    print('Andy is sleeping')
