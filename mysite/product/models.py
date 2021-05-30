from django.db import models
from django.contrib import admin
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


# These classes allow access to the data stored in the db.sqlite3 database
# file.

class Item(models.Model):
    """
    Item Model: The products being sold on the website. Accessible through the
                django Model framework.

    Data Fields: 
        name: The name of the product displayed on the products/all.html page.
        price: The price of the item instance.
        total_stock: The total amount of items available for an item.
        description: A description of the item being displayed.
        pic_address: The path address where the items are located (most are located 
                     in the static_dir/img folder).
        category: The defining category for which the item belongs to, which helps 
                  with filtering out different items a user would want to view.
    """
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

class Size(models.Model):
    """
    Size Model: The size of a specific product. The sizes available include
                small, medium and large.

    Data Fields: 
        product: The foreign key of the Item class that the Size class 
                 relates to.
        quantity: The total amount of products in this size.
        size_type: The string label of the size (i.e. small, medium or large).
    """
    product = ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    size_type = CharField(default="N/A", max_length=20)

    def __str__(self):
        return f"{self.product.name}, {self.size_type}: {self.quantity}"
