#!/usr/bin/env python3
"""
Gimmick: iostream
=================

Seien sie vorsichtig mit kreativen Operator-Überladungen.
Sie können Operatoren so überladen, dass sie aussehen wie in C++.
Ob Sie das *sollten* ist eine andere Frage...
"""

endl = '\n'


class Stream:
    _buffer = []

    def __lshift__(self, text):
        self._buffer.append(text)
        if text is endl:
            print(''.join(self._buffer))
            self._buffer.clear()
        return self


cout = Stream()

if __name__ == '__main__':

    cout << 'Hello, World! ' << 'How are you doing?' << endl;

    # Es ist übrigens erlaubt, eine Zeile mit einem Semikolon zu beenden.
    # Das sollten Sie aber unterlassen :)