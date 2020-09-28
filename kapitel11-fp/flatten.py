#!/usr/bin/env python3
"""
Rekursive Generatoren
=====================

Durch rekursives Aufrufen von Generatoren lassen sich verschachtelte
Strukturen flach ausgeben.
"""


def flatten(tree):
    # Wenn das Argument eine Liste ist,
    # dann sollen die Elemente einzeln ausgegeben werden
    if isinstance(tree, list):
        for branch in tree:
            # `yield from` iteriert die Elemente
            # und gibt sie einzeln zurück
            yield from flatten(branch)
    else:
        # Wenn es sich um ein einzelnes Element handelt,
        # wird es direkt zurückgegeben
        yield tree


# Eine Verschachtelte Struktur
tree = [
    1,  [2, 3, 4, [5, 6]], [7, 8], 9
]

# Der verschachtelte `tree` kann wie eine flache Liste iteriert werden
for value in flatten(tree):
    print(value, end=' ')
