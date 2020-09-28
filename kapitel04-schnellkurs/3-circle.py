#!/usr/bin/env python3
"""
Ein etwas komplexeres Programm
"""

# Modul importieren
import math


# Eine Funktion
def circle_area(radius):
    '''Docstring'''
    area = math.pi * (radius ** 2)
    return math.ceil(area)


radius = 3
# Funktion aufrufen
area = circle_area(radius)

# Text formatiert ausgeben
print(f"Area(r={radius}): about {area}")
