import json
from msilib.schema import InstallUISequence
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.http import (
    JsonResponse,  # turn dict to json
    HttpResponse,  # accept any type of data
)

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True): # if raise_exception=True, it will error message back to frontend
        # only this create a new object,
        # which fills in the default value for the fields
        # that are not specified in the request
        serializer.save()
        print(serializer.data)
        data = serializer.data
    return Response(data)

# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     '''
#     DRF API View
#     '''


#     instance = Product.objects.all().order_by('?').first()
#     data = {}

#     if instance: 
#         # serilaize the data 
#         data = ProductSerializer(instance).data


#     return Response(data)
