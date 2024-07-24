from django.contrib import admin
from parler.admin import TranslatableAdmin

from product.models import Product, Image, Comment, Category
#
# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'order' , 'type']


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['pk']

