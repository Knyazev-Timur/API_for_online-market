from  rest_framework import serializers

from manufacturer.models import Manufacturer
from products.models import Product


class ManufacturerListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=100)
    # product = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )
    class Meta:
        model = Manufacturer
        fields = '__all__'

class ManufacturerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'
#
#
class ManufacturerCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    # product = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=Product.objects.all(),
    #     slug_field='id'
    # )
    class Meta:
        model = Manufacturer
        fields = '__all__'
        # exclude = ['product']

    # def is_valid(self, *, raise_exception=False):
    #     self._product = self.initial_data.pop('product')
    #     return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        manufacturer = Manufacturer.objects.create(**validated_data)

        # for product in self._product:
        #     product_obj, _ = Product.objects.get_or_create(name=product)
        #     manufacturer.product.add(product_obj)

        manufacturer.save()
        return manufacturer
#
#
class ManufacturerUpdateSerializer(serializers.ModelSerializer):
    # product = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=Product.objects.all(),
    #     slug_field='name'
    # )

    id = serializers.PrimaryKeyRelatedField(read_only=True)
    debt = serializers.DecimalField(max_digits=255, decimal_places=2, default=0, read_only=True)


    class Meta:
        model = Manufacturer
        fields = '__all__'
        # exclude = ['product']

    # "id": 18,
    # "slug": "newmanufactura",
    # "name": "NEWManufactura",
    # "created": "2023-07-16",
    # "owner": "factory",
    # "debt": "0.00",
    # "supplier": null,
    # "product": 1,
    # "contact": 1
    # def is_valid(self, *, raise_exception=False):
    #     self._product = self.initial_data.pop('product')
    #     return super().is_valid(raise_exception=raise_exception)

    def save(self):
        contact = super().save()

        # for product in self._product:
        #     product_obj, _ = Product.objects.get_or_create(name=product)
        #     manufacturer.product.add(product_obj)

        contact.save()
        return contact
#
#
class ManufacturerDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id']


