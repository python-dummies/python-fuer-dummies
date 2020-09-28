#!/usr/bin/env python3
"""
Slicing
=======

Mit Hilfe mehrere Indizes können Sie Listen und andere Sequenzen zerteilen.
"""

names = [
    'Annie Easley',
    'Margaret Hamilton',
    'Barbara Liskov',
]

print('    names:', names)
# Das erste Element
print(' names[0]:', names[0])

# Das letzte Element
print('names[-1]:', names[-1])



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing:
# Syntax: [start:stop:step]
print('     numbers:', numbers)

# Wie bei ranges ist der untere Index inklusiv, der obere exklusiv
print('numbers[2:5]:', numbers[2:5])



numbers = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]

# Die Parameter von `range` funktionieren genauso!
a = list(range(0, 20, 2))
b = numbers[0:20:2]
print('a == b:', a == b)

