#!/usr/bin/env python3
"""
Swap Case
=========

Dieses Programm soll die Groß-Kleinschreibung vertauschen.
Leider funktioniert es nicht.
"""
import string
lowers = string.ascii_lowercase


def swap_case(text):
    result = ""
    for char in text:
        if char in string.ascii_lowercase:
            result += char.lower()
        else:
            result += char.upper()
    return result


print(swap_case("Hallo"))
