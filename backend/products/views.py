from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


# retrieve api view return an exiting model instance
# similar to DetailView in Django
class ProductDetailAPIView(generics.RetrieveAPIView):
    # get data from the database
    # we can use def get_queryset(self): to filter the data
    queryset = Product.objects.all()

    # we return a serializer to process the data
    serializer_class = ProductSerializer


# create api view create a new model instance
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # we can add extra logic here
        # we override the perform_create method,
        # so we can add extra logic
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title

        serializer.save(content=content)


# # list api view return a list of model instances
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

