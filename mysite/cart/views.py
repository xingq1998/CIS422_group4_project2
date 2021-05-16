from django.shortcuts import render
from django.http import HttpResponse
from .models import CartItem


def index(request):
    return HttpResponse("Hello, world. You're at the cart index.")


def cartInsert(request):
    instances = [CartItem(name='Un Jardin sur la Lagune Eau de toilette', price=230, quantity=1, user_id=1),
                 CartItem(name='Bright Crystal', price=118, quantity=1, user_id=1),
                 CartItem(name='Viva La Juicy', price=50, quantity=1, user_id=1),
                 CartItem(name='Jimmy Choo', price=173, quantity=2, user_id=1),
                 CartItem(name='Versace Pour Femme Dylan Blue', price=235, quantity=1, user_id=1),
                 CartItem(name='Daisy Eau So Fresh', price=549, quantity=2, user_id=1),
                 CartItem(name='Reb\'l Fleur', price=117, quantity=1, user_id=1),
                 ]
    ret = CartItem.objects.bulk_create(instances)
    return HttpResponse("Hello, world. cart insert success.")


def fetchUserCart(request):
    user_id = 1
    cart_items = CartItem.objects.all().filter(user_id=user_id)
    return render(request, 'cart/cart.html',
                  {'cart_items': cart_items,
                   'total_price': CartItem.user_total_price(user_id),
                   })


def addtoCart(request):
    return HttpResponse("Hello, world. You're at the cart index.")


def removefromCart(request):
    return HttpResponse("Hello, world. You're at the cart index.")
