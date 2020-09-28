#!/usr/bin/env python3
"""
Konsolen-Explorer
=================

Demonstiert die Verwendung der pathlib.
Listet Dateien in einem Verzeichnis `path`, ähnlich wie der Befehl `ls -l`.

Beispiel:

 $ python3 explore.py '/home/johannes'

Sortierung nach Größe:

 $ python3 explore.py '/home/johannes' --size

Sortierung nach Änderungsdatum:

 $ python3 explore.py '/home/johannes' --size

"""
import sys
import stat
import itertools
from datetime import datetime
from pathlib import Path

# Script-Namen verwerfen (`explore.py`)
script, *args = sys.argv

if args and Path(args[0]).is_dir():
    directory = Path(args[0])
else:
    # Wenn Sie kein Verzeichnis zum Durchsuchen angeben,
    # wird das aktuelle verwendet
    directory = Path.cwd()

def describe(path):
    '''
    Listet die Dateien im Verzeichnis `path`, ähnlich wie der
    Befehl `ls -l`, z.B.:

        -rwxrwxr-x  20 johannes www-data    4096 2019-12-12 book.pdf

    '''
    print(
        # Dateirechte
        # z.B. -rwxrwxr-x
        stat.filemode(file.stat().st_mode),
        # Anzahl an Links auf die Datei
        # z.B.  20
        format(file.stat().st_nlink, '>3'),
        # Größe (in bytes)
        # z.B.    4096
        format(file.stat().st_size, '>10'),
        # Änderungsdatum
        # z.B. 2019-12-12
        datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d'),
        # Dateiname
        # z.B. book.pdf
        file.name
    )


def by_name(file):
    return file.name.lower()


def by_size(file):
    return file.stat().st_size


def by_date(file):
    return file.stat().st_mtime


# Sortierreihenfolge feststellen
order_by = (
    by_size if '--size' in args else
    by_date if '--date' in args else
    by_name
)


# Dateien sortieren
paths = sorted(directory.iterdir(), key=order_by)

# Verzeichnisse von Dateien trennen
directories = (file for file in paths if file.is_dir())
files = (file for file in paths if file.is_file())


# Verzeichnisse werden VOR den Dateien ausgegeben.
# Hier werden Iteratoren verkettet, um sie in einer einzigen for-Loop
# zu durchlaufen.
for file in itertools.chain(directories, files):
    describe(file)