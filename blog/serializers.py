from dataclasses import fields
from pyexpat import model
from .models import Blog, Commentaire
from django.contrib.auth.models import User 

from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    commentaires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta: 
        model = Blog
        fields = ['id', 'titre', 'body', 'owner', 'commentaires']

class OwnerSerializer(serializers.ModelSerializer):

    blogs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    commentaires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta: 
        model = User
        fields = ['id', 'username', 'blogs', 'commentaires']

class CommentaireSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta: 
        model = Commentaire
        fields = ['id', 'body', 'owner', 'blog']