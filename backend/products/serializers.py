from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # chnage the name of the field
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    def get_discount(self, obj):
        # obj is the instance of the model
        if hasattr(obj, 'id'):
            return None
        return obj.get_discount()
