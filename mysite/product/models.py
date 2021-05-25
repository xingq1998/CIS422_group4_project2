# from _typeshed import OpenTextModeUpdating
from django.db import models
from django.contrib import admin


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, default='Product name unavailable')
    price = models.FloatField(default=0.0)
    total_stock = models.IntegerField(default=0)
    description = models.CharField(default="Description unavailable", max_length=256)
    pic_address = models.CharField(max_length=300, default="")
    category = models.CharField(default="N/A", max_length=20)

    @property
    @admin.display(
        ordering='id',
        description='id of the product',
    )
    def product_id(self):
        return self.id
