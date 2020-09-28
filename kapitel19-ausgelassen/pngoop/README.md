PNG-Chunks
==========

In Kapitel 7 zeigen wir, wie man Binärdateien liest und schreibt.
Das zeigen wir anhand von prozeduralem Code.

In Wirklichkeit ist die Struktur von PNG-Chunks aber hervorragend geeignet, um
sie als Vererbungshierarchie abzubilden.

Ein `Chunk` besteht immer aus Länge, Typ, Daten und Prüfsumme.
Die verschiedenen Chunk-Typen können dann selbst bestimmen,
wie sie die Daten des Chunks interpretieren.


PNG Spezifikation
-----------------

http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
http://www.libpng.org/pub/png/spec/1.2/PNG-Compression.html


Beispiel PNG
------------

Als Beispiel liefern wir eine kleine PNG-Datei `checkers.png`.
Die Datei `PNG-data.txt` beinhaltet eine kommentierte Version dieser Datei.
Dort haben wir (von Hand) die Bedeutung jedes Bytes der Datei `checkers.png`
aufgeschrieben.


Aufruf
------

### Kurzfassung

    $ python3 short.py checkers.png

Diese Version listet nur die Chunks auf.

### Langfassung

    $ python3 png_chunks.py checkers.png

Diese Version gibt zusätzlich die Daten in den Chunks aus.