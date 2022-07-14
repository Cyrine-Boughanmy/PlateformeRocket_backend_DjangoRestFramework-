from dataclasses import fields
from rest_framework import serializers
from .models import EvaluationClass

class EvaluationSerializers(serializers.Serializer):
    class Meta: 
        model = EvaluationClass
        fields = '__all__'