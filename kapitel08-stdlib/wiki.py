#!/usr/bin/env python3
"""
Wiki
====

Gibt einen zufälligen Wikipedia-Artikel aus
"""

# Lesen von JSON-Daten
import json

# Bibliothek zum Herunterladen einer Webseite
import urllib.request


URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


# Webseite aufrufen
with urllib.request.urlopen(URL) as response:

    # Metadaten auslesen
    content_type_header = response.headers.get('Content-Type')
    content_type, *_ = content_type_header.split(';')

    # Metadaten ausgeben
    print("HTTP Content Type:", content_type)
    print("HTTP Status-Code:", response.status)

    # Binäre HTTP-Response dekodieren
    content = response.read().decode('utf-8')
    dictionary = json.loads(content)

    # Titel ausgeben
    print("Titel:", dictionary.get('title'))

    # Die URL zum Artikel ist etwas verschachtelt...
    print("Link:", dictionary.get('content_urls').get('desktop').get('page'))
