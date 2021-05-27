from django.contrib import admin
from django.contrib.auth.models import User
from cart.models import CartItem


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'user_id', 'username', 'product_id', 'product_name', 'product_price', 'quantity',
                    'status', 'created_at')
    list_editable = ('status', 'user_id', 'quantity')
    list_filter = ('status', 'user_id', 'product_id')
    fields = ('product', 'quantity', 'user_id', 'status', 'created_at')
    empty_value_display = '-empty-'

    @admin.display(ordering='test')
    def product_name(self, obj):
        return obj.product.name

    @admin.display(ordering='test')
    def product_price(self, obj):
        return obj.product.name

    @admin.display(ordering='test')
    def username(self, obj):
        return User.objects.get(id=obj.user_id).username
