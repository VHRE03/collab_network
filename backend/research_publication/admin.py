from django.contrib import admin
from .models import ResearchPublication

@admin.register(ResearchPublication)
class ResearchPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'status', 'category', 'author')