#!/usr/bin/env python3
"""
Year
====

Mit kleinen, fokussierten Objekten können Sie bestimmte Invarianten festlegen.
Jahreszahlen sind sehr spezielle Integer (-239023 ist wahrscheinlich kein
gültiges Jahr).
"""

class BadYearError(Exception):
    pass


class Year(int):
    MIN_YEAR = -120
    MAX_YEAR = 2150

    def __init__(self, year: int):
        if not Year.MIN_YEAR < year <= Year.MAX_YEAR:
            raise BadYearError(year)
        self._year = year

