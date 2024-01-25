"""
Core models declaration
"""

from uuid import UUID, uuid4

from django.db.models import Manager, UUIDField

from model_utils.models import SoftDeletableModel, TimeStampedModel, UUIDModel


class BaseModel(UUIDModel, TimeStampedModel, SoftDeletableModel):
    """
    Base model to inherit by the majority of business logic models
    """

    all_objects = Manager()

    class Meta:
        abstract = True
        ordering = ("-created",)
