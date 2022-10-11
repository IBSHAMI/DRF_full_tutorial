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
        return obj.get_discount()