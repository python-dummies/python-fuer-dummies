#!/usr/bin/env python3
"""
Generatoren
===========

Generatoren sind Funktionen, die einen Generator-Iterator erzeugen.
Dafür gibt es eine eigene Syntax.
"""

# Eine return-Anweisung beendet die Ausführung der Funktion


def one_value():
    return 1


# Aufruf wie gehabt
print(one_value())


# Das Auftauchen einer yield-Anweisung macht aus einer Funktion
# einen Generator.
def two_values():
    yield 1
    yield 2


# Beim Aufruf der Funktion erzeugt sie einen Iterator.
print(two_values())

# Der Iterator kann wie gewohnt verwendet werden
for v in two_values():
    print(v)


# Generatoren können theoretisch unendlich lange Objekte produzieren
def count(start=1):
    while True:
        yield start
        start += 1


## Das sollten Sie vermeiden
# for i in count():
#   print(i, end=' ')

# Das ist ok. Die zip bricht ab, sobald der Iterator für den String
# leer ist, daher läuft diese Iteration nicht unendlich lange.
for number, letter in zip(count(start=10), 'abcd'):
    print(number, letter)
