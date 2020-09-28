#!/usr/bin/env python3
"""
Textdateien zeilenweise schreiben
=================================
"""

from shutil import copyfile

lines = [
    "How strong is your wish",
    "That the crash took it all",
    "No backup remains?",
]

# Aufpassen: file.writelines fügt keine Zeilenenden hinzu, daher ist die
# Ausgabe in einer einzigen Zeile.
with open("a_haiku.txt", "w+") as file:
    file.writelines(lines)
    file.seek(0)
    print(file.read())


# Datei zurücksetzen, falls Sie das Beispiel häufiger ausführen möchten
with open("haikus.txt", "r") as source:
    with open("r_haikus.txt", "r+") as file:
        separator = "~~~"
        ruler = "-" * 34
        lines = source.read().splitlines()
        file.write('\n'.join(lines))
        file.seek(0)
        separated = [line or separator for line in lines]
        framed = [f"| {l:<30} |" for l in separated]
        decorated = [ruler, *framed, ruler]
        file.truncate(0)

        for line in decorated:
            file.write(f"{line}\n")

        file.seek(0)
        print(file.read())
