#!/usr/bin/env python3
"""
Tupel
=====

Tupel funktionieren wie Listen, sind aber unveränderlich (engl.: "immutable").
"""

# Wie Listen, nur halt runte Klammern
group = (0, 1, 2)
print(group)

# Gemischtes Tupel
person = ('Johannes', 32, 1.90)
print(person)

# Auspacken
name, age, height = person
print('Name', name)
print('Alter', age)
print('Größe', height)

# Auspacken mit Stern
person = ('Johannes', 32, 1.90, 'Heidelberg', 'Python')
print(person)
head, *tail = person
print('Kopf: ', head)
print('Rest: ', tail)


# Tupel Vergleichen
# Yoga
head, *center, tail = (1, 2, 3, 4, 5)
print('Die innere Mitte: ', center)

print('Tupel vergleichen:')
print('(1, 2, 3) == (1, 2, 3)')
print((1, 2, 3) == (1, 2, 3))

print('(1, 2) < (1, 2, 3)')
print((1, 2) < (1, 2, 3))

print('(1, 2, 9) < (1, 4, 1)')
print((1, 2, 9) < (1, 4, 1))

print('Geburtstage:')
today = (10, 28)
birthday = (12, 6)
print('today < birthday')
print(today < birthday)


# Konvertieren
group = (0, 1, 2)
print('Liste: ', list(group))

items = [0, 1, 2]
print('Tupel: ', tuple(items))
