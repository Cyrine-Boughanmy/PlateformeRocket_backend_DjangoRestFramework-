from django.db import models
from super_user.models import SuperUser

class Annonce(models.Model):
    titre = models.CharField(max_length=45, null=True)
    description = models.TextField(blank=True, default='')
    date_annonce = models.DateTimeField(auto_now_add=True)
    publie_par = models.ForeignKey(SuperUser, on_delete=models.SET_NULL, blank=True, null=True)
