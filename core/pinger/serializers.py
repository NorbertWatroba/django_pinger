from rest_framework import serializers
from .models import Locomotive, Frequency


class LocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locomotive
        fields = [
            'name',
            'ip_address',
            'active',
        ]


class FreqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = [
            'frequency'
        ]
