#!/usr/bin/env python3
"""
Die Standardbibliothek
======================

"""

# Das Betriebssystem
# ==================
import os
print('Sie verwenden', os.name)

# Genauer?
import platform
print('Sie verwenden', platform.system())
# Noch genauer?
print('Sie verwenden', platform.platform())
# Name?
print('Ihr Computer heißt', platform.node() )
# Architektur des Prozessors (kurz)
print('Ihr Prozessor ist ein', platform.machine())


# Details über den Prozessor
# ==========================
import multiprocessing
cores = multiprocessing.cpu_count()
print('Ihr Prozessor hat', cores, 'Kerne.')

if cores >= 16:
    print('Wow, das sind ganz schön viele Kerne!')
elif cores >= 12:
    print('Komme was wolle, Sie sind gerüstet!')
elif cores >= 8:
    print('Wow, das ist beeindruckend!')
elif cores >= 4:
    print('Stattlich!')
elif cores == 1:
    print('Puh, vielleicht sollten Sie über ein Upgrade nachdenken!')


# Verzeichnisse
# =============
from pathlib import Path
home = Path.home()
print('Ihr Heimverzeichnis liegt in', home)
try:
    owner = home.owner()
except NotImplementedError:
    # Unter windows geht `home.owner()` leider nicht
    owner = os.getenv('username')
print('Ihr Name ist offenbar', owner)

if os.name == 'nt':
    desktop = Path.home() / 'Desktop'
    example_file = desktop / 'example.txt'
    print(example_file)
    print('Gibt es sie schon?', example_file.exists())
    example_file.write_text('Hallo, wie gehts?')
    print('Jetzt ist sie da!', example_file.exists())
    example_file.unlink()
    print('Ist sie noch da?', example_file.exists())

