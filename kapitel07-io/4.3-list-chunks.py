#!/usr/bin/env python3
'''
PNG-Chunks auflisten
====================

Listet die Chunks in einer PNG-Datei auf.

Ein PNG besteht aus einer Signatur (8 bytes), gefolgt von einer Reihe
von Chunks. Jeder Chunk besteht aus:

LEN: 4 Bytes
TYP: 4 Bytes
DAT: ... So viele Bytes, wie im Feld "LEN" steht.
CRC: 4 Bytes, Prüfsumme aus TYP und DAT

Der Erste Chunk sollte immer IHDR sein.
'''
import sys
input_file = sys.argv[1]
with open(input_file, 'rb') as png:

    # Signatur lesen
    signature = png.read(8)

    # Bis zum Ende durchlaufen
    while True:

        # Chunk-Länge einlesen
        length_bytes = png.read(4)

        # Wenn keine Länge feststellbar ist, sind wir am Ende der Datei
        if not length_bytes:
            break

        # Typ bestimmen
        chunk_type = png.read(4)

        # Längen Bytes ans Zahl interpretieren
        length = int.from_bytes(length_bytes, 'big')

        # Daten einlesen
        data = png.read(length)

        # CRC-Prüfsumme einlesen
        crc = png.read(4)

        print(f'{chunk_type} ({length})')
        # Alle Daten werden ignoriert. Sie müssen aber gelesen werden,
        # Um den Datei-Cursor voranzuschieben.