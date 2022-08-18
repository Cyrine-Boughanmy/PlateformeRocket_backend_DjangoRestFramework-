from time import time
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username: 
            raise ValueError(('Veuillez saisir votre username !'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, **extra_fields)
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user 

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user 

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    
    date_de_naissance = models.DateField(null=True)
    adresse = models.CharField(max_length=45, null=True)
    code_postal = models.CharField(max_length=45, null=True)
    ville = models.CharField(max_length=45, null=True)
    num_tel = models.CharField(max_length=45, null=True)
    profile_image = models.ImageField(null=True,upload_to='static/images', blank=True)
    resume = models.FileField(upload_to='file_uploads/', blank=True, null=True)
    presentation = models.TextField(null=True, blank=True)
    avancement = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

# from django.db import models

# from django.dispatch import receiver
# from django_rest_passwordreset.signals import reset_password_token_created
# from django.core.mail import send_mail
# from django.contrib.auth.models import User

# '''
# This model is for the plateform's students (apprenants) of the bootcamp
# '''
# class SimpleUser(models.Model):
#     nom = models.CharField(max_length=45)
#     prenom = models.CharField(max_length=45)
#     # mot_de_passe = models.CharField(max_length=45, null=True)
#     date_de_naissance = models.DateField()
#     adresse = models.CharField(max_length=45)
#     code_postal = models.CharField(max_length=45)
#     ville = models.CharField(max_length=45)
#     num_tel = models.CharField(max_length=45, null=True)
#     email = models.EmailField(unique=True, default="")
#     USERNAME_FIELD = 'email'
#     profile_image = models.ImageField(null=True,upload_to='static/images')
#     resume = models.FileField(upload_to='file_uploads/', blank=True)
#     presentation = models.TextField(null=True, blank=True)
#     avancement = models.IntegerField(blank=True, null=True)
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.prenom

# '''
# Pour la réinitialisation des mots de passe 
# '''
# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

#     user = SimpleUser.objects.filter(
#         email=reset_password_token.user.email).get()
#     nom = user.nom
#     prenom = user.prenom

#     email_plaintext_message = """Bonjour {} {},

# Vous avez récemment demandé la réinitialisation du mot de passe de votre compte Markus. 
# Veuillez suivre la procédure communiquée ci-dessous.

# Copiez ce code de modification : {}

# Ensuite, revenez sur la page de modification du mot de passe de l’application et renseignez le code reçu par mail dans le champs correspondant.

# Enfin, choisissez votre nouveau mot de passe et confirmez-le.

# Si vous n’avez pas demandé une réinitialisation de votre mot de passe, ignorez ce email.

# Markus vous remercie de votre confiance.

#     """.format(nom, prenom, reset_password_token.key)

#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Rocket Coding Bootcamp"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "rocketcoding.bootcamp@gmail.com",
#         # to:
#         [reset_password_token.user.email]
#     )
