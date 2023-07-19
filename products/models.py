from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    sample = models.CharField(max_length=255, verbose_name="Модель")
    created = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Дата создания")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
