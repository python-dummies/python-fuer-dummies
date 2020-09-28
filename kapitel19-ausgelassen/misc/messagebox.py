"""
Externe C-Funktionen
====================

In Pyhon kann man externe C-Funktionen aufrufen.

Im Beispiel rufen wir eine Standard-Funktion unter Windows auf.
Diese konkrete Funktion gibt es natürlich nicht unter Linux/macOS,
aber auch dort kann man natürlich Python mit C-Programmen verknüpfen.
"""

import os

if not os.name == 'nt':
    print("This program won't work under Linux. Watch:")

from ctypes import WinDLL
user32 = WinDLL('user32.dll')

window_handle = 0
MB_ICONASTERISK = 0x00000040
MB_TOPMOST = 0x00040000

user32.MessageBoxA(
    window_handle,
    b'Knowledge brings fear!',
    b'Mars University',
    MB_ICONASTERISK | MB_TOPMOST
)