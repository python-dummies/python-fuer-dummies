#!/usr/bin/env python3
from pathlib import Path
"""
Praktische Builtins
===================

"""


print('Mathe')
print('=====')
print('    abs(-49.95):', abs(-49.95))
print('round(3.141592):', round(3.141592))
print('   pow(2, 8, 7):', pow(2, 8, 7))
print('   divmod(8, 5):', divmod(8, 5))


print()
print('Mengen aggregieren')
print('==================')
print("     len('Python'):", len('Python'))
print("    len([1,2,3,4]):", len([1, 2, 3, 4]))
print("len(range(0,10,2)):", len(range(0, 10, 2)))
print(" sum([1,2,3,4,5]):", sum([1, 2, 3, 4, 5]))
print("min(10, 9, 5, 12):", min(10, 9, 5, 12))
print("  max(5, 6, 3, 1):", max(5, 6, 3, 1))


print()
print('all und any')
print('-----------')

privates = (path.name.startswith('.') for path in Path.home().iterdir())

# Wahrscheinlich True
print('Any private files?', any(privates))

# Wahrscheinlich False
print('All private files?', all(privates))


print()
print('Map, Filter')
print('===========')


print()
print('Map:')


def square(number):
    return number * number


numbers = [1, 2, 3, 4]
squares = map(square, numbers)
print('Map:', squares)
# Hinweis: Maps sind lazy. Erst beim iterieren transformieren sie die Daten
print(list(squares))

print()
print('Filter:')


def five_or_more(value):
    return value >= 5


iterable = range(10)
upper_half = filter(five_or_more, iterable)
print('Filter:', upper_half)
# Hinweis: Filter sind lazy. Erst beim iterieren transformieren sie die Daten
print(list(upper_half))


print()
print('Zip')
print('===')


characters = 'abcde'
digits = '12345'
pairs = zip(characters, digits)
print(f"characters:", characters)
print(f"digits:", digits)

print('Zip:', pairs)
# Hinweis: Zips sind lazy. Erst beim iterieren transformieren sie die Daten
# Wie hier beim String-Join
string = ''.join([f'{char}{digit}' for char, digit in pairs])
print(string)

print()
print('Als Dict:')
keys = 'abcde'
values = '12345'
print(f"keys:", keys)
print(f"values:", values)
# Solche Listen mit Paar-Tupeln darin lassen sich hervorragend
# In Dictionarys umwandeln.
print(dict(zip(keys, values)))
