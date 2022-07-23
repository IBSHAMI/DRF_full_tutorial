from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    price_tax = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'discount_price', 'price_tax']
    
    # obj is the product object instance called
    def get_price_tax(self, obj):
        try:
            return obj.get_price_plus_vat()
        except:
            None