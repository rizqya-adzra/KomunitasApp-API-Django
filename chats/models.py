from django.db import models
from communities.models import Community 

class Chat(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='chats', null=False)
    description = models.CharField(max_length=500)
    attachment = models.FileField(upload_to='attachment/chats', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)