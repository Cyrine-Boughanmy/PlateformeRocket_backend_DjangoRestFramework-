from django.db import models
from categories.models import Categorie
from ckeditor.fields import RichTextField

'''
This is model for the plateform's Courses 
'''
class Cours(models.Model):
    nom = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
    titre_module = models.CharField(max_length=45) 
    cours_module = RichTextField(blank=True, null=True)
    valeur_init = models.IntegerField(blank=True, null=True, default = 25)
    image_cours = models.ImageField(null=True, upload_to='static/images/cours/', blank=True)
    ficher_cours = models.FileField(upload_to='file_uploads/cours/', blank=True)

    def __str__(self):
        return self.nom
