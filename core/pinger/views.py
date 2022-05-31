from rest_framework import viewsets
from .serializers import *
from .models import Locomotive


class LocoView(viewsets.ModelViewSet):
    serializer_class = LocoSerializer
    queryset = Locomotive.objects.all()


class FreqView(viewsets.ModelViewSet):
    serializer_class = FreqSerializer
    queryset = Frequency.objects.all()
