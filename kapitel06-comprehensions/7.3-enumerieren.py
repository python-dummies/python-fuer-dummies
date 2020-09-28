#!/usr/bin/env python3
"""
Ohne Index Elemente auflisten -- Nutzen Sie `enumerate`
"""

# Pythonic
languages = ['Python', 'C#', 'JavaScript']
for i, language in enumerate(languages, start=1):
    print(f'{i}. {language}')


# Nicht pythonic
languages = ['Python', 'C#', 'JavaScript']
i = 0
while i < len(languages):
    print(f'{i + 1}. {languages[i]}')
    i += 1