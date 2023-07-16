from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    sample = models.CharField(max_length=255) #Модель, чтоб не путать с Model Django
    # is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now=False, auto_now_add=False)
    # supplier = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # Поставщик = предыдущий владелец
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # Ткущий владелец перейдет в Suppler при передаче товара другому

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name