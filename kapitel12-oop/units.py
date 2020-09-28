#!/usr/bin/env python3
"""
Vererbung
=========

Wenn Objekte eine "Ist-ein" Beziehung bilden sollen,
ist es sinnvoll, eine Vererbungshierarchie zu definieren.
"""


# Elternklasse
# ------------
class Unit:
    SYMBOL = ''

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return f'{self._value} {self.SYMBOL}'

    def __repr__(self):
        return str(self)


# Kindklasse
# ----------
# Man sagt auch:
# - Unit ist die "Basisklasse"
# - `SquareMetre` ist von `Unit` "abgeleitet"
# - `SquareMetre` "erbt" von `Unit`
#
# Das bedeutet jeweils:
# SquareMetre kann auf die Daten und Methoden der Elternklasse zugreifen
# und deren Verhalten verfeinern, aber auch überschreiben
class SquareMetre(Unit):

    # Das Symbol wird überdeckt.
    SYMBOL = 'm²'
    FACTOR = 1

    def convert_to(self, Target):
        normalized = self._value * self.FACTOR
        return Target(normalized / Target.FACTOR)


class SquareKilometre(SquareMetre):
    SYMBOL = 'km²'
    FACTOR = 1_000_000


class SquareCentimetre(SquareMetre):
    SYMBOL = 'cm²'
    FACTOR = 0.0001


class FootballField(SquareMetre):
    SYMBOL = 'Fußballfelder'
    FACTOR = 105 * 68


class Saarland(SquareMetre):
    SYMBOL = 'Saarland'
    FACTOR = 1_000_000 * 2569.69


class Lyoner(SquareMetre):
    def __init__(self, radius):
        self._radius = radius

    def convert_to(self, Target):
        return Target(3.1415 * self._radius ** 2)


if __name__ == '__main__':

    # Einige Tests
    print(SquareMetre(1).convert_to(SquareCentimetre))
    print(SquareMetre(75).convert_to(SquareCentimetre))
    print(FootballField(1).convert_to(SquareMetre))
    print(FootballField(1).convert_to(Saarland))
    print(Saarland(1).convert_to(SquareKilometre))
    print(SquareMetre(1).convert_to(FootballField))
    print(Saarland(1).convert_to(FootballField))

    # Völliger Murks:
    # radius_cm = 5
    # lyoner = SquareCentimetre(3.1415 * radius_cm ** 2)
    # 78,71 km²

    # Greifbares Beispiel
    yellow_stone_national_park = SquareKilometre(8991)
    print(yellow_stone_national_park.convert_to(Saarland))
