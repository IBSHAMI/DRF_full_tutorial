import json
from django.forms.models import model_to_dict
from django.http import (
    JsonResponse, # turn dict to json 
    HttpResponse, # accept any type of data
)

from products.models import Product

def api_home(request, *args, **kwargs):
    product = Product.objects.all().order_by('?').first()
    data = {}
    
    if product: 
        data["product"] = model_to_dict(product, fields=['id', 'title'])

    print(data)
    return JsonResponse(data)
