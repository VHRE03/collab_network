from django.urls import include, path
from rest_framework import routers
from .views import CollaborationRequestViewSet

router = routers.DefaultRouter()
router.register(r'collaboration-request', CollaborationRequestViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
