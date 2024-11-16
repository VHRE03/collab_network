from django.urls import include, path
from rest_framework import routers
from .views import ResearchPublicationViewSet

router = routers.DefaultRouter()
router.register(r'research-publications', ResearchPublicationViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
