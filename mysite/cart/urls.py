from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.cartInsert, name='insert'),
    path('fetch_user_cart', views.fetchUserCart, name='fetch_user_cart'),
    path('add_to_cart', views.addtoCart, name='add_to_cart'),
    path('update_cart_item', views.updateCartItem, name='update_cart_item'),
    path('remove_from_cart/<int:car_item_id>/', views.removefromCart, name='remove_from_cart'),
]
