#!/usr/bin/env python3
'''
PNG-Chunks prüfen
=================

Gibt den ersten Chunk einer PNG-Datei aus.
Der Erste Chunk sollte immer IHDR sein.

Ein PNG besteht aus einer Signatur (8 bytes), gefolgt von einer Reihe
von Chunks. Jeder Chunk besteht aus:

LEN: 4 Bytes
TYP: 4 Bytes
DAT: ... So viele Bytes, wie im Feld "LEN" steht.
CRC: 4 Bytes, Prüfsumme aus TYP und DAT
'''

with open("screenshot.png", "rb") as png:
    # Signatur einlesen (8 Bytes)
    signature = png.read(8)

    # Anfang des ersten Chunks
    length_bytes = png.read(4)

    # Typ des ersten Chunks
    chunk_type = png.read(4)

    # Ausgabe: IHDR
    print(chunk_type)
