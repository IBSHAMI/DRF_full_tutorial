from django.db import models
from django.db.models import Q

from .models import Product


# to implement a custom qureyset we need to create a class that inherits from models.QuerySet
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookup)
        if user is not None:
            qs = qs.filter(user=user)
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        # We return the custom queryset
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().is_public().search(query, user=user)
