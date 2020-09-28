#!/usr/bin/env python3
"""
Textdateien einlesen
====================
"""

print()
print('Im Ganzen')
print('=========')
# Datei im Ganzen einlesen
with open("haikus.txt", "r") as file:
    text = file.read()
    print(text)


print()
print('Zeilenweise')
print('===========')
# Datei öffnen und zeilenweise einlesen
with open("haikus.txt", "r") as file:
    for line in file:
        print(line)


print()
print('file.readlies')
print('=============')
# Datei öffnen und Zeilen als Liste verarbeiten
with open("haikus.txt", "r") as file:
    lines = file.readlines()
    print(lines)


print()
print('str.splitlines')
print('==============')

# Datei öffnenÖ
with open("haikus.txt", "r") as file:
    # Datei im Ganzen einlesen
    text = file.read()
    # Zeilen auftrennen
    lines = text.splitlines()

# Einzeln ausgeben, leerzeilen durch Deko ersetzen
for line in lines:
    print(line or "~~~~~~~~~")
