#!/usr/bin/env python3
"""
Webseiten testen
================

 $ python3 ping.py https://example.com

"""
import sys
from urllib import request

try:
    _, url = sys.argv
except ValueError:
    print('Bitte url angeben, z.B. https://example.com')
    exit()

try:
    request.urlopen(url)
    print("Up and running!")
except:
    print("Seems to be down!")
