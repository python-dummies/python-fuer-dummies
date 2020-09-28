#!/usr/bin/env python3
'''
PNG-Chunks
==========

Fügt einen tEXt-Chunk an eine PNG-Datei an.

Ablauf:

 1. `INPUT_FILE` als Bytes einlesen
 2. Bytes in Chunks aufteilen
 3. Neuen Kommentar-Chunk erstellen
 4. Bestehende Chunks iterieren
 5. Alte Chunks in `OUTPUT_FILE` schreiben
 6. Nach dem IHDR-Chunk den Kommentar-Chunk schreiben
 7. Fertig!

Wenn Sie die Datei `OUTPUT_FILE` in einem Bildbetrachter anschauen,
sehen Sie in den Metadaten den Text.


Hintergrund
-----------

Ein PNG besteht aus einer Signatur (8 bytes), gefolgt von einer Reihe
von Chunks. Jeder Chunk besteht aus:

LEN: 4 Bytes
TYP: 4 Bytes
DAT: ... So viele Bytes, wie im Feld "LEN" steht.
CRC: 4 Bytes, Prüfsumme aus TYP und DAT

Andere Versionen
----------------

Dieses Programm wird schrittweise entwickelt. Bitte beachten Sie auch:

 - binary-lesen.py
 - first-chunk.py
 - list-chunks.py
'''

import sys
import zlib


def comment_chunk(text):
    """
    Erstellt einen png tEXt-Chunk für `Comment`-Felder.
    """

    # Die Groß-Kleinschreibung ist Absicht.
    # Das gibt die Spezifikation vor.
    header_bytes = b'tEXt'

    # tEXt Chunks beinhaltet Latin-1 encodierten Text.
    # "Comment" ist ein reserviertes Schlüsselwort.
    # Das 0-Byte ist ein string-Separator
    text_bytes = b'Comment' + b'\x00' + text.encode('latin-1')
    length_bytes = len(text_bytes).to_bytes(4, byteorder='big')

    # Prüfsumme hinzufügen
    # Die CRC-Prüfsumme (Cyclical Redundancy Check) beinhaltet
    # den Chunk-Typ und die Nutzdaten (DAT)
    crc = zlib.crc32(header_bytes + text_bytes)
    crc_bytes = crc.to_bytes(4, byteorder='big')

    # Den Chunk als fortlaufende Byte-Sequenz zurückgeben
    return length_bytes + header_bytes + text_bytes + crc_bytes


signature = None
chunks = []
COMMENT = 'Das ist aber ein Schönes Bild!'

INPUT_FILE = 'checkers.png'
OUTPUT_FILE = 'checkers-commented.png'


# Original einlesen
with open(INPUT_FILE, 'rb') as png:

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

        # Chunk als Tupel-Paket an die Ergebnisliste anfügen.
        chunk = (length_bytes + chunk_type + data + crc)
        chunks.append(chunk)


# Bild mit Kommentar abspeichern
with open(OUTPUT_FILE, 'wb') as png:
    # Die alte Signatur wegschreiben
    png.write(signature)

    # Die alten Chunks durchgehen
    for chunk in chunks:
        # Den Chunk schreiben
        png.write(chunk)

        # Nochmal nachgucken: Welcher Chunk-Typ wurde geschrieben?
        chunk_type = chunk[4:8]

        # Wenn der letzte Chunk ein IHDR-Chunk war, kann der
        # tEXt-Chunk eingefügt werden.
        if chunk_type == b'IHDR':
            # Der IHDR-Chunk muss immer zuerst kommen
            # IHDR ist der Image-Header, er beinhaltet wichtige Metadaten
            png.write(comment_chunk(COMMENT))
