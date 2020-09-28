#!/usr/bin/env python3
"""
Print
=====

Texte auf der Konsole ausgeben
"""

# Print erzeugt stets eine neue Zeile
print("Hello, World!")

# Mehrere Einzelteile werden durch Leerzeichen getrennt
print("Hello,", "World!")


# Ende und Separator können verändert werden
print("To do: ", end="")
print("dishes", "paperwork", "call mom", sep=", ")

# Leeres Print macht eine Leerzeile
print()

# Ausgabe Steuern: New Line
print('Hello,\nWorld!')

print()

# Ausgabe Steuern: Carriage Return
password = "s0-s3cur3!!"
print(password)

# \r setzt den "Schlitten" an den Zeilenanfang zurück
masked = password + "\r" + "*****"
print(masked)

# Ausgabe Steuern: Einrückung mit \t
print()
print('Einkaufen:')
print('\t[x] Milch')
print('\t[ ] Mehl')
print('\t[ ] Nudeln')
print('\t[ ] Klopapier')


print()
# Ausgabe Steuern: Glocke
print('Ding!\a')
