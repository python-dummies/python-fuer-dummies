#!/usr/bin/env python3
"""
Paket: picture
==============

Um Python-Code aus einem Ordner zu importieren, muss er eine Datei namens
`__init__.py` beinhalten. Diese definiert ein Paket. Um die Benutzung zu
vereinfachen, importiert man in der Hauptdatei __init__.py gewünschte
Objekte aus den Untermodulen.
"""
from .color import grayscale
from .blur import blur
from .orientation import rotate, flip_horizontal, flip_vertical
from .size import resize
