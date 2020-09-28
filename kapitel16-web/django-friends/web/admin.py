from django.contrib import admin

from . import models

admin.site.register(models.Person)


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email_address', 'person', 'category']
