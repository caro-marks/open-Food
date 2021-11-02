from rest_framework import serializers
from foodData.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'code',
            'url',
            'creator',
            'created_t',
            'last_modified_t',
            'product_name',
            'generic_name',
            'quantity'
        )
