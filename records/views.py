"""
Reords application views and viewsets
"""

from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.views import Response, Request

from records.models import Event, Record
from records.serializers import RecordSerializer


class RecordsViewSet(
    ModelViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    """
    Records ViewSet
    """

    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filter the queryset to retieve only objects belonging to the user
        """
        # TODO: Use filter backends
        user_id = self.request.user.id
        return self.queryset.filter(event__user_id=user_id)


class TransactionRecordViewSet(
    ModelViewSet,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
):
    """
    TransactionRecords ViewSet
    """

    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        event = Event.objects.create(user=self.request.user)
