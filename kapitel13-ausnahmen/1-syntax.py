#!/usr/bin/env python3
"""
Syntax
======

Erläutert die Syntax von try-except-finally
"""

try:
    a = int(input('> '))
    b = int(input('> '))
    result = a / b
except ValueError:
    # Wird ausgegeben, wenn Sie einen Text eingeben, statt Zahlen
    print('Please provide a valid number')
except ZeroDivisionError:
    # Wird ausgegeben, wenn Sie als zweites eine Null (0) eingeben.
    print('Division by zero!')
else:
    # Wenn keine Exception aufgetreten ist
    print(result)
finally:
    # Wird auf jeden Fall ausgegeben.
    print("Fertig")