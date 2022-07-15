from dataclasses import fields
from rest_framework import serializers
from .models import EvaluationClass
from categories.models import Categorie

class EvaluationSerializers(serializers.Serializer):
    class Meta: 
        model = EvaluationClass
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    categories = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    
    class Meta: 
        model = Categorie
        fields = ['id', 'nom']     