from rest_framework import serializers

from goods.models import Contact, Good, Supplier, RetailNetwork


class RetailNetworkCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RetailNetwork
        fields = '__all__'


class RetailNetworkSerializer(serializers.ModelSerializer):

    good = serializers.SlugRelatedField(queryset=Good.objects.all(), slug_field='title')
    supplier = serializers.SlugRelatedField(queryset=Supplier.objects.all(), slug_field='name')
    contact = serializers.SlugRelatedField(queryset=Contact.objects.all(), slug_field='country')

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('accounts_receivable',)


class RetailNetworkUpdateSerializer(RetailNetworkSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
