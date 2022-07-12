from rest_framework import serializers
from .models import SimpleUser

class SimpleUserSerializers(serializers.ModelSerializer):
    class Meta: 
        model = SimpleUser
        fields = '__all__'

