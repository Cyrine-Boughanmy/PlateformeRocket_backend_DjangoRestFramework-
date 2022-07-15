from dataclasses import fields
from numpy import source
from rest_framework import serializers
from .models import Cours
from categories.models import Categorie

class CourSerializers(serializers.ModelSerializer):

    class Meta: 
        model = Cours
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):

    categories = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    

    class Meta: 
        model = Categorie
        fields = ['id', 'nom']