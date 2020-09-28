#!/usr/bin/env python3
"""
Mailbox XXL
===========

Fragt Emails ab und gibt sie auf der Konsole aus.
Auch der Body der Email wird angezeigt

Hinweis: Passen Sie HOSTNAME und PORT an.

"""

# Emails vom Server abfragen
import imaplib
# Entschuldigen Sie bitte:
# In Kapitel 8 im Abschnitt 'imaplib - Emails versenden'
# im Listing `mailbox.py` steht hier fälschlicher Weise `from imaplib`

# Rohe-Emails lesen
import email

# Maskierte Passwortabfrage
import getpass

# Text kurzfassen
import textwrap

# Wie viele Emails sollen gezeigt werden?
LIMIT = 10

# Diese Daten müssen Sie anpassen, z.B. imap.gmail.com, wenn Sie einen
# Googlemail Account haben. Port 993 ist meist für gesicherte Verbindungen.
HOSTNAME = 'imap.example.com'
PORT = 993

# Nutzernamen abfragen
user = input('User:')

# Passwort maskiert einlesen
password = getpass.getpass('Password:')


def body(message):
    '''
    Liest den Text-Inhalt einer Email-Nachricht aus.
    '''

    # Entschuldigung, ab hier wird es etwas hässlich.
    # Emails sind sehr alt, daher ist das etwas unschön.
    # Konsultieren Sie das Manual:
    #
    # https://docs.python.org/3/library/email.examples.html
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            try:
                body = part.get_payload(decode=True)
                if body:
                    return body.decode()
            except:
                pass
    else:
        content_type = message.get_content_type()
        body = message.get_payload(decode=True).decode()

    # Text aus HTML Emails extrahieren
    if content_type == "text/html":
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(body, 'lxml')
            return soup.body.text
        except:
            return ''


# Verbindung aufbauen
with imaplib.IMAP4_SSL(HOSTNAME, PORT) as imap:

    # Authentifizierung
    imap.login(user, password)

    # Standard-Postfach auswählen
    imap.select()

    # Alle Mails selektieren
    status, mails = imap.search(None, 'ALL')

    # IDs kommen als String zurück - zerlegen!
    mail_ids = mails[0].split()

    # Sortieren und begrenzen
    mail_ids = list(reversed(mail_ids))[:LIMIT]

    for i, mail_id in enumerate(mail_ids, start=1):

        # Maildaten abholen
        status, response = imap.fetch(mail_id, '(RFC822)')
        (flags, message_bytes), _ = response

        # Rohdaten in ein Objekt konvertieren
        message = email.message_from_bytes(message_bytes)

        # Inhalt interpretieren
        content = body(message)

        # Text zur Vorschau abkürzen
        preview = textwrap.shorten(content, width=80, placeholder='...')

        # Email ausgeben
        print()
        print(f'Email {i}')
        print('---------')
        print('    Von:', message.get('from'))
        print('Betreff:', message.get('subject'))
        print(' Inhalt:', preview)
