from django.contrib import admin

from manufacturer.models import Manufacturer, Product, Contact

admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Contact)