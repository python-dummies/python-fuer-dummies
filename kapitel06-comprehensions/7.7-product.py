#!/usr/bin/env python3
"""
Zwei Listen mit einander multiplizieren
"""

# Sie haben zwei Listen und möchten alle möglichen Kombinationen erzeugen

# Vorbereitung
import itertools
suits = ['Kreuz', 'Pik', 'Herz', 'Karo']
pictures = ['König', 'Dame', 'Bube']


# Pythonic
cards = [
    f'{suit} {pic}'
    for suit in suits
    for pic in pictures
]


# Ausgabe
print(cards)


# Nicht pythonic
cards = []
for i in range(len(suits)):
    for k in range(len(pictures)):
        cards.append(f'{suits[i]} {pictures[k]}')


# Ausgabe
print(cards)


# Besonders Pythonic: Spezieller Iterator
cards = (' '.join(pair) for pair in itertools.product(suits, pictures))

# Ausgabe
# Cards ist ein Generating Iterator
print('cards:', cards)
print(list(cards))
