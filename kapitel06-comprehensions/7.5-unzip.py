#!/usr/bin/env python3
"""
Eine Liste mit gepaarten Elemente in separate Listen zerlegen
-- nutzen Sie `zip`
"""

# Reißverschlussverfahren umgedreht: Sie haben eine Liste mit Schlüsseln und
# Werten und möchten diese in zwei Listen auftrennen

# Vorbereitung
contacts = [
    ('Annie Easley', 'a.easley@example.com'),
    ('Margaret Hamilton', 'm.hamilton@example.com'),
    ('Barbara Liskov', 'b.liskov@example.com'),
]


# Pythonic
# Achten Sie auf das Sternchen!
names, emails = zip(*contacts)


# Ausgabe:
print(names)
print(emails)


# Nicht pythonic
names = [None] * len(contacts)
emails = [None] * len(contacts)
for i in range(len(contacts)):
    names[i] = contacts[i][0]
    emails[i] = contacts[i][-1]


# Ausgabe
print(names)
print(emails)
