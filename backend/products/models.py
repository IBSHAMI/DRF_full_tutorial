from django.conf import settings
from django.db import models
from django.db.models import Q

user = settings.AUTH_USER_MODEL


# to implement a custom qureyset we need to create a class that inherits from models.QuerySet
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            # we want to return all the products that are public or not public but belong to the user
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        # We return the custom queryset
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Product(models.Model):
    user = models.ForeignKey(user, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=19)
    # Check if product is available for public to view
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def discount_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_price_plus_vat(self):
        return "%.2f" % (float(self.price) * 1.2)

    @property
    def sale_price(self):
        # discount 2 decimal places
        return "{:.2f}".format(self.price * 0.9)

    def get_discount(self):
        return "100"
