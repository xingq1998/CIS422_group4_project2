from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('all', views.product_search, name='all'),
]
