#!/usr/bin/env python3
"""
Modul: picture.orientation
==========================

Definiert Funktionen, um die Orientierung eines Bildes zu verändern.
"""
from PIL import Image


def rotate(image, degrees, clockwise=True):
    angle = degrees * (-1 if clockwise else 1)
    return image.rotate(angle, expand=True)


def flip_vertical(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)


def flip_horizontal(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)
