from django.contrib import admin

from product.models import Item


# admin.site.register(Item)


@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'category', 'price', 'description', 'pic_address')
    list_editable = ['price']
    list_filter = ['category']
    fields = ('id', 'name', 'category', 'price', 'description', 'pic_address')
    empty_value_display = '-empty-'

    @admin.display(empty_value='-empt-')
    def view_description(self, obj):
        return obj.description
