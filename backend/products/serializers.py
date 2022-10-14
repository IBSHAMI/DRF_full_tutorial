from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from api.serializers import UserProductSerializer
from .validators import validate_title_contains_number, unique_product_validator


class ProductSerializer(serializers.ModelSerializer):
    # change the name of the field
    user = UserProductSerializer(read_only=True)
    user_data = serializers.SerializerMethodField(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="products:product_detail",
        lookup_field='pk',
    )

    # Create an email field, drf will try to create a field with the name email
    # So we need to overwrite the create method
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[
        validate_title_contains_number,
        unique_product_validator
    ])

    class Meta:
        model = Product
        fields = [
            'user',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
            'update_url',
            'url',
            'user_data',
            # 'email',
        ]

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email)
    #     print(obj)
    #
    #     return obj

    def get_user_data(self, obj):
        return {
            'username': obj.user.username,
        }
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

    # custom validation for any field
    # we create a function with the name validate_<field_name>
    # we can get access to the value of the field
    # and change, update or validate it


class ProductDetailSerializer(serializers.ModelSerializer):
    # change the name of the field
    discount = serializers.SerializerMethodField(read_only=True)
    # Create an email field, drf will try to create a field with the name email
    # So we need to overwrite the create method
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[
        validate_title_contains_number,
        unique_product_validator
    ])

    class Meta:
        model = Product
        fields = [
            # 'user',
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
