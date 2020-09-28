#!/usr/bin/env python3
"""
Mehrere Listen zusammenführen -- nutzen Sie `zip`
"""

# Reißverschlussverfahren: Sie haben eine Liste mit Schlüsseln und eine mit
# Werten und wollen die Elemente paarweise ausgeben

# Vorbereitung
numbers = [1, 2, 3, 4, 5]
print('numbers:', numbers)
characters = ['a', 'b', 'c', 'd', 'e']
print('characters:', characters)


# Pythonic
merged = zip(numbers, characters)


# Ausgabe
# `merged` ist ein iterator:
print(merged)
print(list(merged))


# Nicht pythonic
result = []
assert len(numbers) == len(characters)
for i in range(len(numbers)):
    number = numbers[i]
    char = characters[i]
    pair = (number, char)
    result.append(pair)

# Ausgabe
print(result)
