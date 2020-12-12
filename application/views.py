from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def home(request):
    return render(request, 'home1.html')

def add(request):
    user = User()
    user.name = request.POST['nm']
    user.save()
    return redirect('../')

