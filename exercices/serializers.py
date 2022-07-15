from rest_framework import serializers
from .models import Exercices
from categories.models import Categorie

class ExerciceSerializers(serializers.ModelSerializer):
    # cours = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta: 
        model = Exercices
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    
    categories = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta: 
        model = Categorie
        fields = ['id', 'nom']