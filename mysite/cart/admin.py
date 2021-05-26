from django.contrib import admin

from cart.models import CartItem


# admin.site.register(Item)


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    # list_display = ('cart_id', 'user_id', 'product_id', 'name', 'price', 'quantity', 'created_at')
    # list_editable = ('user_id', 'quantity')
    # list_filter = ('user_id', 'product_id')
    # fields = ('id', 'name', 'category', 'price', 'total_stock', 'description', 'pic_address')
    empty_value_display = '-empty-'
