from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  UpdateView, ListView)
from django.urls import reverse_lazy
from django.http import HttpResponse

import csv
import datetime

from . import models


class Index(ListView):
    model = models.Person
    context_object_name = 'people'
    ordering = 'last_name'

    def get_ordering(self):
        return self.request.GET.get('order_by', self.ordering)


class Person(DetailView):
    model = models.Person
    context_object_name = 'person'


class CreatePerson(CreateView):
    model = models.Person
    fields = ('first_name', 'last_name', 'birthday')
    success_url = reverse_lazy('index')


class DeletePerson(DeleteView):
    model = models.Person
    context_object_name = 'person'
    success_url = reverse_lazy('index')


class UpdatePerson(UpdateView):
    model = models.Person
    fields = ('first_name', 'last_name', 'birthday')
    context_object_name = 'person'


class CreateEmail(CreateView):
    model = models.Email
    fields = ('email_address', 'category')

    def form_valid(self, form):
        person = models.Person.objects.get(pk=self.kwargs['pk'])
        form.instance.person = person
        return super(CreateEmail, self).form_valid(form)

    def get_context_data(self, **kwargs):
        person = models.Person.objects.get(pk=self.kwargs['pk'])
        context = super(CreateEmail, self).get_context_data(**kwargs)
        context['person'] = person
        return context


class DeleteEmail(DeleteView):
    model = models.Email

    def get_success_url(self):
        return reverse_lazy('person', kwargs={'pk': self.kwargs['person_pk']})


class CommaSeparatedValues(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="people.csv"'

        writer = csv.writer(response)

        # Write Header
        header_row = [
            'Vorname', 'Nachname', 'Geburtstag', 'Email', 'Kategorie'
        ]
        writer.writerow(header_row)

        # Write Rows
        for person in models.Person.objects.all():
            email = person.emails.first() or models.Email()
            row = [
                person.first_name,
                person.last_name,
                datetime.datetime.strftime(person.birthday, '%d.%m.%Y'),
                email.email_address,
                email.get_category_display(),
            ]
            writer.writerow(row)

        return response
