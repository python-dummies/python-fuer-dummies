#!/usr/bin/env python3
"""
Message of the Day
==================

Dieses Programm soll an meinem (fiktiven) Geburtstag einen
Glückwunsch ausgeben. Leider funktioniert es nicht.
"""
from datetime import date

bday = date(1987, 1, 25)
today = date.today()

if bday.day == today.day and bday.month == today.month:
    age = today.year - bday.year
    print("Alles Gute zum " + age + "ten , Johannes!")
else:
    print("Willkommen zurück")