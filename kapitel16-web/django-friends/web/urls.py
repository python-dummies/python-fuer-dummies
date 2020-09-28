from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('person/<int:pk>', views.Person.as_view(), name='person'),
    path('person/create', views.CreatePerson.as_view(), name='create'),
    path('person/delete/<int:pk>', views.DeletePerson.as_view(), name='delete'),
    path('person/update/<int:pk>', views.UpdatePerson.as_view(), name='update'),
    path('person/update/<int:pk>/email/create', views.CreateEmail.as_view(), name='create-email'),
    path('person/update/<int:person_pk>/email/delete/<int:pk>', views.DeleteEmail.as_view(), name='delete-email'),
    path('people.csv', views.CommaSeparatedValues.as_view(), name='csv')
]
