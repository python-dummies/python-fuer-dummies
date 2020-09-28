#!/usr/bin/env python3
"""
Quicksort
=========

Syntax-Angeberei. Hier werden List-Comprehensions geschickt verwendet,
um den Quicksort-Algorithmus naiv umzusetzen. Nutzen Sie in der Praxis aber
bitte `list.sort()`.


Hinweis
-------

Im Buch haben wir leider einen Fehler gemacht:
Dort steht a < pivot -- Dadurch werden doppelte Einträge entfernt.
Ist auch nur ein Beispiel -- Sie sollen ja eigentlich den Timsort verwenden.
Vielen Dank an Volker Lueg, der den Fehler bemerkte.
"""

# Modul für Pseudozufallszahlen
import random


def quicksort(numbers):
    if not numbers:
        return []
    pivot, *numbers = numbers
    left = [a for a in numbers if a <= pivot]
    right = [a for a in numbers if a > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


# Zufallszahlen erzeugen
random_numbers = [random.randint(0, 100) for _ in range(10)]

# Unsortiert ausgeben
print(random_numbers)

# Sortiert ausgeben
print(quicksort(random_numbers))
