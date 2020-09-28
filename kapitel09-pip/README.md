Pip: Pip installiert Pakete
===========================

In diesem Kapitel gibt es keinen Code, nur Schnipsel für die Kommandozeile.

Rufen Sie auf der Kommandozeile den Paketmanager pip auf, indem Sie unter Windows `pip`, unter Linux `pip3` eingeben.

Pip Updaten
-----------

    $ python3 -m pip install --upgrade pip

Ein Paket installieren
----------------------

    $ pip3 install requests

Ein installiertes Paket updaten
-------------------------------

    $ pip3 install requests --upgrade

Mehrere Pakete installieren
---------------------------

Füllen Sie eine Datei mit den gewünschten Paketnamen:

```
pillow
request
django
```

Installieren Sie die Pakete mit Pip:

    $ pip3 install -r requirements.txt

Paketliste erstellen
====================

Wenn Sie bereits installierte Pakete sammeln möchten, um eine Paketdatei
zu erstellen, können Sie `pip freeze` nutzen:

    $ pip3 freeze > requirements.txt

So legen Sie auch konkrete Versionen fest.