from django.shortcuts import render, redirect
from orders.models import Order, OrderedItem
from cart.models import CartItem


# Create your views here.

def orders(request):
    all_orders = Order.objects.all()

    return render(request, 'orders/all.html', {"orders": all_orders})


def fetch_orders(request):
    ordereditem_sets = {}
    if request.user.is_authenticated:
        user_id = request.user.id
        order_set = Order.objects.all().filter(user_id=user_id).all()
        for order in order_set:
            ordereditem_sets[order.id] = order.ordereditem_set.all()
        return render(request, 'orders/all.html', {"orders": order_set, "ordereditem_sets": ordereditem_sets})
    
    else:
        return render(request, 'user/login.html')

def checkout(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        cart_items = CartItem.objects.all().filter(user_id=user_id, status=1)
        order, created = Order.objects.get_or_create(user_id=user_id, total_cost=CartItem.user_total_price(user_id))
        for cart_item in cart_items:
            OrderedItem.objects.create(product_id=cart_item.product_id,
                                       product_name=cart_item.product.name,
                                       product_category=cart_item.product.category,
                                       product_pic_address=cart_item.product.pic_address,
                                       quantity=cart_item.quantity,
                                       cart_item=cart_item,
                                       price=cart_item.product.price,
                                       order=order
                                       )
            cart_item.status = 0
            cart_item.save()
            # new_order_item = order.ordereditem_set.create(product_id=cart_item.product_id,
            #                                               product_name=cart_item.product_name,
            #                                               product_category=cart_item.product.category,
            #                                               quantity=cart_item.quantity,
            #                                               cart_item=cart_item,
            #                                               price=cart_item.product.price,
            #                                               )
    return redirect('/orders/all')
