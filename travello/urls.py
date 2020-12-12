from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    
]
# workon project
# python manage.py runserver