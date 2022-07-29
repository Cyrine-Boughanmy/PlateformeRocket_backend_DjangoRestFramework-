from pyexpat import model
from rest_framework import serializers
from .models import Cours, Module
from categories.models import Categorie


    
class CategorySerializer(serializers.ModelSerializer):

    categories = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    # cours = serializers.SlugRelatedField(slug_field="nom", read_only=True)

    class Meta: 
        model = Categorie
        fields = ['id', 'nom']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
    
class CourSerializers(serializers.ModelSerializer):
    # This line helps to display the category by its name and not by its id
    categorie = serializers.StringRelatedField()
    module = ModuleSerializer(read_only=True, many=True)
    # cours = serializers.SerializerMethodField()

    class Meta: 
        model = Cours
        fields = '__all__'
    
    # def get_accounts_items(self, obj):
    #     module_query = Module.objects.filter(module_id=obj.id)
    #     serializer = ModuleSerializer(module_query, many=True)
    #     return serializer.data