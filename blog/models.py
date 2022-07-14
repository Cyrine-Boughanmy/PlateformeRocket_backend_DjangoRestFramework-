from django.db import models
from super_user.models import SuperUser
from ckeditor.fields import RichTextField

class Blog(models.Model):
    titre = models.CharField(max_length=45, null=True)
    owner = models.ForeignKey(SuperUser, on_delete=models.SET_NULL, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['date']