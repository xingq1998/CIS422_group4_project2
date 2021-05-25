from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.

class CartItem(models.Model):
    product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='')
    desc = models.CharField(max_length=30, default='')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    # total_price = models.IntegerField(default=1)
    user_id = models.IntegerField(default=0)
    pic_address = models.CharField(max_length=300, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def user_total_price(user_id):
        price = 0
        for item in CartItem.objects.filter(user_id=user_id):
            price += item.quantity * item.price
        return price

    @property
    @admin.display(
        ordering='id',
        description='id of the cart item',
    )
    def cart_id(self):
        return self.id

