from functools import partial
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import io
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
@ csrf_exempt
# Create your views here.
def str(request):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = student.objects.get(id = id)
        print('=========================================================')
        serializers = studentserializer(stu,data=pythondata,partial=True)
        stu1=studentserializer()
        if serializers.is_valid():
            print('=========================888888888888888================================')
            serializers.udpate_update(stu1,stu)
            
            print('=========================888888888888888================================')
            res = {'msg':'data update!!'}
            json_data = JsonResponse().render(res)
            return HttpResponse(json_data,content_data='application/json')
