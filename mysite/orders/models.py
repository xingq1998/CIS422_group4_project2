from django.db import models
from product.models import Item
from cart.models import CartItem
from django.utils import timezone


class Order(models.Model):
    user_id = models.IntegerField(default=0)
    total_cost = models.FloatField(default=0.0)


class OrderedItem(models.Model):
    product_id = models.IntegerField(default=1)
    product_name = models.CharField(max_length=300, default="")
    product_category = models.CharField(default="N/A", max_length=20)
    product_pic_address = models.CharField(default="N/A", max_length=20)
    quantity = models.IntegerField(default=1)
    cart_item = models.ForeignKey(CartItem, on_delete=models.DO_NOTHING, null=True)
    price = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']
