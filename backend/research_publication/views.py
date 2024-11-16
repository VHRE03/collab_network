from rest_framework import viewsets
from .serializer import ResearchPublicationSerializer
from .models import ResearchPublication
from rest_framework.response import Response

class ResearchPublicationViewSet(viewsets.ModelViewSet):
    queryset = ResearchPublication.objects.all().order_by('id')
    serializer_class = ResearchPublicationSerializer
    
    def list(self, request, *args, **kwargs):
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer_data = []
        
        for publication in queryset:
            data = self.get_serializer(publication).data
            
            data['author'] = {
                "first_name": publication.author.first_name
            }
            
            serializer_data.append(data)
        
        return Response(serializer_data)
    
    def retrieve(self, request, *args, **kwargs):
        # Para GET (detalle de una publicación)
        instance = self.get_object()
        data = self.get_serializer(instance).data
        # Personalizar el campo `author` en GET
        data["author"] = {
            "id": instance.author.id,
            "first_name": instance.author.first_name
        }
        return Response(data)