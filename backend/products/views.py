from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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


# update api view update an exiting model instance
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        # we can add extra logic here
        # we override the perform_update method,
        # so we can add extra logic
        instance = serializer.save()








# create a function based method for all the api views
@api_view(['GET', 'POST'])
def products_all_views(request, *args, **kwargs):
    method = request.method

    if method == 'GET':
        # detail view
        if 'pk' in kwargs:
            pk = kwargs.get('pk')
            product = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(product).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True).data
        return Response(serializer)
        pass

    if method == 'POST':
        # create view
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
        return Response(serializer.data)

    if method == 'PUT':
        # update view
        pass

    if method == 'DELETE':
        # delete view
        pass
