#!/usr/bin/env python3
"""
Funktionen zusammenstecken
==========================

Funktionen sind praktisch, um Programmen Struktur zu geben. Spannend wird es
wenn man Funktionen wie Variablen an andere Funktionen übergibt.
"""
import os
import sys



def zen():
    """
    Diese Funktion hat einen Seiteneffekt:
    Regulär aufgerufen, spuckt Sie das "Zen of Python" auf der Konsole aus
    """
    import this


def redirect(noisy_function, path):
    """
    Leitet die Standardausgabe während der Ausführung von
    `noisy_function` in die Datei `path` um.
    """
    with open(path, "w") as file:
        # Eine Referenz zum "echten" stdout behalten ...
        old = sys.stdout
        # stdout temporär umbiegen in eine Datei
        sys.stdout = file
        # Nun schreibt die gesprächige Funktion in eine Datei!
        noisy_function()
        # stdout zurückbiegen
        sys.stdout = old


# Um die Ausagbe zu unterdrücken, können Sie die Ausgabe in eine Datei umleiten
textfile = os.path.join(os.getcwd(), "zen.txt")
redirect(zen, textfile)

if os.path.exists(textfile):
    print("zen.txt geschrieben")
