from rest_framework import viewsets
from .serializer import CollaborationRequestSerializer
from .models import CollaborationRequest

class CollaborationRequestViewSet(viewsets.ModelViewSet):
    queryset = CollaborationRequest.objects.all().order_by('id')
    serializer_class = CollaborationRequestSerializer