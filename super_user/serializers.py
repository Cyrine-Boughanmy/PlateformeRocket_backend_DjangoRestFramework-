from dataclasses import fields
from rest_framework import serializers
from .models import SuperUser

class SuperUserSerializers(serializers.ModelSerializer):
    class Meta: 
        model = SuperUser
        fields = '__all__'

