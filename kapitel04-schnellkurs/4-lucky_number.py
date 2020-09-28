#!/usr/bin/env python3
"""
Ein kleines Ratespiel
"""

# Modul zum Generieren von Pseudozufallszahlen
import random

# Eingabe
guess = input("Your guess (1-10): ")

# Zufallszahl generieren
lucky_number = random.randint(1, 10)

# Vergleichen
if int(guess) == lucky_number:
    print("You win!")
else:
    print(f"You lose. Lucky number is {lucky_number}")