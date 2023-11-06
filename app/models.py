import reversion
from django.contrib.auth.models import User
from django.contrib.gis.db import models


@reversion.register()
class Org(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@reversion.register()
class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    location = models.PointField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    state = models.CharField(default='available')

    def __str__(self):
        return self.name

    def mark_on_trip(self):
        pass

    def mark_available(self):
        pass

    def mark_in_maintenance(self):
        pass
