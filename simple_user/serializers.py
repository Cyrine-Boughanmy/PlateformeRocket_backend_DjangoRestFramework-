from rest_framework import serializers
from allauth.account.adapter import get_adapter
from Rocket_Coding_Back import settings
from .models import User
from allauth.account.utils import setup_user_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    first_name = serializers.CharField(required = False, write_only = True)
    last_name = serializers.CharField(required = False, write_only = True)
    adresse = serializers.CharField(required = False, write_only = True)
    # password1 = serializers.CharField(required = False)
    # password2 = serializers.CharField(required = True)
    # old_password = serializers.CharField(write_only=True, required=True)
    # # new_password = serializers.CharField(required=True)
    # class Meta:
    #     model = User
    #     fields = ('old_password', 'password1', 'password2')

    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError( ("Les 2 mots de passe ne sont pas conformes !"))
        return data 
    
    
    
    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name' : self.validated_data.get('last_name', ''),
            'adresse' : self.validated_data.get('adresse', ''), 
            'user_type' : self.validated_data.get('user_type', ''), 
            'password1' : self.validated_data.get('password1', ''), 
            'email' : self.validated_data.get('email', ''),

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        # return user

        user.save()
        return user 

class UserDetailsSerializer(serializers.ModelSerializer):
    # date_de_naissance = serializers.DateField(format="%Y-%m-%d")
    class Meta: 
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'adresse',  'code_postal', 'ville', 'num_tel', 'profile_image', 'resume', 'presentation', 'password', 'old_password', 'password' )
        read_only_fields = ('email', )

class ChangePasswordSerializer(serializers.Serializer):
    # model = User

    # """
    # Serializer for password change endpoint.
    # """
    # old_password = serializers.CharField(required=True)
    # new_password = serializers.CharField(required=True)
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
        # instance.username = validated_data.get('username', instance.username)
        # instance.password = validated_data.get('hashedNewPassword', instance.password)
        # instance.save()
        # return instance

    def validate(self, data):
        """ check that username and new password are different """
        if data["username"] == data["password"]:
            raise serializers.ValidationError("Username and new password should be different")
        return data

    def validate_password(self, value):
        """
        check if new password meets the specs
        min 1 lowercase and 1 uppercase alphabet
        1 number
        1 special character
        8-16 character length
        """

        if len(value) < 8 or len(value) > 16:
            raise serializers.ValidationError("It should be between 8 and 16 characters long")

        if not any(x.isupper() for x in value):
            raise serializers.ValidationError("It should have at least one upper case alphabet")

        if not any(x.islower() for x in value):
            raise serializers.ValidationError("It should have at least one lower case alphabet")

        if not any(x.isdigit() for x in value):
            raise serializers.ValidationError("It should have at least one number")

        valid_special_characters = {'@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')',
                                    '<', '>', '?', '/', '|', '{', '}', '~', ':'}

        if not any(x in valid_special_characters for x in value):
            raise serializers.ValidationError("It should have at least one special character")

        return value
 

# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(max_length=128, write_only=True, required=True)
#     new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
#     new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         if not user.check_password(value):
#             raise serializers.ValidationError(
#                 _('Your old password was entered incorrectly. Please enter it again.')
#             )
#         return value

#     def validate(self, data):
#         if data['new_password1'] != data['new_password2']:
#             raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
#         password_validation.validate_password(data['new_password1'], self.context['request'].user)
#         return data

#     def save(self, **kwargs):
#         password = self.validated_data['new_password1']
#         user = self.context['request'].user
#         user.set_password(password)
#         user.save()
#         return user

# def validate_password(self, value: str) -> str:

#     return make_password(value)

# from dataclasses import fields
# from rest_framework import serializers
# from .models import SimpleUser
# from .models import *
# from .serializers import *

# class RegisterSimpleUserSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = User
#         fields = ('username', 'password')
#         extra_kwargs = {'password' : {"required": False, "allow_null": True}}
#         extra_kwargs = {'username' : {"required": False, "allow_null": True}}

#     def create(self, validated_data):
#         email = validated_data.pop('email')
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.email = email
#         user.username = email
#         user.save()
#         return user

#     def get_validation_exclusions(self):
#         exclusions = super(RegisterSimpleUserSerializer, self).get_validation_exclusions()
#         return exclusions + ['username', 'password']

# class SimpleUserSerializers(serializers.ModelSerializer):
#     user = RegisterSimpleUserSerializer(many=False, required=False)
#     class Meta: 
#         model = SimpleUser
#         fields = [
#             "id",
#             "nom",
#             "prenom",
#             "date_de_naissance",
#             "code_postal",
#             "ville",
#             "num_tel",
#             "email",
#             "profile_image",
#             "adresse",
#             "resume",
#             "presentation",
#             "avancement", 
#             "user"
#         ]
#         depth =2

#     def create(self, data, **kwargs):
#         user_data = data['user']
#         user = User.objects.create(
#             username=user_data["username"],
#             email=user_data["username"]
#         )
#         user.set_password(user_data["password"])
#         user.save()
        
#         simple_user = SimpleUser.objects.create(
#             nom = data["nom"],
#             prenom = data["prenom"],
#             date_de_naissance = data["date_de_naissance"],
#             adresse = data["adresse"],
#             code_postal = data["code_postal"],
#             ville = data["ville"],
#             num_tel = data["num_tel"],
#             email = data["email"],
#             profile_image = data["profile_image"],
#             resume = data["resume"],
#             presentation = data["presentation"],
#             avancement = data["avancement"],
#             user=user
#         )
#         simple_user.save()
#         return simple_user

#     # Function to update simple user's data/profile 
#     def update(self, instance, validated_data):

#         # Update values of model User 
#         user_data = validated_data.pop('user')
#         user = instance.user 
#         user.username = user_data.get('username', user.username)
#         user.email = user_data.get('email', user.email)
#         password = user_data.pop('password')
#         user.set_password(password)
#         user.save()

#         # Update Simple User data 
#         instance.nom = validated_data.get('nom', instance.nom)
#         instance.prenom = validated_data.get('prenom', instance.prenom)
#         instance.date_de_naissance = validated_data.get('date_de_naissance', instance.date_de_naissance)
#         instance.adresse = validated_data.get('adresse', instance.adresse)
#         instance.code_postal = validated_data.get('code_postal', instance.code_postal)
#         instance.ville = validated_data.get('ville', instance.ville)
#         instance.num_tel = validated_data.get('num_tel', instance.num_tel)
#         instance.email = validated_data.get('email', instance.email)
#         instance.profile_image = validated_data.get('profile_image', instance.profile_image)
#         instance.resume = validated_data.get('resume', instance.resume)
#         instance.presentation = validated_data.get('presentation', instance.presentation)
#         instance.avancement = validated_data.get('avancement', instance.avancement)
#         instance.save()
        
#         return instance

# class profileSimpleUser(serializers.ModelSerializer):

#     class Meta: 
#         model = SimpleUser
#         fields = '__all__'
#         depth = 3

