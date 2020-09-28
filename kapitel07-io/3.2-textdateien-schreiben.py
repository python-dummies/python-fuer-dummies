#!/usr/bin/env python3
"""
Textdateien im Ganzen schreiben
===============================
"""

text = """How strong is your wish
That the crash took it all
No backup remains?"""

with open("a-haiku.txt", "w") as file:
    file.write(text)
    try:
        print(file.read())
    except:
        # Im Moduls `open(<name>, 'w')` kann die Datei nur geschrieben
        # aber nicht gelesen werden und erzeugt daher einen Fehler.
        import traceback
        traceback.print_exc()


with open("a-haiku.txt", "w+") as file:
    file.write(text)
    # den Stream "zurückspulen"
    file.seek(0)
    # Im Moduls 'w+' kann die Datei zurückgespult und gelesen werden
    print(file.read())
