from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


def validate_title_contains_number(value):
    # validation
    if any(char.isdigit() for char in value):
        raise serializers.ValidationError('Title cannot contain a number')
    return value


unique_product_validator = UniqueValidator(queryset=Product.objects.all(), message="Title already exists")
