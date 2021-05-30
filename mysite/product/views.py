from django.shortcuts import render
from .models import Item, Size



def all(request):
    # The view for all shop products.
    categories = []
    products = Item.objects.all()

    # Filter distinct categories from all Items. 
    for prod in products:
        if prod.category not in categories:
            categories.append(prod.category)

    return render(request, 'product/all.html', {"products" : products, "categories" : categories})


#---------- Search Functions ----------#


def product_search(request):
    # Populate categories for drop-down list; need this if POST or not
    products = Item.objects.all()
    categories = []

    for prod in products:
            if prod.category not in categories:
                categories.append(prod.category)

    # If method is POST, user has selected filters
    if request.method == 'POST':
        # Get filter options from request
        post_dict = request.POST
        search_cat = post_dict.get("category", "")
        search_size = post_dict.get("size_type", "")

        # Sort based on filters chosen
        # Omit unavailable inventory
        products = Item.objects.filter(category=search_cat, size__size_type=search_size, size__quantity__gte=0, total_stock__gte=0)

        # Render results
        return render(request, 'product/all.html', {"products" : products, "categories" : categories})

    else:
        # By default, we show all options (out of stock or not)
        return render(request, 'product/all.html', {"products" : products, "categories" : categories})

