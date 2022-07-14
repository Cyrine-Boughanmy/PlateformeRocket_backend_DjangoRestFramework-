from rest_framework import serializers
from .models import SimpleUser
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password

class RegisterSimpleUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password' : {"required": False, "allow_null": True}}
        extra_kwargs = {'username' : {"required": False, "allow_null": True}}

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.email = email
        user.username = email
        user.save()
        return user

    def get_validation_exclusions(self):
        exclusions = super(RegisterSimpleUserSerializer, self).get_validation_exclusions()
        return exclusions + ['username', 'password']

class SimpleUserSerializers(serializers.ModelSerializer):
    user = RegisterSimpleUserSerializer(many=False, required=False)
    class Meta: 
        model = SimpleUser
        fields = [
            "id",
            "nom",
            "prenom",
            "date_de_naissance",
            "code_postal",
            "ville",
            "num_tel",
            "email",
            "profile_image",
            "adresse",
            "resume",
            "presentation",
            "avancement", 
            "user"
        ]
        depth =2

    def create(self, data, **kwargs):
        user_data = data['user']
        user = User.objects.create(
            username=user_data["username"],
            email=user_data["username"]
        )
        user.set_password(user_data["password"])
        user.save()
        
        simple_user = SimpleUser.objects.create(
            nom = data["nom"],
            prenom = data["prenom"],
            date_de_naissance = data["date_de_naissance"],
            adresse = data["adresse"],
            code_postal = data["code_postal"],
            ville = data["ville"],
            num_tel = data["num_tel"],
            email = data["email"],
            profile_image = data["profile_image"],
            resume = data["resume"],
            presentation = data["presentation"],
            avancement = data["avancement"],
            user=user
        )
        simple_user.save()
        return simple_user
