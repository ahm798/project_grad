from django.http import JsonResponse
import json 

def api_home(request, *args, **kwargs):
    body = request.body
    print(request.GET)
    data ={}
    try:
        data = json.loads(body)
        print(data)
    except:
        pass 
    # print(data.keys())
    return JsonResponse(data)