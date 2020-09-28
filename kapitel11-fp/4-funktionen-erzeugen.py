#!/usr/bin/env python3
"""
Funktionen zusammenstecken
==========================

"""
import io
import sys


def muted(function):
    """
    Muted ist eine Funktion, die eine andere Funktion als Argument annimmt
    und eine weiter zurückgibt.
    """
    def wrapped(*args, **kwargs):
        old = sys.stdout
        sys.stdout = io.StringIO()
        try:
            result = function(*args, **kwargs)
        finally:
            sys.stdout = old

        return result
    return wrapped


def rot13_decrypt(cipher):
    """
    Funktion mit Seiteneffekt
    """
    print("rot13_decrypt brought to you by Schneider-Hofmeister-IT")
    import codecs
    return codecs.decode(cipher, 'rot_13')


# Die Funktion wird als Argument an Muted übergeben
decipher = muted(rot13_decrypt)


print(decipher("Gur Mra bs Clguba, ol Gvz Crgref\n"))
print(decipher("Ornhgvshy vf orggre guna htyl."))
print(decipher("Fvzcyr vf orggre guna pbzcyrk."))
