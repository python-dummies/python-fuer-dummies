#!/usr/bin/env python3
"""
Input
=====

Texte von der Konsole einlesen
"""

prompt = "The mirror wants to know your name: "
name = input(prompt)
greeting = f"Hello, {name}!"

# Slicing Trick: Text umdrehen
print("The mirror says:", greeting[::-1])


print()
print('Mathe Trick')
print('-----------')
print()
print('           80 Bier')
print('      - dein Alter')
print('         + 40 Euro')
print('==================')
print('= Dein Geburtsjahr')
print()

biere = 80  # (*)
dein_alter = int(input('Dein Alter: '))
euro = 40
print('Geburtsjahr:', biere - dein_alter + euro)


# (*) Das ist natürlich Quatsch und funktioniert nur im Jahr 2020 ;)
