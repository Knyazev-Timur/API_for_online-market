from rest_framework import serializers

from manufacturer.models import Manufacturer


class ManufacturerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ManufacturerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ManufacturerCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    """По заданию закрыто только изменение задолженности в API.
     При создании задолженность можно указать, 
     т.к. в задании не было указано о запрете на создание"""
    # debt = serializers.DecimalField(max_digits=255, decimal_places=2, default=0, read_only=True)

    class Meta:
        model = Manufacturer
        fields = '__all__'

    def create(self, validated_data):
        manufacturer = Manufacturer.objects.create(**validated_data)

        manufacturer.save()
        return manufacturer


class ManufacturerUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    debt = serializers.DecimalField(max_digits=255, decimal_places=2, default=0, read_only=True)

    class Meta:
        model = Manufacturer
        fields = '__all__'

    def save(self):
        contact = super().save()

        contact.save()
        return contact


#
#
class ManufacturerDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id']
