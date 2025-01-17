from django.db import models
from users.models import User
from communities.models import Community

class Role(models.Model):
    class Status(models.TextChoices):
        ADMIN = 'ADMIN'
        MEMBER = 'MEMBER'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles', null=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='roles', null=False)
    role = models.CharField(
        max_length=6,
        choices=Status.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

