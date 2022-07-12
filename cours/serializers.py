from dataclasses import fields
from rest_framework import serializers
from .models import Cours

class CourSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Cours
        fields = '__all__'