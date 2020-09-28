#!/usr/bin/env python3
"""
Variablen in Texten anzeigen
=============================

Es gibt die verschiedensten Möglichkeiten, um Variablen in Texte einzufügen.
"""


# Strings aneinanderhängen (concatenate)
# ======================================
from datetime import datetime
today = datetime.today()

# Mikrosekunden abschneiden
now = today.time().replace(microsecond=0)

# Name des Tages: z.B. "Monday"
day = today.strftime("%A")

print('Concat: ')
print("It is " + str(now) + " on a " + day)


# C-Syntax (wie printf)
# =====================
print('printf-Syntax: ')
print("It is %s on a %s" % (now, day))


# str.format
# ==========
print("str.format()")
print("It is {} on a {}".format(now, day))
print("It is {1} on a {0}".format(day, now))
print("It is {time} on a {day}".format(time=now, day=day))

# Das muss nicht alles in einer Zeile geschehen:
variables = {
    'time': now,
    'day': day
}
print("It is {time} on a {day}".format(**variables))


# f-strings (format-Strings)
# ==========================
# Der bevorzugte Weg.
print('f-strings:')
print(f"It is {now} on a {day}")
# Beachten Sie das kleine f VOR den Anführungsstrichen.
# Wenn Sie die vergessen, passiert Nichts:
print("It is {now} on a {day}")
