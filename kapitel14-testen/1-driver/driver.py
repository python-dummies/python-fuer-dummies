#!/usr/bin/env python3
"""
Driver
======

Zu testende Komponente.
Leider ist sie nocht nicht komplett korrekt.
"""
from datetime import datetime
import math


class Driver:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def age(self, today=None):
        today = today or datetime.today()
        time_alive = today - self.birthdate
        return math.floor(time_alive.days / 365.25)
