#!/usr/bin/env python3
"""
Ohne Index auf Daten zugreifen -- Nutzen Sie "unpacking"
"""

numbers = [1,2,3,4,5]
first, *middle, last = numbers
print('    first == numbers[0]:', first == numbers[0])
print('    last == numbers[-1]:', last == numbers[-1])
print('middle == numbers[1:-1]:', middle == numbers[1:-1])
