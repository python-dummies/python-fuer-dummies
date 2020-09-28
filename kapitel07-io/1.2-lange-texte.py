#!/usr/bin/env python3
"""
Längere Texte
=============

Wenn es um Strings geht, ist Python sehr nutzerfreundlich.
Es gibt verschiedene Arten, längere Strings anzulegen.
"""


# Anführungsstriche
# -----------------

# Quote-Typen mischen.
# Egal ob Sie mit " oder ' anfangen, das Ergebnis ist immer ein String
# Daher können Sie auch mischen:
print('air quotes "secure"')
print("air quotes 'secure'")

# Explizit escapen:
print("air quotes \"secure\"")


# Fragmente verketten
# -------------------

tasks = ["dishes", "paperwork", "call mom"]
print('Roh:', tasks)

# Liste mit Komma aneinanderfügen (CSV-Werte)
# Diese Syntax ist ein feststehendes Idiom
csv = ", ".join(tasks)

# Bonus: Am Ende der Liste ist kein Komma!
print('In einer Zeile: ')
print(f"To do: {csv}")


# In der Wahl des Separators sind Sie frei:
zeilenweise = "\n - ".join(tasks)
print()
print('Zeilenweise: ')
print(f"To do: \n - {zeilenweise}")
