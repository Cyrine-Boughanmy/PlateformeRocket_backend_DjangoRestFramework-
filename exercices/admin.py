from django.contrib import admin
from .models import Exercices

class ExerciceAdmin(admin.ModelAdmin):
    list_filter = ["categorie", "cours"]

admin.site.register(Exercices, ExerciceAdmin)
