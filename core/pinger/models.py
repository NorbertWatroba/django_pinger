from django.db import models


class Locomotive(models.Model):
    name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Frequency(models.Model):
    frequency = models.CharField(max_length=5)

    def __str__(self):
        return f'Frequency: {self.frequency}'
