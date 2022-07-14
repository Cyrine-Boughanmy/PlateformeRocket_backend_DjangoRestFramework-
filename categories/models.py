from django.db import models

'''
This is a model for the courses categories 
'''
class Categorie(models.Model):
    nom = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.nom