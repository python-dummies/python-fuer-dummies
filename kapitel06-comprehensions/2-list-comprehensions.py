#!/usr/bin/env python3
"""
List Comprehensions
===================

Beschreiben Sie Datentransformationen mit einer eleganten Syntax.
Das Ergebnis ist eine Liste.
"""


numbers = range(10)
print('numbers:', numbers)


# Selektion: Daten filtern
print('Gerade Zahlen:')
even = [number for number in numbers if number % 2 == 0]
print(even)


# Projektion: Ergebnis mit Operatoren verändern
print('Zweierpotenzen:')
squares = [2**exponent for exponent in numbers]
print(squares)


# Projektion: Funktionen aufrufen
print('Über einen String iterieren und Funktionen aufrufen:')
name = 'Annie Easley'
# Amerikanische Raketenwissenschaftlerin
# https://de.wikipedia.org/wiki/Annie_Easley
print('name:', name)
consonants = [c.upper() for c in name.lower() if c not in 'aeiou']
# Ergebnis ist eine Liste:
print(consonants)
# Aus einer Buchstaben-Liste einen String machen:
print(''.join(consonants))
# (Das ist so eine Art "Redewendung" (ein Idiom) in der Python-Welt
# - das muss man sich halt merken).


# Verschachtelte Comprehensions
# "Vorname Nachname" tauschen in "Nachname, Vorname"
print()
print('Verschachtelt:')
names = [
    'Annie Easley',
    'Margaret Hamilton',
    'Barbara Liskov',
]

print('names:', names)
lastname_firstname = [
        f'{last}, {first}'
        for first, last in [
            name.split(' ') for name in names
        ]
]

print('lastname_firstname', lastname_firstname)


print()
print('Party-Zauberei:')
# Unfug: Quicksort
def quicksort(numbers):
    if not numbers:
        return []
    pivot, *numbers = numbers
    # Im Buch haben wir leider einen Fehler gemacht:
    # Dort steht a < pivot -- Dadurch werden doppelte Einträge entfernt.
    left = [a for a in numbers if a <= pivot]
    right = [a for a in numbers if a > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

import random
# 10 Zufallszahlen zwischen 0 und 100 (bei Randint ist die Obergrenze inklusiv)
random_numbers = [random.randint(0, 100) for _ in range(10)]
print('random_numbers:', random_numbers)

# Sortieren:
print('      Sortiert:', quicksort(random_numbers))
