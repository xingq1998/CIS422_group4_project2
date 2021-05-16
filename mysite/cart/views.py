from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the cart index.")


def fetchUserCart(request):
    return HttpResponse("Hello, world. You're at the cart index.")


def addtoCart(request):
    return HttpResponse("Hello, world. You're at the cart index.")


def removefromCart(request):
    return HttpResponse("Hello, world. You're at the cart index.")
