#!/usr/bin/env python3
"""
Data-Classes
============

Erzeugt Klassen mit Struct-Semantik.
Objekte der Klasse werden automatisch auf Equivalenz geprüft, nicht auf
Identitätsgleichheit.
"""
from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str

assert Person("Johannes", "Hofmeister") == Person("Johannes", "Hofmeister")
assert Person("Johannes", "Hofmeister") == Person("Horst", "Schneider")
