from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CartItem
from product.models import Item
from django.db.models import F


def index(request):
    return HttpResponse("Hello, world. You're at the cart index.")


def cartInsert(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        instances = [CartItem(name='Palm Print Back Graphic T-shirt', price=23, quantity=1, user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz27451_blue_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     CartItem(name='Basic Crew Neck T-Shirt', price=28, quantity=1, user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz11037_white_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     CartItem(name='Crew Neck T-Shirt With Rolled Sleeves', price=15, quantity=1, user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz24161_black_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     CartItem(name='Original Man Long Sleeve 3/4 Zip Ribbed Polo', price=17, quantity=2,
                              user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz05712_stone_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     CartItem(name='MAN Official Mesh Basketball Vest', price=25, quantity=1, user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz20752_red_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     CartItem(name='Daisy Eau So Fresh', price=59, quantity=2, user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz40053_ice%20blue_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     CartItem(name='Skinny Fit Denim Jeans', price=17, quantity=1, user_id=user_id,
                              pic_address="https://media.boohoo.com/i/boohoo/mzz44519_mid%20blue_xl?$product_image_category_page_horizontal_filters_desktop_2x$&fmt=webp"),
                     ]
        ret = CartItem.objects.bulk_create(instances)
    return HttpResponse("Hello, world. cart insert success.")


def fetchUserCart(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        cart_items = CartItem.objects.all().filter(user_id=user_id, status=1)
        total_price = CartItem.user_total_price(user_id)
        return render(request, 'cart/cart.html',
                      {'cart_items': cart_items,
                       'total_price': total_price,
                       })
    else:
        return render(request, 'cart/cart.html',
                      {'cart_items': None,
                       'total_price': 0,
                       })


def addtoCart(request):
    if not request.user.is_authenticated:
        return render(request, 'user/login.html')

    user_id = request.user.id
    if request.method == 'POST':
        post_dict = request.POST
        product_id = int(post_dict.get("product_id", "0"))
        product = Item.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user_id=user_id, product=product,
                                                            defaults={
                                                                # 'name': product.name,
                                                                # 'desc': product.description,
                                                                # 'price': product.price,
                                                                # 'product_id': product_id,
                                                                'user_id': user_id,
                                                                # 'pic_address': product.pic_address,
                                                                'quantity': 0})
        CartItem.objects.filter(id=cart_item.id).update(quantity=F('quantity') + 1)
        Item.objects.filter(id=product_id).update(total_stock=F('total_stock') - 1)

    return redirect('/cart/fetch_user_cart')


def updateCartItem(request):
    if request.method == 'POST':
        post_dict = request.POST
        print(post_dict)
        quantity = int(post_dict.get("quantity", ""))
        cart_item_id = int(post_dict.get("cart_item_id", 0))  # need to fix, current user id
        cart_item = CartItem.objects.get(id=cart_item_id)
        CartItem.objects.filter(id=cart_item_id).update(quantity=quantity)
        Item.objects.filter(id=cart_item.product.id).update(total_stock=F('total_stock') + quantity)
        return redirect('/cart/fetch_user_cart')


def removefromCart(request, car_item_id):
    cart_item = CartItem.objects.get(id=car_item_id)
    product_id = cart_item.product_id
    CartItem.objects.filter(id=car_item_id).delete()
    Item.objects.filter(id=product_id).update(total_stock=F('total_stock') + cart_item.quantity)

    return redirect('/cart/fetch_user_cart')
