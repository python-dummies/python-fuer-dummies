#!/usr/bin/env python3
"""
Dekoratoren
===========

Dekoratoren sind normale Funktionen, die aber eine Funktion als Argument
annehmen und eine andere Funktion zurückgeben.

Um Sie anzuwenden gibt es eine eigene Syntax mit @.
"""
import random


def count(function):
    """
    Dekoriert eine Funktion, sodass ihre Aufrufe gezählt werden.
    """

    # Innere Funktion mit allgemeiner Signatur
    def wrap(*args, **kwargs):
        # Hochzählen pro Aufruf
        wrap.counter += 1

        # Aufruf der ursprünglichen Funktion
        return function(*args, **kwargs)

    # Zähler initialisieren
    wrap.counter = 0

    # Innere Funktion zurückgeben
    return wrap


# Die Funktion roll mit count "dekorieren"
@count
def roll():
    return random.randint(1, 6)


# Würfeln, bis eine 6 kommt
pips = 0
while pips != 6:
    pips = roll()
    print(pips)

print(f'Roll called {roll.counter} times')
