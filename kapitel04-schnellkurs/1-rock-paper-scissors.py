#!/usr/bin/env python3
"""
Rock - Paper - Scissors

Ein kleines Spiel (Schere, Stein, Papier) um Ihnen ein bisschen Python zu
zeigen.
"""

# Modul importieren
import random

#  Variablen anlegen
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

TIE = "Tie."
WIN = "You win :-)"
LOSE = "You lose :-("


# Eine Funktion mit Parametern
def compare_moves(you, computer):
    # Wenn--Dann-Vergleiche
    if you == computer:
        return TIE
    elif you == SCISSORS and computer == PAPER:
        return WIN
    elif you == ROCK and computer == SCISSORS:
        return WIN
    elif you == PAPER and computer == ROCK:
        return WIN
    else:
        # ... in allen anderen Fällen
        return LOSE


you = ""

# While-Schleife
while you not in [ROCK, PAPER, SCISSORS]:
    # Eingabe
    you = input("(r)ock, (p)aper, or (s)cissors? > ")

# Funktionsaufrufe
computer = random.choice([ROCK, PAPER, SCISSORS])
result = compare_moves(you, computer)

# Ausgabe
print(f"You: {you}, Computer: {computer}. {result}")
