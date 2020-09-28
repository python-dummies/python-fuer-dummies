"""
PNG-Chunks - Kurzfassung
========================

Gibt die Chunk-Typen einer PNG-Datei aus.

In Kapitel 7 zeigen wir, wie man Binärdateien liest und schreibt.
Das demonstrieren wir anhand von prozeduralem Code. In Wirklichkeit
ist die Struktur von PNG-Chunks aber hervorragend geeignet, um
sie als objektorientierte Vererbungshierarchie abzubilden.

Hier demonstrieren wir eine objektorientierte Kurzversion ohne Umwege.

Diese Version ist, mal abgesehen von den Kommentaren, nicht länger
als die Prozedurale Version in `kapitel07-io/pngchunks.py`.

http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
http://www.libpng.org/pub/png/spec/1.2/PNG-Compression.html

Aufruf:

    $ python3 short.py checkers.png

"""
import sys


class Chunk:
    def __init__(self, length, chunk_type, data, crc):
        self._length = length
        self._chunk_type = chunk_type
        self._data = data
        self._crc = crc

    def __repr__(self):
        name = self.__class__.__name__
        type_ = self._chunk_type.decode('ascii')
        return f'<{name}: {type_} ({self._length})>'


class Chunks:
    def __init__(self, file):
        self._file = file

    def _read_number(self, n=1):
        bytes_ = self._file.read(4)
        if not bytes_:
            raise StopIteration
        return int.from_bytes(bytes_, 'big')

    def __iter__(self):
        while True:
            try:
                length = self._read_number(4)
                chunk_type = self._file.read(4)
                data = self._file.read(length)
                checksum = self._read_number(4)
                yield Chunk(length, chunk_type, data, checksum)
            except StopIteration:
                break


class Signature:
    @classmethod
    def read(cls, file):
        # Signature
        assert file.read(4) == b'\x89PNG'
        # Break: CR,LF,EOF,LF
        assert file.read(4) == bytes([0x0d, 0x0a, 0x1a, 0x0a])


if __name__ == '__main__':
    _, filename = sys.argv
    with open(filename, 'rb') as file:
        Signature.read(file)
        for chunk in Chunks(file):
            print(chunk)
