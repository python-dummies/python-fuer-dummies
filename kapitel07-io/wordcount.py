#!/usr/bin/env python3
"""
Datei als Argument übergeben (pipen)
====================================

Beispiel:

 # bash
 $ head haikus.txt -n 3 | python3 wordcount.py

 # powershell
 $ gc haikus.txt -head 3 | python wordcount.py

"""
import sys


def word_count(line):
    return len(line.strip().split(' '))


# Zeilenweise von STDIN lesen
count = sum(
    word_count(line) for line in sys.stdin.readlines()
)

# Das macht hier das gleiche wie `print`.
sys.stdout.write(
    f'Number of Words: {count}'
)
