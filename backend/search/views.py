from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        # get the query from the url
        search_results = Product.objects.none()
        query = self.request.GET.get('query')
        # only return results if the query is not empty
        if query is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user

            search_results = queryset.search(query, user=user)
        return search_results
