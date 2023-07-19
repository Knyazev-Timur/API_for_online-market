from rest_framework import serializers

from products.models import Product


# from manufacturer.models import Manufacturer, Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)

        product.save()
        return product


class ProductUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'sample', 'created']

    def save(self):
        product = super().save()

        product.save()
        return product


class ProductDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']
