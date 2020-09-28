#!/usr/bin/env python3
"""
Container Konvertieren
======================

Listen, Tupel, Dicts und Sets können hin- und herkonvertiert werden.
"""

print()
print('Tupel in Liste konvertieren')
print('---------------------------')
tupel = (1, 2, 3)
liste = list(tupel)
print(tupel, '-->', liste)


print()
print('Dictionary in Tupel konvertieren')
print('--------------------------------')
dictionary = {'a': 1, 'b': 2}
print('Keys:')
# Hinweis: Die Konversion iteriert das Objekt.
# Iterierte Dictionaries geben nur die Schlüssel zurück.
tupel = tuple(dictionary)
print(dictionary, '-->', tupel)


print()
print('Items:')
# Schlüssel und Werte iterieren
items = tuple(dictionary.items())
print(dictionary, '-->', items)


print()
print('Tupel in Dictionary konvertieren')
print('--------------------------------')
coordinates = [('x', 1), ('y', 2), ('z', 3)]
vector = dict(coordinates)
print(coordinates, '-->', vector)


print()
print('Übrigens: Leere Container')
print('-------------------------')
print('list() -->', list())
print('dict() -->', dict())
print('tuple() -->', tuple())
print('set() -->', set())


print()
print('Eigentlich: Konstruktoren')
print('-------------------------')
# Eigentlich sind list, dict, tuple und set nicht nur Funktionen,
# sondern sog. Konstruktoren, also Funktionen, die Objekte eines bestimmten
# Typs erstellen.
print('type(list) -->', type(list))
numbers = [1, 2, 3]
print('numbers:', numbers)
print('isinstance(numbers, list):', isinstance(numbers, list))

