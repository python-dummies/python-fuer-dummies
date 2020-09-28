from django.urls import reverse_lazy
from django.db import models
from django.utils import timezone
import math


class Person(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('person', args=(self.id,))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        if not self.birthday:
            return
        time_alive = self.birthday - timezone.now().today().date()
        return math.floor(abs(time_alive.days) / 365.25)

    def is_born_today(self):
        if not self.birthday:
            return
        today = timezone.now().today().date()
        return (
            (self.birthday.day, self.birthday.month) == (today.day, today.month)
        )


email_categories = [
    (1, "🏭 Arbeit"),
    (2, "🏠 Privat"),
    (3, "⭐ Hauptadresse"),
]


class Email(models.Model):
    email_address = models.EmailField(
        max_length=512, null=False, blank=False, unique=True
    )
    person = models.ForeignKey(
        Person, null=False, blank=False, on_delete=models.CASCADE,
        related_name='emails'
    )
    category = models.SmallIntegerField(choices=email_categories)

    def __str__(self):
        return f'{self.email_address}'

    def get_absolute_url(self):
        return reverse_lazy('person', args=(self.person.id,))
