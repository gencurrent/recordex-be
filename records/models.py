"""
Records application models
"""


from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel

from polymorphic.models import PolymorphicModel


class StorageFile(BaseModel):
    """
    File to store on within a cloud storage service
    """

    path: str = models.CharField(
        max_length=255,
        default="",
        help_text="Path to the file in the storage to access",
    )


class Event(BaseModel):
    """
    Base event referred by a Record instance
    """

    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.PROTECT,
        related_name="events",
    )


class Record(PolymorphicModel, BaseModel):
    """
    General event record to refer derivative records to
    """

    from_record: "Record" = models.ForeignKey(
        "self",
        null=True,
        unique=True,
        on_delete=models.CASCADE,
        help_text="Record from which the current Record is created from",
    )

    event: Event = models.ForeignKey(
        Event,
        null=False,
        on_delete=models.PROTECT,
        related_name="records",
        help_text="Event Records",
    )

    class Meta:
        ordering = ("-created",)


class VoiceRecord(Record):
    """
    Voice record to capture data from
    """

    file: StorageFile = models.ForeignKey(
        StorageFile,
        null=False,
        unique=True,
        related_name="voice_records",
        on_delete=models.PROTECT,
    )


class TransactionRecord(Record):
    """
    Voice record to capture data from
    """

    amount: int = models.IntegerField(
        help_text="Amount as income (+) or expense (-)",
    )
    description: str = models.CharField(
        max_length=256,
        default="",
        null=False,
        blank=True,
    )
