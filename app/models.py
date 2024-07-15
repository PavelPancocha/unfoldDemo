from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django_fsm import FSMField, transition


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
    state = FSMField(default='available')
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.name

    @transition(field=state, source='available', target='on_trip')
    def mark_on_trip(self):
        pass

    @transition(field=state, source='+', target='available')
    def mark_available(self):
        pass

    @transition(field=state, source='+', target='in_maintenance')
    def mark_in_maintenance(self):
        pass
