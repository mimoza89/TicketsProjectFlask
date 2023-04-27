import factory

from db import db
from models import User, RoleType, Concert, Purchase, PurchaseStatus
from tests.base import mock_uuid


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.commit()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    favourite_genres = factory.Faker("favourite_genres")
    city = factory.Faker("city")
    purchased_tickets = 0
    password = factory.Faker("password")
    role = RoleType.simple_user


def get_user_id():
    return UserFactory().id


class ConcertFactory(BaseFactory):
    class Meta:
        model = Concert

    id = factory.Sequence(lambda n: n)
    title = "Mocked title"
    city = "Mocked city"
    artist = "Mocked artist"
    price = 150
    created_at = "2023-04-27"


def get_concert_id():
    return ConcertFactory().id


class PurchaseFactory(BaseFactory):
    class Meta:
        model = Purchase

    id = factory.Sequence(lambda n: n)
    user_id = mock_uuid()
    concert_id = mock_uuid()
    quantity = 1
    amount = 20
    created_at = "2023-04-27"
    status = PurchaseStatus.pending