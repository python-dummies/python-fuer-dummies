#!/usr/bin/env python3
"""
Taschenrechner
==============

Kleiner Taschenrechner für die Kommandozeile.
Beispiel:

 $ python3 calc.py 10 + 20 * 30 - 20
"""
import sys

arguments = ' '.join(sys.argv[1:])

# Nur gültige Zeichen auswählen und neuen String zusammenstellen
command = ''.join(c for c in arguments if c in '1234567890. +-/*()')

# Befehl wiederholen
print(command)

# Ergebnis auswählen
print(f'= {eval(command)}')

# Vorsicht mit Eval. Für diese Spielerei ist das ok, aber der Befehl
# kann sehr gefährlich sein.
