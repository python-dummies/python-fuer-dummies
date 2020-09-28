#!/usr/bin/env python3
"""
Eine Liste mit gepaarten Elemente in ein Dictionary verwandeln
"""

# Sie haben eine Liste mit Schlüsseln und eine mit Werten und
# wollen daraus ein Dict machen

# Vorbereitung
names = ['Mareike', 'Marion', 'Kim']
print('names:', names)
ages = [27, 43, 19]
print('ages:', ages)


# Pythonic
people = dict(zip(names, ages))


# Ausgabe
print(people)


# Nicht pythonic
people = {}
for i in range(len(names)):
    people[names[i]] = ages[i]

# Ausgabe
print(people)
