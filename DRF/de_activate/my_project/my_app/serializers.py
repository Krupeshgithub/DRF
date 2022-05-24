from rest_framework import serializers
from .models import *

class studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=30)
    
    def create(self,valid_data):
        return student.objects.create(**valid_data) 