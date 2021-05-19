#from mysite import product
from django.shortcuts import render
from .models import Item

# Create your views here.

def all(request):
    products = Item.objects.all()
    return render(request, 'product/all.html', {"products" : products})