from rest_framework import serializers
from .models import Cours, Module, SousModule
from categories.models import Categorie


    
class CategorySerializer(serializers.ModelSerializer):

    categories = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta: 
        model = Categorie
        fields = ['id', 'nom']

class SousModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = SousModule
        fields = '__all__'
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        depth = 4
    
class CourSerializers(serializers.ModelSerializer):
    # This line helps to display the category by its name and not by its id
    categorie = serializers.StringRelatedField()

    class Meta: 
        model = Cours
        fields = '__all__'
        depth = 4
