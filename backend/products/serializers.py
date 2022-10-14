from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # change the name of the field
    discount = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="products:product_detail",
        lookup_field='pk',
    )

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            'update_url',
            'url',
        ]

    def get_update_url(self, obj):
        # We have to access the request from self.context
        # This is because sometimes we might not have access to the request
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('products:product_update', kwargs={'pk': obj.pk}, request=request)

    def get_discount(self, obj):
        # obj is the instance of the model
        if hasattr(obj, 'id'):
            return None
        return obj.get_discount()


class ProductDetailSerializer(serializers.ModelSerializer):
    # change the name of the field
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
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