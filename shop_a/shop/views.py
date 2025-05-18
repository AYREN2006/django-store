from django.shortcuts import render
from .models import Mobile, Laptop, TV

def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'shop/mobile_list.html', {'mobiles': mobiles})

def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'shop/laptop_list.html', {'laptops': laptops})

def tv_list(request):
    tvs = TV.objects.all()
    return render(request, 'shop/tv_list.html', {'tvs': tvs})
    