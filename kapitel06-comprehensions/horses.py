#!/usr/bin/env python3
"""
Berühmte Rennpferde
===================

Übung zu Dictionary-Comprehensions.
"""

race_horses = {
    'Acatenango' : (1993, 2005),
    'Hoof Hearted' : (1973, 1978),
    'Seabiscuit' : (1933, 1947),
    'Anita Hanjab' : (1951, 1969),
    'Oil Beef Hooked': (1989, 1997),
    'Ben Timover': (1974, 1986),
    'Secretariat' : (1972, 1989),
    'Sea the Moon': (2014, 2020)
}

horse_years = {
    name: end - start
    for name,(start, end)
    in race_horses.items()
    if 1970 <= start <= 1980
}

print(horse_years)