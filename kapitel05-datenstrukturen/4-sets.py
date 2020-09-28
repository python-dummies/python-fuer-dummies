#!/usr/bin/env python3
"""
Sets
====

Sets speichern nur eindeutige Werte und vereinfachen Mengenoperationen,
wie das Bilden der Schnittmenge.
"""

students = {'Johannes', 'Horst', 'Lars', 'Horst', 'Kim'}
print(students)


# Uffbasse:
a = 1
b = 2
print('Aufgepasst:')
print("Set:  { a, b }:", {a, b}, type({a, b}))
print("Dict: { a: b }:", {a: b}, type({a: b}))


print('Dubletten entfernen:')
items = [2, 3, 4, 5, 1, 2, 3, 4]
print('Vorher:', items)
unique_items = set(items)
print('Nachher:', unique_items)


print('Mitgliedschaft prüfen:')
authors = {'Johannes', 'Horst'}
print('authors:', authors)
print("'Horst' in authors:", 'Horst' in authors)
print("'Igor' in authors:", 'Igor' in authors)


print('Hinzufügen')
colors = {'red', 'green', 'blue'}
print('Vorher:', colors)
colors.add('yellow')
print('Nachher:', colors)
# Beim zweiten Mal passiert nichts:
colors.add('yellow')
print('Nochmal:', colors)


print('Entfernen')
colors = {'red', 'green', 'blue'}
print('Vorher:', colors)
colors.remove('red')

# Alternativ: um Fehler zu vermeiden!
# colors.discard('red')
print('Nachher:', colors)


print()
print('Mengenlehre')
print('-----------')
print()

print('Schnittmenge:')
science_fiction = {'Alien', 'Blade Runner', 'Star Wars'}
print('Sci-Fi:', science_fiction)
horror = {'Insidious', 'Alien', 'Psycho'}
print('Horror:', horror)
print('science_fiction & horror:', science_fiction & horror)

print()
print('Vereinigungsmenge:')
scifi = {'Terminator', 'Blade Runner', 'Star Wars'}
print('Sci-Fi:', scifi)
action = {'Indiana Jones', 'Aliens', 'Terminator'}
print('Action:', action)
print('scifi | action:', scifi | action)


print()
print('Differenzmenge:')
dvds = {'Terminator', 'Blade Runner', 'Star Wars', 'Aliens'}
print('dvds:', dvds)
lent = {'Terminator', 'Star Wars'}
print('lent:', lent)
print('dvds - lent:', dvds - lent)


print()
print('Symmetrische Differenz:')
office = {'paperwork', 'pants'}
print('office:', office)
home = {'tv', 'pants'}
print('home:', home)
# Keine Hose, Kein Problem!
print('home ^ office:', home ^ office)


print()
print('Teilmenge:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('alphabet:', alphabet)
pangram = ('franz jagt im komplett verwahrlosten '
           'taxi quer durch bayern')
print('pangram:', pangram)
print('Teilmenge?:', set(alphabet) <= set(pangram))
