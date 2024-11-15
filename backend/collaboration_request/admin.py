from django.contrib import admin
from .models import CollaborationRequest

@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'date_sent', 'applicant', 'research_publication')