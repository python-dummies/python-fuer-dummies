# Original einlesen
with open('screenshot.png', 'rb') as png:
    # Signatur
    signature = png.read(8)

    # Chunks
    while True:
        length_bytes = png.read(4)
        if not length_bytes:
            break

        chunk_type = png.read(4)
        length = int.from_bytes(length_bytes, 'big')
        data = png.read(length)
        crc = png.read(4)
        print(f'{chunk_type} ({length})')