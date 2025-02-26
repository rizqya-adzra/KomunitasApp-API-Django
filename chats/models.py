from django.db import models
from communities.models import Community 
from users.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats', null=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='chats', null=False)
    description = models.CharField(max_length=500)
    attachment = models.FileField(upload_to='attachment/chats', null=True)
    image = models.FileField(upload_to='attachment/chats', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)