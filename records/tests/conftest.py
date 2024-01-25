"""
Conftest for the Records application
"""

from typing import Dict

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import Client
from pytest_django.lazy_django import skip_if_no_django

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@pytest.fixture
@pytest.mark.djnago_db
def user() -> User:
    user = get_user_model().objects.create(
        username="test_user", password="password", email="test_email@email.com"
    )
    yield user


@pytest.fixture
def token(user: User) -> Dict[str, str]:
    yield get_tokens_for_user(user)


@pytest.fixture()
def authenticated_client(token) -> Client:
    """A Django test authenticated client instance"""
    skip_if_no_django()

    return Client(headers={"Authorization": f"Bearer {token['access']}"})
