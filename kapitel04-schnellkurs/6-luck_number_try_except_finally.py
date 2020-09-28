#!/usr/bin/env python3
"""
Ratespiel, das Fehlerfälle besser unterscheidet
"""

# Modul zum Generieren von Pseudozufallszahlen
import random

# Eingabe
guess = input("Your guess (1-10): ")

# Zufallszahl generieren
lucky_number = random.randint(1, 10)


# Vergleichen
try:
    if int(guess) == lucky_number:
        print("You win!")
    else:
        print(f"You lose. Lucky number is {lucky_number}")
except ValueError:
    # Empfohlen: Die erwartete Ausnahme explizit benennen
    print(f"'{guess}' is not a number.")
finally:
    # In jedem Fall wird dieser Block zusätzlich aktiv
    # (also auch im Fehlerfall).
    print("Bye!")
