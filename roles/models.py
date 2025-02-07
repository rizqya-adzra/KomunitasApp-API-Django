from django.db import models
from users.models import User

class Role(models.Model):
    class ROLE_CHOICES(models.TextChoices):
        ADMIN = 'ADMIN'
        MEMBER = 'MEMBER'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles', null=False)
    community = models.ForeignKey('communities.Community', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=6,
        choices=ROLE_CHOICES.choices,
        default='MEMBER'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'community')

