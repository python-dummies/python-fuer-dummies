#!/usr/bin/env python3
"""
Wheel
=====

Ein nicht-intrusiver, visueller Timer.
Drücken Sie ESC, um den Timer zu beenden.

Der Timer läuft eine Stunde lang. Alle fünf Minuten wird ein Panel
geupdated. Nach 60 Minuten erklingt ein ein Erinnerungston.

Hier benutzen wir die Bibliothek QT, um eine kleine, grundlegende GUI
zu demonstrieren. Dabei werden viele Konzepte aus dem Buch erneut aufgegriffen.
"""
from pathlib import Path
from xml.dom import minidom
import os
import sys
import time

from PySide2 import QtSvg
from PySide2.QtMultimedia import QSound
from PySide2.QtCore import Qt, QPoint, QTimer, SIGNAL
from PySide2.QtGui import QImage, QPainter
from PySide2.QtWidgets import QApplication, QMainWindow, QAction


class Stopwatch:
    """
    Keeps track of time.
    During each tick of the clock, it measures how much time has passed.
    If the predefined time has elapsed, it emits an event and resets.
    """

    class Elapsed(Exception):
        """
        Event, which is fired when the Stopwatch timer elapsed.
        """

        def __init__(self, elapsed, *args, **kwargs):
            self.elapsed = elapsed
            super().__init__(*args, **kwargs)

    def __init__(self, interval_s):
        self._elapsed = 0
        self._interval_s = interval_s
        self._last_tick = None

    def tick(self):
        """
        When enough time has passed,
        fires a `Stopwatch.Elapsed` event
        """
        if not self._last_tick:
            # This hack avoids having a .start() method
            self._last_tick = time.time()
            return

        if (time.time() - self._last_tick) > self._interval_s:
            self._elapsed += 1
            self._last_tick = time.time()
            raise Stopwatch.Elapsed(self._elapsed)


class Wheel:
    """
    Represents a wheel.
    This abstracts the file "wheel.svg", which contains
    twelve paths, each representing a time segment of five minutes.
    """

    def __init__(self, svg, color_active, color_inactive):
        self._svg = svg
        self._color_active = color_active
        self._color_inactive = color_inactive
        self._segments = {
            path.getAttribute('id'): path
            for path in svg.getElementsByTagName('path')
        }

    def _fill_segment(self, svg_path, color):
        """
        Update SVG color value
        """
        svg_path.setAttribute('fill', color)

    def mute(self):
        """
        Set all panels to their inactive color
        """
        for segment in self._segments.values():
            self._fill_segment(segment, self._color_inactive)

    def activate(self, minute):
        """
        Activate a certain segment, based on a 5,10,15,... minute value
        """
        segment = self._segments.get(f'Segment{minute}')
        self._fill_segment(segment, self._color_active)

    def __bytes__(self):
        """
        Returns the updated SVG Data as UTF-8 encoded bytes
        """
        return self._svg.toxml('utf-8')

    @classmethod
    def from_svg_file(cls, svg_path, color_active, color_inactive):
        """
        Loads an SVG File and retunrs a new Wheel object
        """
        svg = minidom.parse(svg_path)
        return cls(svg, color_active, color_inactive)


class Sound:
    """
    Plays a sound
    """

    def __init__(self, path):
        self._path = path

    def trigger(self):
        QSound.play(self._path)


class Window(QMainWindow):
    """
    Displays a colored wheel.
    - ESC to exit
    - Drag and Drop to move around
    """

    def __init__(self, width, height, wheel, stopwatch, alert, app, *args, **kwargs):
        self._width = width
        self._height = height
        self._wheel = wheel
        self._stopwatch = stopwatch
        self._alert = alert
        self._app = app
        self._svg = None
        self._old_position = None
        super().__init__(*args, **kwargs)

    def show(self, *args, **kwargs):
        """
        Displays this window
        """
        # Transparent Background
        #
        # See: https://doc.qt.io/qt-5/qt.html#WindowType-enum
        # This combination works on Windows 10
        # Note: It may not work on Ubuntu...
        # Has Keyboard Focus
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        )

        # Not Sure if this is needed at all
        # window.setStyleSheet("background:transparent;")
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Load SVG Data
        self._svg = QtSvg.QSvgWidget(parent=self)
        self._redraw()

        # Adopt size
        self.resize(self._width, self._height)
        self._svg.resize(self._width, self._height)

        self._start_timer()

        super().show(*args, **kwargs)

    def keyPressEvent(self, event):
        """
        Handles key presses, e.g. ESC to Quit
        """
        if event.key() == Qt.Key_Escape:
            # self.close()
            self._app.quit()

    def mousePressEvent(self, event):
        """
        Handles start of Drag-and-Drop
        """
        self._old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        """
        Handles move during Drag-and-Drop
        """
        delta = QPoint(event.globalPos() - self._old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_position = event.globalPos()

    def _redraw(self):
        self._svg.load(bytes(self._wheel))

    def _update_time(self):
        try:
            self._stopwatch.tick()
        except Stopwatch.Elapsed as event:
            minute_segment = (event.elapsed * 5) % 65
            if not minute_segment:
                # Reset Wheel
                self._alert.trigger()
                self._wheel.mute()
            else:
                self._wheel.activate(minute_segment)

            self._redraw()
        except KeyboardInterrupt:
            # When the user presses Ctrl+C on their console
            # This is where the exception will be caught
            self.close()

    def _start_timer(self):
        timer = QTimer(self)

        # After the timer has elapsed,
        # Update the wheel
        self.connect(timer, SIGNAL('timeout()'), self._update_time)

        # Tick every 100ms
        timer.start(100)


class Color:
    BLUE = '#00b6ff'
    GREEN = '#b6ff00'
    ORANGE = '#ffb700'
    PINK = '#ff00b7'
    WHITE = '#ffffff'


class Size:
    HUGE = 1025
    LARGE = 512
    NORMAL = 256
    SMALL = 128
    TINY = 32
    ICON = 16


def main(args):
    app = QApplication(args)
    wheel = Wheel.from_svg_file(
        'wheel.svg',
        color_active=Color.GREEN,
        color_inactive=Color.BLUE
    )

    # Display the wheel in its deactivated colors
    wheel.mute()

    # Update panels every five minutes
    # Except when adding `debug` to the commandline,
    # which makes the clock run fast
    stopwatch = Stopwatch(
        interval_s=(0.1 if 'debug' in sys.argv else 5 * 60)
    )

    # This accepts any object with a .trigger() method.
    # You could easily configure this to send you an email,
    # lock your computer, or something else.
    # Windows users might find good alert sounds under
    # C:\Windows\Media\
    #
    # Default to local ting.wav
    alert = Sound('ting.wav')

    # Override on Windows
    if 'win' in sys.platform:
        c_windows = Path(os.getenv('SYSTEMROOT'))
        path = c_windows/'Media'/'Alarm02.wav'
        if path.exists():
            alert = Sound(str(path))

    # Set to sensible size
    width = height = Size.SMALL
    window = Window(
        width=width,
        height=height,
        stopwatch=stopwatch,
        wheel=wheel,
        alert=alert,
        app=app
    )
    window.show()

    # To suppress the console, start the program with
    # $ pythonw program.py
    print("Press ESC to quit.")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
