#!/usr/bin/env python3
"""
Iteration
=========

Betrachten Sie die Elemente einer Menge oder Sequenz nacheinander, ohne
einen Index zu benutzen.
"""

print()
print('Liste iterieren:')
for number in [1, 2, 3, 4, 5, 6]:
    print(number, end=' ')

print()
print()
print('String iterieren:')
for character in "Hello, World!":
    print(character, end=' ')

print()
print()
print('Schrittweise iterieren: Das was die for-Schleife macht')

# Iterierbares Objekt anlegen
numbers = [1, 2, 3, 4]
print('numbers:', numbers)

# Iterator erzeugen
iterator = iter(numbers)
print('Iterator:', iterator)

# Iterator abfragen
i = next(iterator)
print(i)

i = next(iterator)
print(i)

i = next(iterator)
print(i)

i = next(iterator)
print(i)

# Am Ende: StopIteration
print('Sobald der Iterator leer ist, wird ein Fehler ausgegeben:')
try:
    i = next(iterator)
except StopIteration:
    # Fehler auf der Konsole ausgeben
    # Das machen wir hier nur zu Demozwecken.
    # Das macht man normalerweise alles nicht, denn die for-Schleife
    # löst das viel eleganter. Wir fangen den Fehler ab und geben ihn aus,
    # Weil solche Ausnahme-Fehler sonst den Programmablauf unterbrechen.
    # Details finden Sie in Kapitel 13 - Ausnahmen
    import traceback
    traceback.print_exc()

# Abkürzung: Ranges
print()
print('Ranges:')
print('Range Objekte sind lazy:')
print(range(10))
print('Sie erzeugen Werte erst beim Iterieren:')
for i in range(10):
    print(i, end=' ')

print()
print('Verschiedene Ranges:')
# ... daher konvertieren wir sie hier in eine Liste, um sie anschaulich
# darzustellen:
# Hinweis: der erste Wert ist **inklusiv**, der letzte Wert ist **exklusiv**
# Alle Elemente von 0 - 9
print('       range(10):', list(range(10)))
# Jedes zweite Element von 0 - 20 (20 ist nicht mehr dabei)
print(' range(0, 20, 2):', list(range(0, 20, 2)))
# Rückwärts:
print('range(20, 0, -2):', list(range(20, 0, -2)))
