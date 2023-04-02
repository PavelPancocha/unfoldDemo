import factory
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from faker import Faker
from faker_vehicle import VehicleProvider

from .models import Car, Org

factory.Faker.add_provider(VehicleProvider)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")


class OrgFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Org

    name = factory.Faker('company')


class CarFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('vehicle_model')
    brand = factory.Faker('vehicle_make')
    location = factory.LazyFunction(lambda: Point(x=float(Faker().longitude()), y=float(Faker().latitude())))
    owner = factory.SubFactory(UserFactory)
    org = factory.SubFactory(OrgFactory)

    class Meta:
        model = Car
