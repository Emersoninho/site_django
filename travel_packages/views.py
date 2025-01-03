from django.shortcuts import render
from .models import TravelPackage

def home(request):
    packages = TravelPackage.objects.all()
    return render(request, 'travel_packages/home.html', {'packages': packages})

def black_friday(request):
    packages = TravelPackage.objects.all().order_by('discounted_price')
    return render(request, 'travel_packages/black_friday.html', {'packages': packages})