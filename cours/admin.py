from django.contrib import admin
from .models import Cours, Module, SousModule

class CoursAdmin(admin.ModelAdmin):
    list_filter = ["categorie"]

# class ModuleAdmin(admin.ModelAdmin):
#     list_filter = ["cours"]

admin.site.register(Cours, CoursAdmin)
admin.site.register(Module)
admin.site.register(SousModule)
