#!/usr/bin/env python3
"""
Zahlen konvertieren
===================

Zahlen (bzw. elementare Datentypen) können flexibel ineinander konvertiert
werden.
"""

print('Ints und Floats:')
f = 3.1415
print(f, '-->', int(f))
i = 3
print(i, '-->', float(i))


# Leider haben wir dafür keinen Anwendungsfall
print(complex(4,3))

print()
print('Bool:')
print('       bool():', bool())
print('      bool(0):', bool(0))
print('      bool(1):', bool(1))
print('     bool(-4):', bool(-4))
print('     bool([]):', bool([]))
print('bool([1,3,4]):', bool([1,3,4]))

print()
print('Int mit Basis:')
print("   int(19.95):", int(19.95))
print("   int('111'):", int('111'))
print("int('111', 2):", int('111', 2))
print("int('ff', 16):", int('ff', 16))

print()
print('Floats:')
print("   float('3.1415'):", float('3.1415'))
print("  float('+356E-6'):", float('+356E-6'))
print("float('-Infinity'):", float('-Infinity'))

print()
print('Explizite Ints')
print(' bin(777):', bin(777))
print('  oct(25):', oct(25) )
print(' hex(255):', hex(255))
# Oder als Literal:
print('0b0101010:', 0b0101010)

print()
print('Zahlen in String verwandeln:')
print("format(7, 'b'):", format(7, 'b'))
print("      ord('A'):", ord('A'))
print("     chr(8364):", chr(8364))
x = 5
print("        str(x):", str(x))
