from django.db import models
from product.models import Item


class Order(models.Model):
    order_id = models.BigIntegerField(default=0)
    user_id = models.IntegerField(default=0)
    total_cost = models.FloatField(default=0.0)


class OrderedItem(models.Model):
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)