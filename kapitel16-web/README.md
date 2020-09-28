Django Friends
==============

Dieses kleine Projekt demonstriert eine datenzentrierte Webseite,
die mit Django gebaut wurde.

Um Sie zu betrachten, gehen Sie wie folgt vor:

1. Datenbank anlegen
--------------------

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

2. Server starten
-----------------

    $ python3 manage.py runserver

3. Browser öffnen
-----------------

Navigieren Sie nach

    http://localhost:8000


Bonus
-----

Betrachten Sie auch die Redaktionsoberfläche!

1. Admin erstellen
------------------

    $ python3 manage.py createsuperuser


2. Einloggen
------------

Navigieren Sie nach

    http://localhost:8000/admin

Loggen Sie sich mit den Daten ein, die Sie im Schritt "createsuperuser"
angegeben haben.

Mehr zu Django erfahren Sie offiziellen Django Tutorial:

https://docs.djangoproject.com/en/3.0/intro/tutorial01/