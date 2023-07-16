from django.contrib.auth.models import User
from django.db import models

from contacts.models import Contact
from products.models import Product


class Manufacturer(models.Model):
    FORM = [
        ("factory", "Завод"),
        ("entrepreneur", "Индивидуальный предприниматель"),
        ("seller", "Торговая сеть")
    ]

    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    owner = models.CharField(max_length=12, choices=FORM, default='factory', null=True, blank=True) # надобность???
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                                 blank=True)  # Поставщик = предыдущий владелец
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    # product = models.ManyToManyField(Product, null=True)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=255, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        # ordering = ['name'] # список колонок, для общей сортировки

    def __str__(self):
        """название в админке"""
        return self.slug

    # @property
    # def username(self):
    #     return self.user.username if self.user else None

# class Payment(models.Model):
#     supplier = models.ManyToManyField(Manufacturer)
#     debtor = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True,
#                                  blank=True)
#
#     debt = models.DecimalField(max_digits=255, decimal_places=2, default=0)
#
#     class Meta:
#         verbose_name = 'Рассчет'
#         verbose_name_plural = 'Рассчеты'
