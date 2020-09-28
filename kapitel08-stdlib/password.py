#!/usr/bin/env python3
"""
Password Generator
==================

Erzeugt zufällige Passwörter.

Beispiel:

 $ python3 password.py

 $ python3 password.py 24

"""
import sys
import string
import secrets
try:
    LENGTH = int(sys.argv[1])
except:
    LENGTH = 16

alphabet = string.ascii_letters + string.digits + '%^#$!#?='
password = ''.join(secrets.choice(alphabet) for _ in range(LENGTH))
print(password)