import pytest

from ..models import Cheese
from .factories import CheeseFactory

# connects tests with the DB
pytestmark = pytest.mark.django_db


def test___str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
