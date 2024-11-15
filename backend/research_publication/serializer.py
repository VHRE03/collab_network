from rest_framework import serializers
from .models import ResearchPublication

class ResearchPublicationSerializer(serializers.ModelSerializer):
    class Metas:
        model = ResearchPublication
        fields = '__all__'