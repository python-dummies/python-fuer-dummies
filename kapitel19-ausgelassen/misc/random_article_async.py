"""
Async IO
========

Gibt mehrere zufällige Artikel der Wikipedia aus.

Threading geht in Python nicht richtig, denn da steht der
"Global Interpreter Lock" im Weg.

Sie können jedoch asynchrone IO verwenden. Dabei wird ein Thread gestartet.
Sobald dieser Thread Daten aus einer langsamen Ressource, etwa dem Netzwerk,
lädt, macht der Thread mit anderen Verarbeitungsaufgaben weiter.

Ob das Ihr Programm beschleunigt, hängt davon ab, ob Ihr Programm ständig mit
IO beschäftigt ist. Wenn Ihr Programm hauptsächlich rechnen muss, ist
Multiprocessing besser geeignet (das Verteilen von Prozessen auf mehrere
CPU-Kerne).

Zusätzlich demonstriert dieses Programm einen eigenen klassenbasierten Iterator.
Im Hintergrund werden mehrere Daten abgefragt, aber der aufrufende
Code bekommt davon nichts mit.
"""
import json
import time
import requests
import multiprocessing


URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


def title(json_string):
    return json.loads(json_string).get('title')


def download(*args):
    return requests.get(URL).content


class RandomArticles:
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        with multiprocessing.Pool() as pool:
            future_results = [
                pool.apply_async(download)
                for _ in range(self._n)
            ]
            for result in future_results:
                yield result.get()


class Stopwatch:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *args):
        end = time.time()
        elapsed = end - self._start
        print(f'{elapsed:.2f}s')


if __name__ == '__main__':
    N = 20
    print("Seriell")
    print("=======")
    with Stopwatch():
        # 14 Sekunden seriell
        for _ in range(N):
            print(title(download()))
        print()

    print()
    print("Parallel (Async-IO)")
    print("===================")
    with Stopwatch():
        # 2 Sekunden parallel
        for article in RandomArticles(N):
            print(title(article))
        print()
