from django.shortcuts import render
from .models import Item

# Create your views here.

def all(request):
    categories = []
    products = Item.objects.all()

    for prod in products:
        if prod.category not in categories:
            print(prod.category)
            categories.append(prod.category)

    print(categories)
    return render(request, 'product/all.html', {"products" : products, "categories" : categories})