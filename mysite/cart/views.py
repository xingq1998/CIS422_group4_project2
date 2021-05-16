from django.shortcuts import render, redirect
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


def addtoCart(request, name, price, quantity):
    CartItem.objects.create(name=name, price=price, quantity=quantity, user_id=1)
    return HttpResponse("Add to shopping cart success.")


def updateCartItem(request):
    if request.method == 'POST':
        post_dict = request.POST
        print(post_dict)
        quantity = int(post_dict.get("quantity", ""))
        cart_item_id = int(post_dict.get("cart_item_id", 0))  # need to fix, current user id
        CartItem.objects.filter(id=cart_item_id).update(quantity=quantity)
        return redirect('/cart/fetch_user_cart')


def removefromCart(request, car_item_id):
    CartItem.objects.filter(id=car_item_id).delete()
    return redirect('/cart/fetch_user_cart')
