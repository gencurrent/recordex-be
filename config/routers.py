"""
URL configuration for recordex_be project.
"""
from rest_framework import routers

from records.views import RecordsViewSet

router = routers.DefaultRouter()


router.register(
    prefix="records",
    viewset=RecordsViewSet,
    basename="records",
)

urlpatterns = router.urls
