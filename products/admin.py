from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sample', 'created')


admin.site.register(Product, ProductAdmin)
