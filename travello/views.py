from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello</h1>")
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'dcfgvhbjk'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Goa'
    dest2.desc = 'rtyuio'
    dest2.img = 'destination_2.jpg'
    dest2.price = 1000
    dest2.offer = True

    dests = [dest1,dest2]
    return render(request, 'index.html', {'dests':dests})

    # return render(request, 'index.html', {'dest1':dest1, 'dest2': dest2})
