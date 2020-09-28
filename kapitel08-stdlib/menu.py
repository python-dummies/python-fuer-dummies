#!/usr/bin/env python3
"""
Menü
====

Formatiert ein verschachteltes Dictionary als Speisekarte.

Demonstriert die Mini-Syntax für die Formatierung von
Strings mit fester Breite.
"""

menu = {
    'Speisen': {
        'Pizza Margherita': 8,
        'Pizza Toscana': 11.6,
        'Pizza Tartufo': 100.9,
    },
    'Getränke': {
        'Wasser (4cl)': 0.5,
        'Cola (5cl)': 1.2,
    }
}

# Alle Oberkategorien durchlaufen
for category, dishes in menu.items():

    # Überschrift ausgeben
    # ====================
    #  - Füllzeichen: ~
    #  - Zentrieren mit ^
    #  - 40 Zeichen Zeilenbreite
    print(format(category, '~^40'))
    for dish, price in dishes.items():

        # Gericht ausgeben
        # ================
        #
        #  - Füllzeichen: .
        #  - Links ausreichten: <
        #  - Die ersten 20 Zeichen der Zeile
        #  - Zeile wird noch nicht umgebrochen (`end=''`)
        print(format(dish, '.<20'), end='')

        # Preis ausgeben
        # ==============
        #
        #  - Füllzeichen: .
        #  - Rechts ausreichten: >
        #  - Die vorletzten zwei Zeichen einer Zeile sind Nachkommastellen
        #  - Alle Zahlen werden auf 2 Nachkommastellen gerundet
        #  - Die letzten zwei Zeichen sind ein Währungssymbol
        #  - Zeile wird abgeschlossen und umgebrochen (`end='\n'`)
        print(format(price, '.>18.2f'), end=' €\n')

        ## Kürzer mit Format-Strings
        ## Dieser Einzeiler ersetzt die letzten beiden Aufrufe von `format`
        # print(f'{dish:.<20}{price:.>18.2f} €')
