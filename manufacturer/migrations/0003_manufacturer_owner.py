# Generated by Django 4.2.3 on 2023-07-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0002_remove_product_supplier_alter_manufacturer_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='owner',
            field=models.CharField(choices=[('factory', 'Завод'), ('entrepreneur', 'Индивидуальный предприниматель'), ('seller', 'Торговая сеть')], default='draft', max_length=12),
        ),
    ]
