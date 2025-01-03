from django.shortcuts import render
from .models import TravelPackage

def home(request):
    packages = TravelPackage.objects.all()
    return render(request, 'travel_packages/home.html', {'packages': packages})