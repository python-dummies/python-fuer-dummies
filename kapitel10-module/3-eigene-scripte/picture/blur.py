#!/usr/bin/env python3
"""
Modul: picture.blur
===================

Definiert eine Funktion zum Weichzeichnen eines Bildes.
"""
from PIL import ImageFilter


def blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius=radius))
