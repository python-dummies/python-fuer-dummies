#!/usr/bin/env python3
"""
Fraction
========

Stellt eine Bruch-Klasse dar.

Hier werden verschiedene Prinzipien demonstriert:
 - Der Bruch ist unveränderlich
 - Durch die Operatoren verhält er sich wie eine Zahl
 - Der Bruch kann sich selbst formatieren

Hinweis
-------
Bauen Sie das für die Praxis nicht selber. In der Standard-Bibliothek gibt
es bereits eine bessere Umsetzung:
https://docs.python.org/3/library/fractions.html
"""
import math


# Klasse
class Fraction:

    # Konstruktor
    def __init__(self, numerator, denominator):
        # Attribut: Zähler
        self._numerator = numerator
        # Attribut: Nenner
        self._denominator = denominator

    # Methode
    def reduced(self):
        gcd = math.gcd(self._numerator, self._denominator)
        return Fraction(
            self._numerator // gcd,
            self._denominator // gcd
        )

    def flipped(self):
        return Fraction(
            self._denominator, self._numerator
        )

    # "Dunder"-Methode. Diese Methode wird durch den Operator "*" aufgerufen
    def __add__(self, other):
        return Fraction(
            self._numerator * other._denominator + other._numerator * self._denominator,
            self._denominator * other._denominator
        )

    def __sub__(self, other):
        return Fraction(
            self._numerator * other._denominator - other._numerator * self._denominator,
            self._denominator * other._denominator
        )

    def __mul__(self, other):
        return Fraction(
            self._numerator * other._numerator,
            self._denominator * other._denominator
        )

    def __truediv__(self, other):
        return self * other.flipped()

    def value(self):
        return self._numerator / self._denominator

    def __float__(self):
        return self.value()

    def __str__(self):
        """
        Besonders wichtig: Diese Methode formatiert den Bruch als String.
        """
        return f'{self._numerator}/{self._denominator}'

    def __repr__(self):
        """
        Besonders wichtig: Diese Methode formatiert das Objekt in einer
        eindeutigen Repräsentation.
        """
        return f'<Fraction: {self._numerator}/{self._denominator}>'

    def __iter__(self):
        """
        Besonders wichtig: Diese Methode macht den Bruch iterierbar.
        """
        yield self._numerator
        yield self._denominator

    def __lt__(self, other):
        return float(self) < float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __eq__(self, other):
        """
        Besonders wichtig: Durch diese Methode können Sie Brüche mit
        anderen Objekten (Brüchen, Komma- oder Ganzzahlen) vergleichen.
        """
        if isinstance(other, float):
            return float(self) == other
        if isinstance(other, int):
            return self == Fraction(other, 1)
        return tuple(self.reduced()) == tuple(other.reduced())



# Durch diese Sperre wird verhindert, dass der folgende Code ausgeführt wird
# Wenn sie die Bruch-Klasse in einem anderen Programm importieren.
if __name__ == '__main__':

    # Konstruktor aufrufen, um ein Objekt anzulegen
    one_half = Fraction(1, 2)

    # Print ruft automatisch `Fraction.__str__` auf
    print("Bruch formatieren:", one_half)
    print("Kommaschreibweise ausgeben:", one_half.value())
    print("In Float konvertieren:", float(one_half))

    # Kürzen
    fraction = Fraction(6, 12)
    print("Roh:", fraction)
    print("Gekürzt:", fraction.reduced())

    # Vergleichen
    a = Fraction(1, 2)
    b = Fraction(17, 34)

    print("a:", a)
    print("b:", b)

    # Fraction.__eq__: Sind die Brüche equivalent?
    print(f"Gleichwertig? a == b", a == b)

    # Identität: Handelt es sich um dasselbe Objekt?
    print(f"Selb? a is b", a is b)

    c = a
    print(f"Selb? a is c", a is c)

    # Klarer: Speicheradressen angucken
    print("hex(id(a)):", hex(id(a)))
    print("hex(id(b)):", hex(id(b)))
    print("hex(id(c)):", hex(id(c)))

    # Tests: Geht alles?
    # ------------------

    assert Fraction(1, 3) * Fraction(100, 1) * \
        Fraction(3, 1) == Fraction(100, 1)

    # Vergleiche
    assert Fraction(1, 2) > Fraction(1, 4)
    assert Fraction(14, 18) > Fraction(12, 18)
    assert Fraction(1, 8) < Fraction(1, 4)
    assert Fraction(2, 1) == 2

    # Addition
    assert Fraction(1, 4) + Fraction(7, 4) == Fraction(2, 1)
    assert Fraction(1, 2) + Fraction(3, 4) == Fraction(5, 4)
    assert Fraction(2, 3) + Fraction(1, 3) == Fraction(1, 1)
    assert Fraction(4, 5) + Fraction(1, 2) == Fraction(13, 10)
    assert Fraction(8, 7) + Fraction(1, 2) == Fraction(23, 14)
    assert Fraction(6, 9) + Fraction(2, 3) == Fraction(4, 3)
    assert Fraction(5, 2) + Fraction(2, 8) == Fraction(11, 4)
    assert Fraction(1, 9) + Fraction(7, 3) == Fraction(22, 9)
    assert Fraction(2, 10) + Fraction(4, 10) == Fraction(3, 5)
    assert Fraction(4, 12) + Fraction(5, 12) == Fraction(3, 4)
    assert Fraction(6, 18) + Fraction(2, 6) == Fraction(2, 3)

    # Subtraktion
    assert Fraction(3, 4) - Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(7, 8) - Fraction(1, 4) == Fraction(5, 8)
    assert Fraction(8, 3) - Fraction(2, 3) == Fraction(2, 1)
    assert Fraction(4, 5) - Fraction(1, 4) == Fraction(11, 20)
    assert Fraction(3, 3) - Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(17, 4) - Fraction(14, 4) == Fraction(3, 4)
    assert Fraction(9, 2) - Fraction(10, 2) == Fraction(-1, 2)
    assert Fraction(4, 4) - Fraction(8, 2) == Fraction(-3, 1)
    assert Fraction(8, 1) - Fraction(12, 2) == Fraction(2, 1)
    assert Fraction(18, 3) - Fraction(20, 3) == Fraction(-2, 3)

    # Multiplikation
    assert Fraction(1, 3) * Fraction(2, 3) == Fraction(2, 9)
    assert Fraction(2, 4) * Fraction(1, 2) == Fraction(1, 4)
    assert Fraction(6, 1) * Fraction(2, 3) == Fraction(4, 1)
    assert Fraction(5, 6) * Fraction(3, 5) == Fraction(1, 2)
    assert Fraction(8, 2) * Fraction(5, 3) == Fraction(20, 3)
    assert Fraction(6, 9) * Fraction(2, 8) == Fraction(1, 6)
    assert Fraction(2, 4) * Fraction(6, 7) == Fraction(3, 7)
    assert Fraction(6, 3) * Fraction(2, 3) == Fraction(4, 3)
    assert Fraction(8, 2) * Fraction(10, 12) == Fraction(10, 3)
    assert Fraction(12, 7) * Fraction(1, 2) == Fraction(6, 7)

    # Beispiele für Divisionen
    assert Fraction(6, 3) / Fraction(2, 1) == Fraction(1, 1)
    assert Fraction(1, 2) / Fraction(3, 4) == Fraction(2, 3)
    assert Fraction(9, 2) / Fraction(1, 2) == Fraction(9, 1)
    assert Fraction(4, 5) / Fraction(2, 3) == Fraction(6, 5)
    assert Fraction(7, 2) / Fraction(5, 6) == Fraction(21, 5)
    assert Fraction(2, 9) / Fraction(2, 10) == Fraction(10, 9)
    assert Fraction(2, 3) / Fraction(6, 3) == Fraction(1, 3)
    assert Fraction(10, 20) / Fraction(3, 13) == Fraction(13, 6)
    assert Fraction(11, 12) / Fraction(10, 10) == Fraction(11, 12)
    assert Fraction(8, 17) / Fraction(2, 10) == Fraction(40, 17)
