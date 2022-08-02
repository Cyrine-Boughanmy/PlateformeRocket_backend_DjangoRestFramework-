from .models import Annonce
from rest_framework import serializers
from django.contrib.auth.models import User
class AnnonceSerializer(serializers.ModelSerializer):
    publie_par = serializers.ReadOnlyField(source='publie_par.username')
    class Meta: 
        model = Annonce
        fields = ['id', 'titre', 'description', 'publie_par', 'image_annonce', 'fichier_pdf' ]

class OwnerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username']