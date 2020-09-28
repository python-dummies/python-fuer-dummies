"""
PNG-Chunks
==========

Gibt die Chunks einer PNG-Datei und eine Zusammenfassung ihrer Inhalte aus.

In Kapitel 7 zeigen wir, wie man Binärdateien liest und schreibt.
Das demonstrieren wir anhand von prozeduralem Code. In Wirklichkeit
ist die Struktur von PNG-Chunks aber hervorragend geeignet, um
sie als objektorientierte Vererbungshierarchie abzubilden.

Hier demonstrieren wir eine objektorientierte Implementierung mit einer
Vererbungshierarchie für Chunk-Typen.

Ein `Chunk` besteht immer aus Länge, Typ, Daten und Prüfsumme.
Die verschiedenen Chunk-Typen können dann selbst bestimmen,
wie sie die Daten des Chunks interpretieren.

http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
http://www.libpng.org/pub/png/spec/1.2/PNG-Compression.html

Aufruf:

    $ python3 png_chunks.py checkers.png

"""
import sys
import datetime
import pathlib
import collections
import zlib


def big_endian_number(function):
    def convert_bytes(*args, **kwargs):
        return int.from_bytes(function(*args, **kwargs), 'big')
    return convert_bytes


class _Chunk:

    class WrongLength(Exception):
        def __init__(self, actual_length, expected_length):
            self._actual_length = actual_length
            self._expected_length = expected_length

        def __str__(self):
            return (
                f'Wrong amount of data read:\n'
                f'  Length of data read: {self._actual_length}\n'
                f'  Expected Length: {self._expected_length}\n'
            )

    class ChecksumMismatch(Exception):
        def __init__(self, actual_crc, expected_crc):
            self._actual_crc = actual_crc
            self._expected_crc = expected_crc

        def __str__(self):
            return (
                f'Data Corruption detected:\n'
                f'  Actual: {self._actual_crc}\n'
                f'  Expected: {self._expected_crc}\n'
            )

    def __init__(self, length, chunk_type, data, crc):
        self._length = length
        self._chunk_type = chunk_type
        self._data = data
        self._crc = crc
        self._check_length()
        self._check_sum()

    def _check_length(self):
        if self._length == len(self._data):
            return
        raise Chunk.WrongLength(
            len(self._data), self._length
        )

    def _check_sum(self):
        actual_crc = zlib.crc32(self._chunk_type + self._data)
        if actual_crc == self._crc:
            return
        raise Chunk.ChecksumMismatch(
            self._actual_crc, self._crc
        )

    def __repr__(self):
        name = self.__class__.__name__
        type_ = self._chunk_type.decode('ascii')
        return f'<{name}: {type_} ({self._length})>'


class ImageHeader(_Chunk):
    def __init__(self, *args):
        super().__init__(*args)

    @big_endian_number
    def width(self):
        return self._data[:4]

    @big_endian_number
    def height(self):
        return self._data[4:8]

    @big_endian_number
    def bit_depth(self):
        return self._data[8:9]

    @big_endian_number
    def color_type(self):
        # IF 6, Pixels are RGB Triple and Bit Depth must be 8 or 16
        return self._data[9:10]

    @big_endian_number
    def compression_method(self):
        # PNG 1.1: @0
        return self._data[10:11]

    @big_endian_number
    def filter_method(self):
        # PNG 1.1: @0
        return self._data[11:12]

    @big_endian_number
    def interlace_method(self):
        # 0 == no interlace
        # 1 == interlace
        return self._data[12:13]

    def __repr__(self):
        w, h = self.width(), self.height()
        return f'<ImageHeader: {w}x{h}>'


class ImageData(_Chunk):
    def deflate(self):
        # Data is in zlib format, thus comes with a header
        # (first couple of bytes)
        # and an ADLER32 CRC (last 4 bytes)
        # This could word off the shelf like this, but I haven't tried
        # return zlib.decompress(self._data)
        raise NotImplemented()


class ModificationTime(_Chunk):
    '''
    #  Time of last Image Modification
    LEN: 00 00 00 07 (7)
    TYP: 74 49 4d 45 (tIME)
    DAT:
        - 07 e4 (YEAR)
        - 01 (MONTH)
        - 11 (DAY)
        - 0c (HOUR)
        - 29 (MINUTE)
        - 0c (SECOND)
    CRC: d0 2e c0 da (SUM)
    '''

    def __repr__(self):
        yyyy = int.from_bytes(self._data[:2], 'big')
        month, day, hour, minute, second = self._data[2:]
        time = datetime.datetime(yyyy, month, day, hour, minute, second)
        return f'<ModificationTime: {time}>'


class Background(_Chunk):
    '''
    # Background Color
    LEN: 00 00 00 06 (6)
    TYP: 62 4b 47 44 (bKGD)
    DAT:
        - 00 ff (RED)
        - 00 ff (GREEN)
        - 00 ff (BLUE)
    CRC: a0 bd a7 93 (SUM)
    '''

    @big_endian_number
    def red(self):
        return self._data[0:2]

    @big_endian_number
    def green(self):
        return self._data[2:4]

    @big_endian_number
    def blue(self):
        return self._data[4:6]

    def __repr__(self):
        rgb = (self.red(), self.green(), self.blue())
        color = ''.join(f'{channel:02x}' for channel in rgb)
        return f'<Background: #{color}>'


class Text(_Chunk):
    KEYWORDS = [
        'Title', 'Author', 'Description', 'Copyright',
        'Creation Time', 'Software', 'Disclaimer', 'Warning',
        'Source', 'Comment'
    ]

    def keyword(self):
        content = self._data[:80].decode('utf-8')
        for keyword in self.KEYWORDS:
            if content.startswith(keyword):
                return keyword
        return f'<Weird Keyword: {content}>'

    def text(self):
        keyword = self.keyword()
        return self._data[len(keyword):].decode('utf-8')

    def __repr__(self):
        return f'<Text: {self.keyword()}: "{self.text()}">'


class PhysicalDimensions(_Chunk):
    # Resolution?
    '''
    # Physical Pixel Dimensions
    LEN: 00 00 00 09 (9)
    TYP: 70 48 59 73 (pHYs)
    DAT:
        - 00 00 0b 13 (2835) [X Pixels per unit, i.e. 72.009 dpi]
        - 00 00 0b 13 (2835) [Y Pixels per unit, i.e. 72.009 dpi]
        - 01 (Unit) [0=?, 1=meter]
    CRC: 00 9a 9c 18 (SUM)
    '''
    @big_endian_number
    def x_pixels_per_unit(self):
        return self._data[0:4]

    @big_endian_number
    def y_pixels_per_unit(self):
        return self._data[4:9]

    def __repr__(self):
        DPI_FACTOR = 0.0254
        dpi = self.x_pixels_per_unit() * DPI_FACTOR
        return f'<Resolution: {dpi:.2f} dpi>'


class UnknownChunk(_Chunk):
    '''
    Null object. We were too lazy to implement all chunk types.
    The most important types are IHDR, IDAT, and IEND.

    - PLTE (Palette Information)

    Ancillary chunks (identifyable by their lowercase letter, as determined by
    bit 5 of the first byte) are:

    - tRNS (Transparency)
    - gAMA (Gamma Correction)
    - cHRM (Primary Chromaticities)
    - sRGB (Standard RGB Color Space)
    - iCCP (Embedded ICC Profile)
    -  tEXt, iTXt, and zTXt (Text, International Text, Compressed Text)
    - sBIT (Significant bits)
    - sPLT (Palette)
    - hIST (Palette Histogram)

    See: http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
    '''
    pass


class EndOfFile(_Chunk):
    pass


class Chunk:
    CHUNK_TYPES = {
        b'IHDR': ImageHeader,
        b'IDAT': ImageData,
        b'IEND': EndOfFile,
        b'bKGD': Background,
        b'pHYs': PhysicalDimensions,
        b'tIME': ModificationTime,
        b'tEXt': Text,
    }

    def __new__(cls, length, chunk_type, data, crc):
        ChunkType = cls.CHUNK_TYPES.get(chunk_type, UnknownChunk)
        return ChunkType(length, chunk_type, data, crc)


class Chunks:
    def __init__(self, file):
        self._file = file

    @big_endian_number
    def _read_number(self, n=1):
        bytes_ = self._file.read(4)
        if not bytes_:
            raise StopIteration
        return bytes_

    def _write_number(self, number):
        # TODO: Maybe later...
        # To write, use this:
        # return number.to_bytes(4, byteorder='big')
        raise NotImplemented

    def _read_chunk_data(self):
        length = self._read_number(4)
        chunk_type = self._file.read(4)
        data = self._file.read(length)
        checksum = self._read_number(4)
        return length, chunk_type, data, checksum

    def __iter__(self):
        data = self._read_chunk_data()
        yield ImageHeader(*data)
        while True:
            try:
                data = self._read_chunk_data()
                yield Chunk(*data)
            except StopIteration:
                return



class Signature:
    '''
    The signature is built in such a way that printing the image to a
    terminal will not dump all data (on msdos type), hence the "portable"...
    SIG: 89
    PNG: 50 4e 47 (PNG)
    BRK: 0d 0a 1a 0a (CR,LF,EOF,LF)
    '''
    @classmethod
    def read(cls, file):
        # Signature
        assert file.read(1) == b'\x89'
        assert file.read(3) == b'PNG'
        # Break: CR,LF,EOF,LF
        assert file.read(4) == bytes([0x0d, 0x0a, 0x1a, 0x0a])
        return cls()


def print_chunks(file):
    Signature.read(file)
    for chunk in Chunks(file):
        print(chunk)


if __name__ == '__main__':
    _, filename = sys.argv
    with open(filename, 'rb') as file:
        print_chunks(file)
