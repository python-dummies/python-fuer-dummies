#!/usr/bin/env python3
"""
Mailbox
=======

Fragt Emails ab und gibt sie auf der Konsole aus.

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

# Wie viele Emails sollen gezeigt werden?
LIMIT = 10

# Diese Daten müssen Sie anpassen, z.B. imap.gmail.com, wenn Sie einen
# Googlemail Account haben. Port 993 ist meist für gesicherte Verbindungen.
HOSTNAME = 'imap.example.com'
PORT = 993

user = input('User:')
password = getpass.getpass('Password:')

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

    for mail_id in mail_ids:

        # Maildaten abholen
        status, response = imap.fetch(mail_id, '(RFC822)')
        (flags, message_bytes), _ = response

        # Rohdaten in ein Objekt konvertieren
        message = email.message_from_bytes(message_bytes)

        # Email ausgeben
        print(
            message.get('from'),
            message.get('subject')
        )
