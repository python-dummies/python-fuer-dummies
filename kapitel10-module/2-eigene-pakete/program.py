#!/usr/bin/env python3
"""
program.py
==========

Dieses Programm demonstriert, wie Sie Funktionen aus einem eigenen Paket
importieren und aufrufen.
"""
from PIL import Image
from picture.color import grayscale

with Image.open('bild.jpg') as image:
    image = grayscale(image)
    image.save('bild-bw.jpg')
    # bild-bw.jpg beinhaltet nun sie Schwarz-weiße Version von bild.jpg
