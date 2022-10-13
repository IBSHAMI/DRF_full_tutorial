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
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
