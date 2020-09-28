
#!/usr/bin/env python3
"""
Built-Ins
=========

Built-in Funktionen und Objekte müssen nicht importiert werden.
"""

# Blanke Ironie: Wir importieren hier das Modul `builtins`,
# um alle bekannten Built-ins auszugeben.
# Normalerweise muss man das nicht.
# Beispielsweise kann jedes Python Programm kann ohne einen
# Import `print` aufrufen.
import builtins

print('Built-Ins')
print('=========')
print()
print('Alle')
print('----')
print(dir(builtins))

print()
print('Die wichtigsten')
print('---------------')

important_builtins = [
    builtin
    for builtin in dir(builtins)
    if builtin.lower() == builtin
    and not builtin.startswith('_')
]

# https://docs.python.org/3/library/functions.html
for i, builtin in enumerate(important_builtins):
    # 7 Elemente pro Spalte
    if i % 5 == 0:
        print()
    # Als Tabelle formatieren
    print(f'{builtin:<18s}', end=' ')

print()
print()
print('Dokumentation zu einem Built-In ausgeben:')
print('-----------------------------------------')
print(help(zip))
