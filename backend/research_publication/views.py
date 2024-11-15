from rest_framework import viewsets
from .serializer import ResearchPublicationSerializer
from .models import ResearchPublication

class ResearchPublicationViewSet(viewsets.ModelViewSet):
    queryset = ResearchPublication.objects.all().order_by('id')
    serializer_class = ResearchPublicationSerializer