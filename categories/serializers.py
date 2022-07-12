from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Categorie

class CategorieSerializers(serializers.ModelField):
    class Meta: 
        model = Categorie
        fields = '__all__'