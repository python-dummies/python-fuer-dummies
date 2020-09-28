#!/usr/bin/env python3
"""
Unsinn
======

Ein kleiner Syntax-Hack.
"""
class Text:
    def __init__(self):
        self._buffer = []

    def __getattr__(self, name):
        self._buffer.append(name)
        return self

    def __str__(self):
        return ' '.join(self._buffer)

text = Text(). Dies. ist. jetzt. valider. python. code

print(text)