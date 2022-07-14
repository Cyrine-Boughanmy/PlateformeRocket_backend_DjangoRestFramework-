from rest_framework import serializers
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password



class RegisterSuperUserSerializer(serializers.ModelSerializer):
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
        exclusions = super(RegisterSuperUserSerializer, self).get_validation_exclusions()
        return exclusions + ['username', 'password']

class SuperUserSerializers(serializers.ModelSerializer):
    user = RegisterSuperUserSerializer(many=False, required=False)
    class Meta: 
        model = SuperUser
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
        
        super_user = SuperUser.objects.create(
            nom = data["nom"],
            prenom = data["prenom"],
            date_de_naissance = data["date_de_naissance"],
            adresse = data["adresse"],
            code_postal = data["code_postal"],
            ville = data["ville"],
            num_tel = data["num_tel"],
            email = data["email"],
            profile_image = data["profile_image"],
            user=user
        )
        super_user.save()
        return super_user
     













        

    # def create(self, validated_data):
       
    #     super_user = SuperUser.objects.create(
    #         nom = validated_data["nom"],
    #         prenom = validated_data["prenom"],
    #         date_de_naissance = validated_data["date_de_naissance"],
    #         adresse = validated_data["adresse"],
    #         code_postal = validated_data["code_postal"],
    #         ville = validated_data["ville"],
    #         num_tel = validated_data["num_tel"],
    #         email = validated_data["email"],
    #         profile_image = validated_data["profile_image"]     
    #     )
    #     mot_de_passe = validated_data.pop('mot_de_passe')
    #     super_user.set_password(mot_de_passe)
    #     super_user.save()
    #     return super_user





        

    # def create(self, data, **kwargs):
    #     super_user_data = data['num_tel']
    #     super_user = SuperUser.objects.create(
    #         nom = super_user_data["nom"],
    #         prenom = super_user_data["prenom"],
    #         mot_de_passe = super_user_data["mot_de_passe"],
    #         date_de_naissance = super_user_data["date_de_naissance"],
    #         adresse = super_user_data["adresse"],
    #         code_postal = super_user_data["code_postal"],
    #         ville = super_user_data["ville"],
    #         num_tel = super_user_data["num_tel"],
    #         email = super_user_data["email"],
    #         profile_image = super_user_data["profile_image"],

    #     )   
    #     super_user.save()

    # def update(self, instance, validated_data):
    #     super_user_data = validated_data.pop("super-user")
    #     super_user = instance.super_user
    #     super_user.nom = super_user_data.get('nom', super_user.nom)
    #     instance.super_user.prenom = super_user_data.get('prenom', instance.super_user.prenom)
    #     instance.super_user.mot_de_passe = super_user_data.get('mot_de_passe', instance.super_user.mot_de_passe)
    #     instance.super_user.date_de_naissance = super_user_data.get('date_de_naissance', instance.super_user.date_de_naissance)
