from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('addd',views.add, name='add')
]
# workon project
# python manage.py runserver
# python manage.py collectstatic