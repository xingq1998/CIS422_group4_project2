from django.shortcuts import render
from orders.models import Order

# Create your views here.

def orders(request):
    all_orders = Order.objects.all()
    
    return render(request, 'orders/all.html', {"orders" : all_orders})