#!/usr/bin/env python3
"""
Dictionary Comprehensions
=========================

Beschreiben Sie Datentransformationen mit einer eleganten Syntax.
Das Ergebnis ist ein Dictionary (Schlüssel--Wert-Paare).
"""

lexicon_de_en = {
    'Auto': 'car',
    'Wand': 'wall',
    'Boden': 'floor',
}

print('lexicon_de_en:', lexicon_de_en)

# Projektion: Schweifklammern und Doppelpunkt
# Iteration des Dicts mit `lexicon_de_en.items()`
lexicon_en_de = {value: key for key, value in lexicon_de_en.items()}

print('lexicon_en_de:', lexicon_en_de)

print()
print('Liste berühmter Rennpferde:')
race_horses = {
    'Acatenango': (1993, 2005),
    'Hoof Hearted': (1973, 1978),
    'Seabiscuit': (1933, 1947),
    'Anita Hanjab': (1951, 1969),
    'Oil Beef Hooked': (1989, 1997),
    'Ben Timover': (1974, 1986),
    'Secretariat': (1972, 1989),
    'Sea the Moon': (2014, 2020)
}
print('race_horses:', race_horses)
# Komplexeres Beispiel:


# Projektion: <Schlüssel>:<Wert>. Hier ist Wert ist ein Ausdruck
# Iteration: iterieren über dict.items(). Jedes Item ist ein Tupel, das an
# zweiter Stelle ein Tupel beinhaltet
# Selektion: Filter über die Jahreszahlen
horse_years = {
    name: end - start
    for name, (start, end)
    in race_horses.items()
    if 1970 <= start <= 1980
}

print('horse_years:', horse_years)
