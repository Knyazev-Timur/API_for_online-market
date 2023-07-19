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
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=255, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.slug

