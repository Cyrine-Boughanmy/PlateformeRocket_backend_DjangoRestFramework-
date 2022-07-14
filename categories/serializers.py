from dataclasses import fields
from rest_framework import serializers
from .models import Categorie

class CategorieSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Categorie
        fields = '__all__'