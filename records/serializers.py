"""
Serializers
"""

from rest_framework import serializers

from records.models import (
    Record,
    TransactionRecord,
    VoiceRecord,
)
from records.constants import (
    VOICE,
    TEXT,
    TRANSACTION,
)


class RecordSerializer(serializers.ModelSerializer):
    TYPES = {
        TransactionRecord: TRANSACTION,
        VoiceRecord: VOICE,
    }

    type = serializers.SerializerMethodField()

    class Meta:
        model = Record

        fields = (
            "id",
            "event_id",
            "created",
            "type",
        )

    def get_type(self, record: Record) -> str:
        """
        Get the type of the record
        """
        instance_class = record.get_real_instance_class()
        return self.TYPES.get(instance_class)
