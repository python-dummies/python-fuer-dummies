#!/usr/bin/env python3
"""
Modul: picture.orientation
==========================

Definiert eine Funktion zur Änderung der Bildgröße.
"""


def resize(image, size):
    """
    Verändert die Größe eines Bildes.
    Die lange Kante des Bildes wird auf die größe `size` begrenzt.
    """
    short_edge = min(image.size)
    long_edge = max(image.size)
    aspect_ratio = short_edge / long_edge

    width, height = image.size

    if height > width:
        # Porträt (Hochformat)
        width, height = int(size * aspect_ratio), size

    if width > height:
        # Landscape (Querformat)
        width, height = size, int(size * aspect_ratio)

    return image.resize((width, height))
