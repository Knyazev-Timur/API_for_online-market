from rest_framework import serializers

from contacts.models import Contact


class ContactListSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)

        contact.save()
        return contact


#
#
class ContactUpdateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'email', 'country', 'city', 'street', 'house']

    def save(self):
        contact = super().save()

        contact.save()
        return contact


class ContactDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id']
