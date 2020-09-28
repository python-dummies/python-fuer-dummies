#!/usr/bin/env python3
"""
age
===

Dieses Programm soll das alter eines Fahrschülers bestimmen.
Leider funktioniert es nicht.
"""
from datetime import datetime
import math


class Driver:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def age(self):
        time_alive = datetime.today() - self.birthdate
        return math.floor(time_alive.days / 365.25)
