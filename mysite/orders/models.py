from django.db import models
from product.models import Item
from cart.models import CartItem
from django.utils import timezone
from django.contrib import admin


class Order(models.Model):
    """
    Order Model: The order being created in cart module. Accessible through the
                django Model framework.

    Data Fields:
        id: The id of the order records.
        user_id: The id of the user who created the order.
        total_cost: The total_cost of the order.
    """
    user_id = models.IntegerField(default=0)
    total_cost = models.FloatField(default=0.0)

    @property
    @admin.display(
        ordering='id',
        description='id of the Order',
    )
    def order_id(self):
        return self.id


class OrderedItem(models.Model):
    """
    OrderedItem Model: The items contains in each order. Accessible through the
                django Model framework.

    Data Fields:
        product_id: The product id of the order item when checking out.
        product_name: The name of the order item when checking out.
        product_category: The product category of the order item when checking out.
        product_pic_address: The pic_address of the order item when checking out.
        quantity: The quantity of the order items when checking out.
        cart_item: The foreign key of the CartItem class that the OrderedItem instance relates to.
        price: The product price of the order item when checking out.
        order: The foreign key of the Order class that the OrderedItem instance relates to.
        created_at: The created timestamp when user created the order.
    """
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

    @property
    @admin.display(
        ordering='id',
        description='Item ID',
    )
    def order_item_id(self):
        return self.id
