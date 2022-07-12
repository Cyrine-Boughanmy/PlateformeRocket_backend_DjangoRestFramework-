from django.db import models

'''
This model is for the Super User who can be the ADMIN 
'''
class SuperUser(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    date_de_naissance = models.DateField()
    adresse = models.CharField(max_length=45)
    code_postal = models.CharField(max_length=45)
    ville = models.CharField(max_length=45)
    num_tel = models.CharField(max_length=45, null=True)
    email = models.EmailField(unique=True, default="")
    profile_image = models.ImageField(null=True,upload_to='static/images')
