from django.db import models
from user.models import User

class ResearchPublication(models.Model):
     # Opciones para el campo `status`
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('open', 'Open for Collaboration'),
        ('closed', 'Closed for Collaboration'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    # Opciones para el campo `category`
    CATEGORY_CHOICES = [
        ('architecture', 'Architecture'),
        ('industrial_design', 'Industrial Design'),
        ('graphic_design', 'Graphic Design'),
        ('urban_promotion', 'Urban Promotion'),
    ]
    
    title = models.CharField(max_length=255, blank=False)
    abstract = models.TextField(max_length= 500,blank=False)
    content = models.TextField(blank=False)
    date_published = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20 ,choices=STATUS_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')