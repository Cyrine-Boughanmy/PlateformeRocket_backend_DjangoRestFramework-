from django.db import models
from categories.models import Categorie

class Qcm(models.Model):
    nom = models.CharField(max_length=45)
    categorie = models.ManyToManyField(Categorie, null=True)
    questions = models.CharField(max_length=200,null=True)
    options_choix = models.CharField(max_length=100,null=True)