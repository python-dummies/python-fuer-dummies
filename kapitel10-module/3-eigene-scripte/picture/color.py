#!/usr/bin/env python3
"""
Modul: picture.color
====================

Definiert eine Funktion, die ein Bild entsättigt.
"""


def grayscale(image):
    '''
    Das Bild ändert den Farbmodus in LA. Dadurch gehen die Farbinformationen
    verloren. Um das Bild als JPG oder PNG zu speichern, muss es in den RGB Modus konvertiert werden
    '''
    return image.convert('LA').convert('RGB')
