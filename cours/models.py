from django.db import models
from categories.models import Categorie

'''
This is model for the plateform's Courses 
'''
class Cours(models.Model):
    nom = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, blank=True, null=True)
    titre_module = models.CharField(max_length=45) 
    cours_module = models.CharField(max_length=45) 
    valeur_init = models.IntegerField(blank=True, null=True)
