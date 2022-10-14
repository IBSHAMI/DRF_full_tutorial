from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditor


# create api view create a new model instance
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # The authentication_classes below is similar to default authentication classes in settings.py
    # authentication_classes = [TokenAuthentication, authentication.SessionAuthentication]

    # by default the user will have access to safe methods,
    # safe methods are GET. If we want pervent the user even from get method
    # we have to create a custom permission class
    # order of permission_classes is important
    # I want to check if user is staff or editor
    # then I want to check if user has permission to add or change or delete
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]

    def perform_create(self, serializer):
        # we can add extra logic here
        # we override the perform_create method,
        # so we can add extra logic
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title

        serializer.save(content=content)


# retrieve api view return an exiting model instance
# similar to DetailView in Django
class ProductDetailAPIView(generics.RetrieveAPIView):
    # get data from the database
    # we can use def get_queryset(self): to filter the data
    queryset = Product.objects.all()

    # we return a serializer to process the data
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]


# update api view update an exiting model instance
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]

    def perform_update(self, serializer):
        # we can add extra logic here
        # we override the perform_update method,
        # so we can add extra logic
        instance = serializer.save()


# delete api view delete an exiting model instance
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]

    def perform_destroy(self, instance):
        # we can add extra logic here
        # we override the perform_destroy method,
        # so we can add extra logic
        super().perform_destroy(instance)


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


# create a generic class based method for all the api views
class ProductGenericAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    # in class based view we use methods instead of if statements
    # each method take the request and argument and keyword arguments
    # we will use different methods for different http methods

    # we declare our queryset and serializer class
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # we use the get method to get a list of objects or detail of an object
    def get(self, request, *args, **kwargs):
        # we check if the pk is in the kwargs
        if 'pk' in kwargs:
            # if it is we call the retrieve method
            return self.retrieve(request, *args, **kwargs)

        # I can return a list of objects or a detail of an object
        # by calling self.list from mixins.ListModelMixin class
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
