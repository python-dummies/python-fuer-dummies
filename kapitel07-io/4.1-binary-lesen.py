#!/usr/bin/env python3
"""
Binärdateien lesen
==================

Am Beispiel einer PNG-Datei.
"""

print()
print('Falsch:')
with open("screenshot.png") as binary:
    try:
        print(binary.read())
    except:
        # Ohne das richtige Encoding, erzeugt die Funktion eine
        # `UnicodeDecodeError`-Ausnahme.
        import traceback
        traceback.print_exc()

print()
print('Richtig:')
# Geben Sie zum lesen von Binärdateien den Moduls 'rb' an:
with open("screenshot.png", "rb") as binary:
    print('100 Bytes von screenshot.png')
    print(binary.read()[:20])
    # Ausgabe sollte sein:
    # b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\xec' ...

print()
print('Die PNG-Datei etwas genauer untersuchen:')
with open("screenshot.png", "rb") as binary:

    # PNGs fangen immer an mit b'\x89PNG\r\n\x1a\n'
    header = binary.read(8)
    print(header)

    # Erstes Byte ignorieren
    magic_number = header[1:4]
    print(magic_number)

    is_png = magic_number == b'PNG'
    print(f"File is {'a' if is_png else 'not a'} PNG")
