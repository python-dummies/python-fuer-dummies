#!/usr/bin/env python3
"""
Dictionarys
===========

Dictionary speichern Schlüssel--Wert-Paare.
"""

# Dict anlegen
lexicon = {
    'Wand': 'wall',
    'Haus': 'house',
    'Dach': 'roof',
    'Boden': 'floor'
}

print(lexicon)

# Elemente abfragen
print('Wand:', lexicon.get('Wand'))
print('Hand:', lexicon.get('Hand', '<Nicht gefunden>'))

# Alternative: Zugriff mit Klammern
print('Zugriff mit Klammern:')
print("lexicon['Wand']):", lexicon['Wand'])
print("lexicon['Hand']): Ausnahme!")
try:
    # Löst eine Exception aus
    # KeyError fehler können Sie umgehen, indem Sie
    # `lexicon.get(...)`  verwenden
    print(lexicon['Hand'])
except KeyError:
    # Fehler auf der Konsole ausgeben.
    # Wenn ein Schlüssel nicht im Lexikon ist, entsteht ein KeyError
    # Wir fangen den Fehler ab und geben ihn aus.
    # Das machen wir hier nur zu Demozwecken.
    # Das macht man normalerweise alles nicht.
    # Weil solche Ausnahme-Fehler sonst den Programmablauf unterbrechen.
    # Details finden Sie in Kapitel 13 - Ausnahmen
    import traceback
    traceback.print_exc()


# Auspacken
print('Auspacken')
items = lexicon.items()
print(items)
head, *body, tail = items
print(body)


# Durchsuchen
print('Nach Schlüssel suchen:')
print("'Dach' in lexicon:", 'Dach' in lexicon)
print("'Monster' in lexicon:", 'Monster' in lexicon)
print('Nach Wert suchen:')
print("'house' in lexicon.values()", 'house' in lexicon.values())


# Hinzufügen
print('Hinzufügen')
print('Vorher:', lexicon)
lexicon['Brücke'] = 'Bridge'
print('Nachher:', lexicon)


# Werte überschreiben
print('Überschreiben')
lexicon['Auto'] = 'Vehicle'
print('Vorher:', lexicon)
lexicon['Auto'] = 'Car'
print('Nachher:', lexicon)


# Dicts erweitern
print('Erweitern:')
part1 = {'Auto': 'car',  'Schrank': 'wardrobe'}
part2 = {'Haus': 'house', 'Schrank': 'cupboard'}
print('Teil 1:', part1)
print('Teil 2:', part2)
part1.update(part2)
print('Teil 1, erweitert:', part1)


# Schlüssel löschen
print('Löschen')
lexicon = {'Auto': 'car',  'Schrank': 'wardrobe'}
print('Vorher:', lexicon)
print("Löschen: del lexicon['Auto']")
del lexicon['Auto']
print('Nachher:', lexicon)
