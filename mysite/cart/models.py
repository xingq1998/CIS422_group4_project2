from django.db import models
from django.utils import timezone
from django.contrib import admin
from product.models import Item


# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    user_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def user_total_price(user_id):
        price = 0
        for item in CartItem.objects.filter(user_id=user_id):
            # product = Item.objects.get(item.product_id)
            price += item.quantity * item.product.price
        return price

    @property
    @admin.display(
        ordering='id',
        description='id of the cart item',
    )
    def cart_id(self):
        return self.id
