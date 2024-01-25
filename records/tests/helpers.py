"""
Helper test utilities
"""
from random import randint
from django.contrib.auth import get_user_model


def generate_user():
    u_number = randint(0, 1 << 20)
    user = get_user_model().objects.create(
        username=f"test_user_{u_number}",
        password="password",
        email=f"test_email_{u_number}@email.com",
    )
    return user
