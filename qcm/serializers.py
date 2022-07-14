from dataclasses import fields
from .models import Qcm
from rest_framework import serializers

class QcmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qcm
        fields = '__all__'