from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializers import *
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
@ csrf_exempt
def student_crete(request):
 if request.method == 'POST':
    json_data = request.body
    print(json_data)
    stream = io.BytesIO(json_data)
    print(stream)
    pythondata = JSONParser().parse(stream)
    print(pythondata)
    str = studentserializers(data=pythondata)
    print(str)
    if str.is_valid():
        str.save()
        res = {'msg':'data cerated'}
        return HttpResponse(res,content_type='application/json')
    json_data = JsonResponse().render(str.error)
    return HttpResponse(json_data,content_type='application/json')
#  return HttpResponse(content_type='application/json')
 
    