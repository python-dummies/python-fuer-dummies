#!/usr/bin/env python3
"""
Funktionale Programmierung
==========================

"""


# Eine einfache Funktion
# ----------------------

def even(number):
    return number % 2 == 0


print(even(10))
print(even(3))


# Positionale Argumente
# ---------------------

from datetime import datetime


def timestamp():
    return datetime.now().isoformat()


def shorten(text, length, placeholder):
    shortened = text[:length]
    placeholder = "" if shortened == text else placeholder
    return f"{shortened}{placeholder}"


print(timestamp())
text = "Lorem ipsum dolor sit amet, consetetur sadipscing"

# Argumente positional übergeben
print(shorten(text, 15, "..."))


# Benannte Argumente
# ------------------

# Placeholder wird als benanntes Argument übergeben
shorten(text, 15, placeholder="...")


# Namenlosigkeit erzwingen
# ------------------------

def shorten(text, /, length, *, placeholder):
    shortened = text[:length]
    placeholder = "" if shortened == text else placeholder
    return f"{shortened}{placeholder}"


# Default-Werte
# -------------

def shorten(text, length, placeholder="..."):
    shortened = text[:length]
    placeholder = "" if shortened == text else placeholder
    return f"{shortened}{placeholder}"


text = "A long and prosaic description"

# Die Übergabe optionaler Argumente ist ... nun: optional.
teaser = shorten(text, 10)
print(teaser)