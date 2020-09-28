#!/usr/bin/env python3
"""
IBAN Überprüfen
===============

Validierung nach nach ISO 7064, mod 97-10.

Quellen:
 - https://de.wikipedia.org/wiki/Internationale_Bankkontonummer#Pr%C3%BCfsumme
 - https://www.iban.de/iban-pruefsumme.html

Example IBAN: DE89 3704 0044 0532 0130 00
BBAN:              3704 0044 0532 0130 00
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(character):
    """
    Kodierung der Buchstaben:
    A = 10, B = 11, C = 12, usw.
    Für Deutsche IBAN muss dieser Wert
    DE = 1314
    sein
    """
    code = ALPHABET.index(character) + 10
    return str(code)


# Eingabe
iban = input('IBAN > ')
iban = iban.replace(' ', '').upper()

# Einzelteile
countrycode = iban[0:2]
a = encode(countrycode[0])
b = encode(countrycode[1])
checksum = iban[2:4]
bban = iban[4:]

# Prüfung
valid = int(bban + a + b + checksum) % 97

if valid == 1:
    print("IBAN ist gültig")
else:
    print("IBAN ist ungültig")
