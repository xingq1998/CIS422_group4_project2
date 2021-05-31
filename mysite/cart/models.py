from django.db import models
from django.utils import timezone
from django.contrib import admin
from product.models import Item


# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    size = models.CharField(default="N/A", max_length=20)
    quantity = models.IntegerField(default=1)
    user_id = models.IntegerField(default=0)
    status = models.IntegerField(default=1)  # 1 represents active,0 represents closed
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.name

    def user_total_price(user_id):
        price = 0
        for item in CartItem.objects.filter(user_id=user_id, status=1):
            # product = Item.objects.get(item.product_id)
            price += item.quantity * item.product.price
        return price

    @property
    @admin.display(
        ordering='id',
        description='CartItem id',
    )
    def cart_id(self):
        return self.id
