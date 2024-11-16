from rest_framework import serializers
from .models import ResearchPublication
from user.models import User

class ResearchPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPublication
        fields = '__all__'