from django.db import models
from django.utils import timezone
import uuid

class APIKey(models.Model):
    key = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
    
