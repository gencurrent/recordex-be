"""
Test Records models
"""
import pytest

from records.models import Event, Record, VoiceRecord, TransactionRecord, StorageFile


@pytest.mark.django_db
def test_records(user):
    """Test the polymorphism of the records tables"""

    event = Event.objects.create(user=user)
    storage_file = StorageFile.objects.create(path="test_path")
    trx_record = TransactionRecord.objects.create(amount=0, event=event)
    voice_record = VoiceRecord.objects.create(file=storage_file, event=event)

    records_list = [voice_record, trx_record]
    assert [*Record.objects.all()] == records_list
    assert [*event.records.all()] == records_list  # Back Querying
