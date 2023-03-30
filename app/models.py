from django.contrib.auth.models import User
from django.contrib.gis.db import models

class Org(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    location = models.PointField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

