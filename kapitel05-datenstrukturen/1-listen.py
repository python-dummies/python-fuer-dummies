#!/usr/bin/env python3
"""
Listen
======

Listen sind wohl der wichtigste Datentyp.
"""

# Liste mit Ganzzahlen
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Liste mit Kommazahlen
heights = [1.95, 1.75]


# Liste mit Strings
authors = ['Horst', 'Johannes']


# Verschachtelt
triangle = [
    [0.0, 1.0],
    [1.0, 0.0],
    [0.0, 0.0],
]


# Länge bestimmen
print('Länge von `numbers`: ', len(numbers))


# Einträge suchen
grades = [1, 2, 2, 3, 4, 3, 2, 1]
print('Schlechter Schüler?', 6 in grades)
print('Guter Schüler?', 1 in grades)
print('Klausuren geschrieben', len(grades))
print('Gute Klausuren', grades.count(2))


# Listen manipulieren - Hinzufügen
pasta = ['Spaghetti', 'Fusilli']
print(pasta)
pasta.append('Penne')
print('Hinzugefügt:', pasta)


# Listen manipulieren - Hinzufügen
pasta = ['Rigatoni', 'Maccheroni']
small_pasta = ['Fusilli', 'Farfalle']
pasta.extend(small_pasta)
print('Erweitert:', pasta)


# Listen manipulieren - Entfernen
pasta.remove('Farfalle')
print('Entfernt: Farfalle', pasta)

print()
print('Ob Bett kaputt oder Nudeln runtergefallen: Penne heute auf dem Boden.')
print()
# Bonus: Nach diesem Kalauer sollten Sie sich ein "Ba Dum Tss!"-Tusch anhören
#
# import browser
# browser.open('https://www.youtube.com/watch?v=6zXDo4dL7SU')

# Sortieren
print('Sortieren')
lengths_cm = [8.99, 4.5, 10.8, 3.95, 4.0, 2.3, 2.0]
print('Kraut und Rüben:', lengths_cm)
lengths_cm.sort()
print('Ordnung: ', lengths_cm)
# Oder aber:
# print('Odgnnru: ', sorted(lengths_cm))

lengths_cm = [8.99, 4.5, 10.8, 3.95, 4.0, 2.3, 2.0]
print('gnundrO: ', sorted(lengths_cm, reverse=True))
