#!/usr/bin/env python3
"""
Hotelbuchung
============

Ablaufsteuerung mit Ausnahmen.

Mit Ausnahmen können Sie geschickt eine State-Machine abbilden.
Das Programm stellt nacheinander Fragen, bis diese vollständig
beantwortet wurden.
"""
import datetime


class Back(Exception):
    """
    Nachricht, die auf eine vorherige Frage zurückspringt
    """
    pass


class Exit(Exception):
    """
    Nachricht, die das Programm beendet
    """
    pass


class Hint(Exception):
    """
    Nachricht, die auf Fehleingaben hinweist
    """
    pass


class Restart(Exception):
    """
    Nachricht, die den Dialog neu startet
    """
    pass


def number(string):
    """
    Prüft, ob eine Eingabe eine gültige Zahl beinhaltet.
    Falls nicht, wird ein Hinweis ausgegeben.
    """
    try:
        number = int(string)
        if not 0 < number <= 10:
            raise ValueError
    except ValueError:
        raise Hint('Please provide a number between 1 and 10')
    else:
        return number


def arrival(string):
    """
    Prüft, ob eine Eingabe ein gültiges Ankunftsdatum ist.
    Falls nicht, wird ein Hinweis ausgegeben.
    """
    try:
        date = datetime.datetime.strptime(string, '%d.%m.%Y').date()
        if date < datetime.date.today():
            raise Hint('Arrival date can not be in the past')
    except ValueError:
        raise Hint('Please provide a valid date (dd.mm.yyyy)')
    else:
        return date


def departure(string):
    """
    Prüft, ob eine Eingabe ein gültiges Abreisedatum ist.
    Falls nicht, wird ein Hinweis ausgegeben.
    """
    try:
        date = datetime.datetime.strptime(string, '%d.%m.%Y').date()
        if date < datetime.date.today():
            raise Hint('Depature date can not be in the past')
    except ValueError:
        raise Hint('Please provide a valid date (dd.mm.yyyy)')
    else:
        return date


class City:
    """
    Prüft, ob eine Eingabe eine gültige Stadt bezeichnet.
    Falls nicht, wird ein Hinweis ausgegeben.

    Hinweis: Objekte dieser Klasse verhalten sich wie Funktionen.
    """

    def __init__(self, cities):
        self._cities = cities

    def __call__(self, city):
        """
        Trick 17: Durch diese Methode können Objekte dieser Klasse
        wie Funktionen behandelt werden.
        """
        if city in self._cities:
            return city

        cities_available = ', '.join(self._cities)
        raise Hint(f'Our hotels are located at {cities_available}')


class Question:
    """
    Stellt Nutzern eine Frage und wertet die Antwort aus.

    Falls die Antwort nicht die richtigen Bedingungen erfüllt,
    wird die Frage erneut gestellt.

    Durch Eingabe von "exit", "restart" oder "back" kann der Ablauf
    des Dialogs gesteuert werden.
    """

    def __init__(self, question, evaluate_answer):
        self._question = question
        self._evaluate_answer = evaluate_answer

    def ask(self):
        while True:

            # Frage ausgeben
            print(self._question)

            # Antwort annehmen
            answer = input('> ').strip()

            # Leere Antwort? Nochmal nachgehakt!
            if not answer:
                continue

            # Eine Frage zurück
            if 'back' in answer:
                raise Back

            # Neustart
            if 'restart' in answer:
                raise Restart

            # Abbruch
            if 'exit' in answer:
                raise Exit

            try:
                return self._evaluate_answer(answer)
            except Hint as hint:
                # Wenn die Frage nicht richtig beantwortet wurde
                # wird ein Hinweis ausgegeben und die Frage nochmal gestellt.
                print(hint)


class Dialogue:
    """
    Stellt alle Fragen bis zur vollständigen Beantwortung
    und gibt diese als Dictionary zurück.

    Steuert den Ablauf.
    """

    def __init__(self, **questions):
        self._questions = questions

    def engage(self):
        answers = {}

        # Die Fragen werden richtig herum aufgeschrieben.
        # Wir verwenden im folgenden die Liste als Stapelspeicher (Stack)
        # Daher müssen wir sie umkehren, sodass die erste Frage "oben"
        # auf dem Stapel liegt.
        todo = list(reversed(list(self._questions.items())))
        done = []

        # Solange noch Fragen auf dem "todo"-Stapel liegen,
        # werden diese gestellt und danach auf den "done" Stapel gelegt.
        while todo:

            # Frage vom Stapel ziehen.
            name, question = todo.pop()
            try:
                # Frage stellen
                answers[name] = question.ask()
            except KeyboardInterrupt:
                # Umwegloser Abbruch des Programms
                # durch Drücken von Strg+C -- für Notfälle
                raise Exit
            except Back:
                # Eine Frage zurückspringen
                todo.append((name, question))
                if not done:
                    continue
                todo.append(done.pop())
            except Restart:
                # Von vorne anfangen
                todo.append((name, question))
                todo = todo + list(reversed(done))
                done = []
            else:
                # Kein fehler trat auf?
                # Dann wird die Frage auf den "Fertig"-Stapel gelegt
                done.append((name, question))

        # Sobald der "todo"-Stapel leer ist, können die gesammelten
        # Antworten zurückgegeben werden
        return answers


class Booking:
    """
    Formatiert ein Dictionary mit beantworteten Fragen als Hotelbuchung.
    """

    def __init__(self, dictionary):
        self._dictionary = dictionary
        self._dictionary['nights'] = self._nights(dictionary)

    def _nights(self, dictionary):
        return (
            (dictionary['departure'] - dictionary['arrival']).days
        )

    def print(self):
        for key, value in self._dictionary.items():
            # str.title formatiert z.B. "guests" in "Guests"
            key = key.title()
            value = str(value)
            print(f'{key:.<15}....{value:.>20}')


if __name__ == '__main__':
    """
    Hier sehen Sie den Vorteil einer Komposition.
    Alle Nutzdaten können an dieser Einstiegsstelle
    definiert werden. Sie erfahren auf einen Blick, was das Programm tut.
    """
    city = City([
        'Heidelberg', 'Mannheim', 'Frankfurt', 'Berlin'
    ])

    # Der Dialog nimmt eine beliebige Anzahl an Fragen an.
    # Wenn Ihnen noch eine einfällt, müssen Sie hier lediglich ein neues Objekt
    # hinzufügen.
    dialogue = Dialogue(
        location=Question('Where would you like to stay?', city),
        guests=Question('How many guests will be visiting?', number),
        arrival=Question('Date of arrival (dd.mm.yyyy)?', arrival),
        departure=Question('Date of departure (dd.mm.yyyy)?', departure),
        name=Question('Please give us a name for the reservation:', str),
    )

    print('Welcome to Schneider-Hofmeister Resort Hotels')
    print('~' * 45)
    try:
        # Hier wird der Dialog direkt gestartet.
        booking = Booking(dialogue.engage())
    except Exit:
        print('Your booking has been canceled.')
    else:
        print('Your booking Summary: ')
        booking.print()
        print('Your booking was accepted!')
    print('Have a nice day!')
