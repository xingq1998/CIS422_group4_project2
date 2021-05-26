from django.shortcuts import render
from .models import Item

# Create your views here.


def all(request):
    categories = []
    products = Item.objects.all()

    for prod in products:
        if prod.category not in categories:
            #print(prod.category)
            categories.append(prod.category)

    #print(categories)
    return render(request, 'product/all.html', {"products" : products, "categories" : categories})


#---------- Search Functions ----------#


def product_search(request):
    products = Item.objects.all()
    categories = []

    for prod in products:
            if prod.category not in categories:
                categories.append(prod.category)

    if request.method == 'POST':
        post_dict = request.POST
        search_cat = post_dict.get("category", "")

        products = Item.objects.all().filter(category=search_cat)

        return render(request, 'product/all.html', {"products" : products, "categories" : categories})

    else:
               
        return render(request, 'product/all.html', {"products" : products, "categories" : categories})

