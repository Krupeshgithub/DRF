from django.http import HttpResponse
from .models import *
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@ csrf_exempt
def delete(request):
  json_data = request.body
  print(json_data)
  streams = io.BytesIO(json_data)
  print(streams)
  pythondata = JSONParser().parse(streams)
  id = pythondata.get('id')
  stu = student.objects.get(id=id)
  stu.delete()  
  return HttpResponse(stu)
  