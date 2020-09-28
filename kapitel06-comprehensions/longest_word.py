#!/usr/bin/env python3
"""
Das längste Wort finden
=======================

Übung zu Generator Expressions.

Hier wird ein Wörterbuch durchsucht, dass Sie hier herunterladen können:

https://extensions.libreoffice.org/en/extensions/show/german-de-de-frami-dictionaries

1. Laden Sie die .oxt Datei herunter
2. Öffnen Sie sie mit einem Zip-Programm
3. Darin ist das Wörterbuch "de_DE_frami.dic"
"""
def remove_tag(word):
    '''
    Returns "Abdeckerei" from "Abdeckerei/Pm"
    '''
    return word.split('/')[0]

with open('de_DE_frami.dic', mode='r', encoding='cp1252') as words:
    tagged_words = (
        remove_tag(word)
        for word in words
        if word.strip() and not word.startswith('#')
    )
    longest = max(len(word) for word in words)
    print(longest)
