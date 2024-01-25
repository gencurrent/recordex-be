"""
Test Records application views
"""

import pytest
from django.urls import reverse

from records.models import Event, VoiceRecord, TransactionRecord, StorageFile
from records.constants import (
    VOICE,
)
from records.tests.helpers import generate_user


@pytest.mark.django_db
def test_get_records(user, authenticated_client):
    """Test getting a list of Records"""

    event = Event.objects.create(user=user)
    file = StorageFile.objects.create()
    voice_record = VoiceRecord.objects.create(event=event, file=file)
    url = reverse("records-list")

    response = authenticated_client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    data = data[0]
    assert data["id"] == str(voice_record.id)
    assert data["type"] == VOICE
    assert data["event_id"] == str(event.id)


@pytest.mark.django_db
def test_get_records__user_restricted(user, authenticated_client):
    """Test getting a list of Records belonging to the user"""

    new_user = generate_user()
    for _ in range(2):
        event = Event.objects.create(user=new_user)
        file = StorageFile.objects.create()
        voice_record = VoiceRecord.objects.create(event=event, file=file)

    event = Event.objects.create(user=user)
    file = StorageFile.objects.create()
    voice_record = VoiceRecord.objects.create(event=event, file=file)
    url = reverse("records-list")

    response = authenticated_client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == str(voice_record.id)
