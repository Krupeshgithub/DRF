from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.

def index(request,pk):
    stu = student.objects.get(id=pk)
    serializer = studentserializer(stu)
    # json_data = JsonResponse().render(serializer.data)
    # return HttpResponse(json_data,content_type ='application/json')\
    return JsonResponse(serializer.data)   

def all(request):
    stu = student.objects.all()
    serializers = studentserializer(stu,many = True)
    return JsonResponse(serializers.data,safe=False)
