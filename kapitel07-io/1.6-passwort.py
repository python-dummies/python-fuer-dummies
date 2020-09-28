#!/usr/bin/env python3
"""
Passwörter einlesen
===================

Sensible Daten sollten Sie maskieren. Dafür gibt es die Funktion `getpass`:
"""

from getpass import getpass
password = getpass("Password: ")
quality = 'ok' if len(password) > 8 else 'too short'
print(f"That password is {quality}")
