from  rest_framework import serializers

from contacts.models import Contact
from manufacturer.models import Manufacturer, Product




class ContactListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=100)
    # product = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )
    class Meta:
        model = Contact
        fields = '__all__'

class ContactDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
#
#
class ContactCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    # product = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=Product.objects.all(),
    #     slug_field='name'
    # )
    class Meta:
        model = Contact
        fields = '__all__'
        # exclude = ['product']

    # def is_valid(self, *, raise_exception=False):
    #     self._product = self.initial_data.pop('product')
    #     return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)

        # for product in self._product:
        #     product_obj, _ = Product.objects.get_or_create(name=product)
        #     manufacturer.product.add(product_obj)

        contact.save()
        return contact
#
#
class ContactUpdateSerializer(serializers.ModelSerializer):
    # product = serializers.SlugRelatedField(
    #     required=False,
    #     many=True,
    #     queryset=Product.objects.all(),
    #     slug_field='name'
    # )

    id = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Contact
        fields = ['id', 'email', 'country', 'city', 'street', 'house']
        # exclude = ['product']

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


class ContactDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id']


