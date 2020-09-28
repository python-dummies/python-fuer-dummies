#!/usr/bin/env python3
"""
consoleshop.py
==============

Wie Photoshop, nur für die Konsole. Diese Programm demonstiert einen
komplexeren Bild-Editor für die Kommandozeile. Das `picture`-Paket wird dabei
importiert.

Beispiel:

    $ python3 consoleshop.py --blur 5 --grayscale --rotate 90 bild.jpg

"""
from PIL import Image

# Modul zum Öffnen von Dateien
import pathlib

import picture

# Argparse ist ein Modul zum Einlesen von Kommandozeilenparametern
# Sie ist Teil der Standard-Bibliothek
import argparse


def apply_changes(image, arguments):
    """
    Wendet die gewünschten Änderungen auf das Bild an.
    """
    if arguments.resize:
        image = picture.resize(image, arguments.resize)

    if arguments.rotate:
        image = picture.rotate(image, arguments.rotate)

    if arguments.blur:
        image = picture.blur(image, arguments.blur)

    if arguments.grayscale:
        image = picture.grayscale(image)

    return image


def save_as_copy(image, filename, quality):
    """
    Speichert das veränderte Bild unter einem neuen Namen ab
    """
    path = pathlib.Path(filename)
    new_path = path.parent / f'{path.stem}-copy{path.suffix}'
    image.save(new_path, quality=quality)


def image_changes(arguments):
    """
    Interpretiert die gewünschten Bildänderungen aus den Argumenten der
    Kommandozeile.
    """

    # Operationen, die das Bild verändern
    CHANGES = {'blur', 'grayscale', 'resize', 'rotate'}

    # Parameternamen der übergebenen Argumente
    provided_parameters = {
        parameter
        for parameter, argument
        in vars(arguments).items()
        if argument
    }

    # Intersection
    return provided_parameters & CHANGES


if __name__ == '__main__':

    # Setup der Arguments des Scripts
    parser = argparse.ArgumentParser(description='Process an image')

    # Parameter für das eigentliche Bild
    parser.add_argument('image', help='The image to manipulate')

    # Bild weichzeichnen
    parser.add_argument('--blur', metavar='strength',
                        type=int, help='Blur the image')

    # Bild entsättigen
    parser.add_argument('--grayscale', action='store_true',
                        help='Convert the image to grayscale')

    # Größe ändern
    parser.add_argument('--resize', metavar='size', type=int,
                        help='Resize the image along its longest edge')

    # Bild drehen
    parser.add_argument('--rotate', metavar='degrees',
                        type=int, help='Rotate the image')

    # Qualität reduzieren
    parser.add_argument('--quality', metavar='quality',
                        type=int, default=75, help='Set the quality')

    # Argumente von der Kommandozeile einlesen
    arguments = parser.parse_args()

    # Bild öffnen
    with Image.open(arguments.image) as image:

        # Wenn keine Argumente angegeben wurden, dann passiert nichts.
        if not any(image_changes(arguments)):
            exit()

        # Wenn Argumente übergeben wurden, wird eine Kopie des Bildes
        # mit den gewünschten Änderungen angelegt
        image = apply_changes(image, arguments)
        save_as_copy(image, arguments.image, arguments.quality)
