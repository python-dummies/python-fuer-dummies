#!/usr/bin/env python3
"""
Bytecode Ausgeben
=================

Python-Code wird in Bytecode übersetzt. Diesen kann man mit Hilfe des Moduls
`dis` aus der Standardbibliothek ausgeben.
"""
def is_first_half(month):
    return month in (5, 4, 3, 2, 1)

import dis
print(dis.dis(is_first_half))