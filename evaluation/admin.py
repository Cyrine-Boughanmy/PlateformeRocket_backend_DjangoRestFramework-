from django.contrib import admin
from .models import EvaluationClass

class EvaluationAdmin(admin.ModelAdmin):
    list_filter = ["categorie"]

admin.site.register(EvaluationClass, EvaluationAdmin)
