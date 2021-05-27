from django.contrib import admin

from orders.models import Order, OrderedItem
from django.contrib.auth.models import User


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'total_cost', 'order_item_set')
    list_editable = ('user_id', 'total_cost')
    list_filter = ['user_id']

    empty_value_display = '-empty-'

    @admin.display(ordering='test')
    def order_item_set(self, obj):
        return obj.ordereditem_set.all()


@admin.register(OrderedItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order_item_id', 'order_id', 'userid', 'username', 'product_id', 'order_id', 'product_name', 'product_category',
        'quantity', 'cart_item', 'price', 'order', 'created_at')
    list_editable = ['quantity', 'price']

    empty_value_display = '-empty-'

    @admin.display(ordering='test')
    def order_id(self, obj):
        return obj.order.id

    @admin.display(ordering='test')
    def userid(self, obj):
        return obj.cart_item.user_id

    @admin.display(ordering='test')
    def username(self, obj):
        return User.objects.get(id=obj.cart_item.user_id).username
