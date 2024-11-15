from django.db import models
from user.models import User
from research_publication.models import ResearchPublication

class CollaborationRequest(models.Model):
    # Opciones para el campo `status`
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
        ('in_review', 'In Review'),
    ]

    message = models.TextField(blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_sent = models.DateField(auto_now_add=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collaboration_requests')
    research_publication = models.ForeignKey(ResearchPublication, on_delete=models.CASCADE, related_name='collaboration_requests')