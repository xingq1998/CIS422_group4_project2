from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.my_login, name='login'),
    path('logout', views.my_logout, name='logout'),
    path('signup', views.my_signup, name='signup'),
]
