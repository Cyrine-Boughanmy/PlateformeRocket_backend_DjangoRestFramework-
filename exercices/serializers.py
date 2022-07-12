from rest_framework import serializers
from .models import Exercices

class ExerciceSerializers(serializers.ModelSerializer):

    class Meta: 
        model = Exercices
        fields = '__all__'