from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('all', views.fetch_orders, name='all'),
    path('checkout', views.checkout, name='checkout'),
]
