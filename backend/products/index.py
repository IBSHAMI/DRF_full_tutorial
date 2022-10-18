from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    # decide which fields of your model to send to algolia
    # avoid sending sensitive data
    fields = [
        'title',
        'content',
        'price',
        'public',
        'user',
    ]
    tags = 'get_tag'
