from django.db import models
from django.utils import timezone
from django.contrib import admin
from product.models import Item


class CartItem(models.Model):
    """
    CartItem: The cart items being added to user's shopping cart. Accessible through the
                django Model framework.

    Data Fields:
        product: The foreign key of the product.Item class that the cart items class
                 relates to. When products changed, detail of cart item should changed
                 as well.
        size: The size type of the cart item instance. Same product with different size
              types won't be merged.
        quantity: The amount of the cart item.
        user_id: The id of the user who created the cart item.
        status: The status of the cart item. Active when in shopping cart, closed when items are checked out.
        created_at: The created timestamp when user created the cart item.
    """
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
