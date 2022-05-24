from rest_framework import serializers
from .models import *

class studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length = 30)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=30)
    
    # class Meta:
    #     model =
    #     fields = '__all__'   
    

    def udpate_update(self, instance, validated_data):
        # print(instance.name)  
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance 

        
    
    

