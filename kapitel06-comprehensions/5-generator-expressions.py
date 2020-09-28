#!/usr/bin/env python3
"""
Generator Expressions
=====================

Beschreiben Sie Datentransformationen mit einer eleganten Syntax.
Das Ergebnis ist ein Generator, der Daten erst beim Iterieren transformiert.
"""

generator = (i**i for i in range(100))
print('generator:', generator)

# Mit eckigen Klammern wirds eine Liste
list_comprehension = [i**i for i in range(10)]
print('list_comprehension:', list_comprehension)

print('Summe:', sum(generator))



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Generator Expressions können in vielen Fällen
# ohne zusätzliche Klammerung an eine Funktion
# übergeben werden:
largest = max(i for i in numbers if not i % 2)
print('largest:', largest)

smallest = min(i for i in numbers if not i % 2)
print('smallest:', smallest)


print()
print('All')
# Mit all prüfen Sie, ob ein Ausdruck für alle Werte einer Menge zutrifft
grades = [4, 1, 4, 3, 2, 2]
print('grades:', grades)
print('Sind alle Noten kleiner als 5?', all(grade < 5 for grade in grades))
print('Sind alle Noten größer 1?', all(grade > 1 for grade in grades))


print()
print('Any')
# Mit any prüfen Sie, ob mindestens ein Ausdruck für die Werte einer Menge
# zutrifft
names = [
    'Annie Easley',
    'Margaret Hamilton',
    'Barbara Liskov',
]

print('names:', names)
does_any_name_start_with_A = any(name.startswith('A') for name in names)
print('A...:', does_any_name_start_with_A)
does_any_name_start_with_F = any(name.startswith('F') for name in names)
print('F...:', does_any_name_start_with_F)
