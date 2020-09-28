#!/usr/bin/env python3
"""
Iterieren ohne Index -- Nutzen Sie for-Schleifen
"""

# Kein Guter Stil!
data = [1,2,3,4]
i = 0
while i < len(data):
    value = data[i]
    print(value)
    i += 1

# Viel einfacher
data = [1,2,3,4]
for value in data:
    print(value)