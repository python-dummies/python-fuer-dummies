#!/usr/bin/env python3
"""
Mailbox: Senden
===============

Schickt eine Email

Hinweis: Passen Sie HOSTNAME und PORT an.
"""

# Bibliothek zum verschicken
import smtplib

# Passwort maskiert einlesen
import getpass

HOSTNAME = 'smtp.example.com'
PORT = 587

user = input('User:')
password = getpass.getpass('Password:')

with smtplib.SMTP(HOSTNAME, PORT) as smtp:

    # Verbindung verschlüsseln
    smtp.starttls()

    # Login
    smtp.login(user, password)

    # Nachricht schreiben und versenden
    smtp.sendmail(
        input('From: ').strip() or user,
        input('To: '),
        input('Message: ')
    )
