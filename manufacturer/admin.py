from django.contrib import admin


from manufacturer.models import Manufacturer


@admin.action(description='Delete all debt')
def debet_delete(modeladmin, request, queryset):
    #Обнуляет задолженность в админке
    queryset.update(debt=0)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'supplier', 'debt')
    list_display_links = ['name', 'supplier']
    list_filter = ('contact',)
    #Активирует действие по удалению задолженности через админку
    actions = [debet_delete]


admin.site.register(Manufacturer, ManufacturerAdmin)
