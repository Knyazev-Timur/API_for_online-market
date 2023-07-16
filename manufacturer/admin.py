from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode

from manufacturer.models import Manufacturer

# admin.site.register(Manufacturer)

@admin.action(description='Delete all debt')
def debet_delete(modeladmin, request, queryset):
    queryset.update(debt=0)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'supplier', 'debt')
    list_display_links = ['supplier']
    list_filter = ('contact',)
    actions = [debet_delete]

    # def view_suppler_link(self, obj):
    #     from django.utils.html import format_html
    #     count = obj.person_set.count()
    #     url = (
    #         reverse('admin:')
    #     )




# @admin.register(Manufacturer)
# class ManufacturerInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('name',)

admin.site.register(Manufacturer, ManufacturerAdmin)
