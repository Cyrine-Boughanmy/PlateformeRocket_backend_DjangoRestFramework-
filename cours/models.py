from django.db import models
from categories.models import Categorie
from ckeditor.fields import RichTextField

'''
This is model for the plateform's Courses 
'''
class SousModule(models.Model):
    num_module = models.CharField(blank=True, null=True, max_length=45)
    cours_module = RichTextField(blank=True, null=True)
    valeur_init = models.IntegerField(blank=True, null=True, default = 25)
    ficher_cours_pdf = models.FileField(upload_to='file_uploads/cours/', blank=True)

    def __str__(self):
        return self.num_module
class Module(models.Model):
    titre_module = models.CharField(max_length=45, blank=True, null=True) 
    # cours_module = RichTextField(blank=True, null=True)
    # valeur_init = models.IntegerField(blank=True, null=True, default = 25)
    # ficher_cours = models.FileField(upload_to='file_uploads/cours/', blank=True)
    sous_module = models.ManyToManyField(SousModule)

    def __str__(self):
        return self.titre_module 

class Cours(models.Model):
    nom_cours = models.CharField(max_length=45)
    description_cours = models.CharField(max_length=45)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
    image_cours = models.ImageField(null=True, upload_to='static/images/cours/', blank=True)
    modules = models.ManyToManyField(Module)


    def __str__(self):
        return self.nom_cours
