import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request taken from front end 
    body = request.body # byte string of json data 
    data = {}
    
    # possibility that request.body is empty (no JSON data)
    try: 
        data = json.loads(body) # convert byte string to json object
    except: 
        pass
    
    # we can access headers and content type from request object
    data["params"] = request.GET 
    data["headers"] = dict(request.headers) # dictionary of headers
    data["content_type"] = request.content_type # string of content type
    print(data)
    
    return JsonResponse(data)
