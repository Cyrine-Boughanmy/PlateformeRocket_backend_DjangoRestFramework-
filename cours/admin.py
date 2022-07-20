from django.contrib import admin
from .models import Cours

class CoursAdmin(admin.ModelAdmin):
    list_filter = ["categorie"]

admin.site.register(Cours, CoursAdmin)
