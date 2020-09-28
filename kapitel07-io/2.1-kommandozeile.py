#!/usr/bin/env python3
"""
Kommandozeilenparameter
=======================

Daten beim Aufruf des Programms übergeben
"""

import sys
# Rufen Sie dieses Programm auf mit "python3 <dateiname> arg1 arg2 arg3"
print(sys.argv)

# Der Name des Programms steckt immer im ersten Wert von `argv`.
# Diesen können Sie auch über die magische Variable `__file__` abfragen.
print(sys.argv[0] == __file__)

# Konvention, um nur die echten Parameter zu erhalten.
# Der Variablenname '_' suggeriert, dass diese Variable nicht
# weiter verwendet wird
_, *arguments = sys.argv
print(arguments)
