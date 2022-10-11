import json
from msilib.schema import InstallUISequence
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.forms.models import model_to_dict
from django.http import (
    JsonResponse, # turn dict to json 
    HttpResponse, # accept any type of data
)

from products.models import Product
from products.serializers import ProductSerializer



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(): 
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
