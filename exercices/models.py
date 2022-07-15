from django.db import models
from cours.models import Cours
from categories.models import Categorie
from ckeditor.fields import RichTextField
'''
This is a model for the plateform's exercices 
'''
class Exercices(models.Model):
    nom = models.CharField(max_length=45)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, blank=True, null=True, related_name='cours')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True, related_name='exercices')
    enonce =  RichTextField(blank=True, null=True)
    bonne_reponse = models.CharField(max_length=45) 
    
    def __str__(self):
        return self.nom