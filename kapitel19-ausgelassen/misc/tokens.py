"""
Walross-Operator
================

Zerlegt einen Text in seine Einzelteile.

In der Community wurde hitzig über den Walrus-Operator diskutiert.
Eine Zuweisung ist eine Anweisung -- deren Ergebnis ist immer ein Seiteneffekt,
also dass NACH dem Durchführen der Anweisung eine Variable da ist.

Die Zuweisung hat aber keinen Rückgabewert.

Der Walross-Operator hingegen hat auch einen Rückgabewert, sodass sich manche
Codes vereinfachen lassen. Etwa kann geprüft werden, ob eine Zuweisung geklappt
hat.
"""
import string
text = """Als ich vor einigen Jahren – wie lange es genau her ist, tut wenig zur Sache –
so gut wie nichts in der Tasche hatte und von einem weiteren Aufenthalt auf dem
Lande nichts mehr wissen wollte, kam ich auf den Gedanken, ein wenig zur See zu
fahren, um die Welt des Meeres kennenzulernen. Man verliert auf diese Weise
seinen verrückten Spleen, und dann ist es auch gut für die Blutzirkulation.
Wenn man den scheußlichen Geschmack auf der Zunge nicht loswerden kann; wenn
man das Frostgefühl eines feuchten und kalten Novembers auf der Seele hat; wenn
man unwillkürlich vor jedem Sargmagazin stehenbleibt und jedem Leichenzug
nachsieht, wenn man sich der Schwermut nicht mehr erwehren kann, daß man auf
die Straße stürzen und vorsätzlich den Leuten den Hut vom Kopfe schlagen müßte,
dann ist es allerhöchste Zeit, auf See zu gehen.
"""


alphabet = string.ascii_letters + 'äöüÄÖÜß'

EndOfFile = -1


def tokenize(iterator):
    buffer_ = []
    try:
        # Walross-Operator
        # Ohne := müsste man außerhalb der Schleife erst
        # in einer separaten Zeile den ersten Buchstaben einlesen
        while (c := next(iterator)) in alphabet:
            buffer_.append(c)
        return ''.join(buffer_)
    except StopIteration:
        return EndOfFile


if __name__ == '__main__':
    iterator = iter(text)

    # Walross-Operator
    # Ohne := müsste man außerhalb der Schleife erst
    # in einer separaten Zeile das erste Token einlesen
    while (token := tokenize(iterator)) != EndOfFile:
        if token.strip():
            print(token)
