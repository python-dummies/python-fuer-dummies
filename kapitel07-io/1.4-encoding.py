#!/usr/bin/env python3
"""
Encoding
========

Code und Daten sollten in Python utf-8 kodiert sein.

Achtung: Je nach Einstellung ihrer Konsole kann es
zu Darstellungsfehlern in der Ausgabe kommen.
"""


text = "hallö, wëlt!"
print('String:', text)

encoded = text.encode(encoding="utf-8")
print('Byte-Darstellung:', encoded)

decoded = encoded.decode()
print('String', decoded)

# Wenn Sie einem String ein kleines b voranstellen
# handelt es sich um ein Bytes-Objekt, nicht um einen String.
text_bytes = b'hall\xc3\xb6, w\xc3\xablt!'
print(text_bytes)

# Erst, wenn Sie diesen Text dekodieren, bekommen Sie einen String:
print(text_bytes.decode('utf-8'))
