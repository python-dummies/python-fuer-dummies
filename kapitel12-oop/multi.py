#!/usr/bin/env python3
"""
Komposition
===========

Wenn Objekte eine Teile-Ganzes Beziehung bilden, ist es sinnvoll, nicht mit Vererbung, sondern stattdessen mit Komposition zu arbeiten.
"""

from pathlib import Path
import os
import platform


class MultiPurposeDevice:
    # Geben Sie mehrere kleine Objekte über den Konstruktor in ein
    # größeres Objekt ein,
    def __init__(self, printer, scanner, phone):
        # Speichern Sie die Argumente als Attribute.
        self._printer = printer
        self._scanner = scanner
        self._phone = phone

    def print(self, document):
        # Delegieren Sie die eigentliche Funktionalität an die Attribute
        self._printer.print(document)

    def scan(self):
        return self._scanner.scan()

    def copy(self):
        document = self._scanner.scan()
        return self._printer.print(document)

    def send_fax(self, recipient):
        document = self._scanner.scan()
        # Natürlich können Sie noch mehr anstellen
        # ...
        self._phone.send(document, recipient)

    def receive_fax(self):
        document = self._phone.receive()
        self._printer.print(document)


class Console:
    def print(self, document):
        print('Printing:', document)

    def scan(self):
        return input('Scanning: ')


class Phone:
    def send(self, document, recipient):
        pass

    def receive(self):
        pass


# Diese Klasse kümmert sich um alle Windows-spezifischen Details
class WindowsMyDocuments:
    def save(self, document):
        destination = Path.home() / 'Documents' / 'scan.txt'
        print("Saving to: ", destination)
        destination.write_text(document)


# Diese Klasse kümmert sich um alle Linux-spezifischen Details
class LinuxHomeDir:
    def save(self, document):
        destination = Path.home() / 'scan.txt'
        print("Saving to: ", destination)
        destination.write_text(document)


class FilePrinter:
    def __init__(self, windows, linux):
        self._windows = windows
        self._linux = linux

    def print(self, document):
        destination = (
            self._linux
            if platform.system() == 'Linux'
            else self._windows
        )

        name = destination.__class__.__name__
        destination.save(document)


if __name__ == '__main__':

    # Erzeugen Sie zuerst die kleinen Dienstobjekte
    console = Console()
    phone = Phone()

    # Fügen Sie das komplexere Objekt zusammen
    device = MultiPurposeDevice(
        printer=console,
        scanner=console,
        phone=phone
    )

    # Rufen Sie die übergeordnete Funktion auf
    device.copy()

    print_to_file = FilePrinter(
        windows=WindowsMyDocuments(),
        linux=LinuxHomeDir()
    )

    # Solange das Interface gleich ist, können Objekte gegeneinander
    # ausgetauscht werden -- mit etwas Geschick können Sie das
    # zur Laufzeit einstellen und sehr flexible Programme schreiben.
    device = MultiPurposeDevice(
        printer=print_to_file,
        scanner=console,
        phone=phone
    )
    device.copy()

    # Viele kleine Klassen und Objekte sind gut.
    # Wenige, große Klassen sind ein Zeichen dafür, dass Sie prozedural
    # Arbeiten und die Power von Objekten nicht voll ausnutzen.
    # Es ist ok, wenn ein Objekt nur eine Sache macht.
