from django.shortcuts import render, get_object_or_404
from .models import TravelPackage

def home(request):
    packages = TravelPackage.objects.all().order_by('-id')
    return render(request, 'travel_packages/home.html', {'packages': packages})

def black_friday(request):
    packages = TravelPackage.objects.all().order_by('discounted_price')
    return render(request, 'travel_packages/black_friday.html', {'packages': packages})

def package_detail(request, id):
    package = get_object_or_404(TravelPackage, id=id)
    return render(request, 'travel_packages/package_detail.html', {'package': package})