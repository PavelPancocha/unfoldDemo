import factory
from faker import Faker
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from .models import Car, Org


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")


class OrgFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Org

    name = factory.Faker('company')

class CarFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    brand = factory.Faker('company')
    location = factory.LazyFunction(lambda: Point(x=Faker.longitude(), y=Faker.latitude()))
    owner = factory.SubFactory(UserFactory)
    org = factory.SubFactory(OrgFactory)

    class Meta:
        model = Car
