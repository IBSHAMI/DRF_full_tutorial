import json
# from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# allow what method to allow when url is called
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    product = Product.objects.all().order_by('?').first()
    instance = {}
    
    if product: 
        instance = ProductSerializer(product).data

    return Response(instance)


# def api_home(request, *args, **kwargs):
#     product = Product.objects.all().order_by('?').first()
#     data = {}
    
#     if product: 
#         data["product"] = model_to_dict(product, fields=['id', 'title'])

#     print(data)
#     return JsonResponse(data)