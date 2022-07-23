import json
# from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# allow what method to allow when url is called
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """_summary_
    DRF api_home view
    """
    data = request.data
    serializer_data = ProductSerializer(data=data)
    
    if serializer_data.is_valid(raise_exception=True):
        instance = serializer_data.save()
        return Response(serializer_data.data)
