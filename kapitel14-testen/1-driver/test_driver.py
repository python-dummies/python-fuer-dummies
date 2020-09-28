#!/usr/bin/env python3
"""
Unittests
=========

Beinhaltet Tests für `driver.Driver`.

Ausführen mit:
  $ cd 1-driver
  $ python3 -m unittest -v

Der Test-Runner sucht alle Module, deren Name mit "test" anfängt
und führt sie aus. Sie brauchen also keinen __main__-Abschnitt.

Wenn Sie die Tests ausführen, laufen nicht alle Testfälle erfolgreich ab.
Das ist ein Hinweis darauf, dass `driver.Driver` noch nicht vollständig ist
und verbessert werden muss.

Lassen Sie solche Tests nach jeder kleinen Änderung an `driver.Driver` laufen,
dann erfahren Sie sofort, wann alles fertig ist.
"""

from datetime import datetime
from driver import Driver
import unittest


class DriverTests(unittest.TestCase):

    def test_exactly_zero(self):
        """
        Testet was passiert, wenn das Geburtsdatum und Referenzdatum
        bei der Altersbestimmung gleich sind.
        """

        # Tests haben immer die folgenden Teile:
        #  - Arrange: Vorbedingungen anlegen
        #  - Act: Zu testende Klasse oder Funktion ausführen
        #  - Assert: Effekte überprüfen

        # Arrange
        born = datetime(2018, 1, 1)
        today = datetime(2018, 1, 1)

        # System under Test
        driver = Driver("Test", "Tester", born)

        # Act
        age = driver.age(today)

        # Assert
        self.assertEqual(age, 0)

    def test_zero_something(self):
        born = datetime(2018, 1, 1)
        today = datetime(2018, 7, 1)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(today), 0)

    def test_almost_one(self):
        born = datetime(2018, 1, 1)
        today = datetime(2018, 12, 31)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(today), 0)

    def test_exactly_one(self):
        born = datetime(2018, 1, 1)
        today = datetime(2019, 1, 1)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(today), 1)

    def test_almost_eighteen(self):
        born = datetime(2000, 7, 15)
        today = datetime(2018, 7, 14)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(today), 17)

    def test_exactly_eighteen(self):
        born = datetime(2000, 7, 1)
        today = datetime(2018, 7, 1)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(today), 18)

    def test_born_feb_29_non_leap_years(self):
        born = datetime(2000, 2, 29)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(datetime(2017, 2, 28)), 16)
        self.assertEqual(driver.age(datetime(2017, 3, 1)), 17)

    def test_born_feb_29_leap_years(self):
        born = datetime(2000, 2, 29)

        driver = Driver("Test", "Tester", born)

        self.assertEqual(driver.age(datetime(2016, 2, 28)), 15)
        self.assertEqual(driver.age(datetime(2016, 2, 29)), 16)
