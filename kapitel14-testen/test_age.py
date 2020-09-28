#!/usr/bin/env python3
"""
test_age.py
===========

Beinhaltet Test-Fälle für das Errechnen des Alters aus zwei Datumsangaben.
Die Vorannahmen werden hier mit `assert`-Anweisungen geprüft.
"""
from datetime import datetime
import math
import unittest


def age(born, today):
    assert born <= today

    birthday_upcoming = (today.month, today.day) < (born.month, born.day)
    return today.year - born.year - birthday_upcoming


def agex(born, today):
    assert born <= today

    time_alive = today - born
    return math.floor(round(time_alive.days / 365.25))


class AgeTests(unittest.TestCase):
    def test_exactly_zero(self):
        born = datetime(2018, 1, 1)
        today = datetime(2018, 1, 1)

        self.assertEqual(age(born, today), 0)

    def test_zero_something(self):
        born = datetime(2018, 1, 1)
        today = datetime(2018, 7, 1)

        self.assertEqual(age(born, today), 0)

    def test_almost_one(self):
        born = datetime(2018, 1, 1)
        today = datetime(2018, 12, 31)

        self.assertEqual(age(born, today), 0)

    def test_exactly_one(self):
        born = datetime(2018, 1, 1)
        today = datetime(2019, 1, 1)

        self.assertEqual(age(born, today), 1)

    def test_almost_eighteen(self):
        born = datetime(2000, 7, 15)
        today = datetime(2018, 7, 14)

        self.assertEqual(age(born, today), 17)

    def test_exactly_eighteen(self):
        born = datetime(2000, 7, 1)
        today = datetime(2018, 7, 1)

        self.assertEqual(age(born, today), 18)

    def test_eighteen_something(self):
        born = datetime(2000, 7, 1)
        today = datetime(2018, 12, 1)

        self.assertEqual(age(born, today), 18)
