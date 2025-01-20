from django.db import models
from communities.models import Community
from users.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Post(models.Model):
    class Status(models.TextChoices):
        PUBLIC = 'PUBLIC'
        PRIVATE = 'PRIVATE'

    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts', null=False)
    like = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    bookmark = models.IntegerField(default=0)
    visibility = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.PUBLIC
    )
    description = models.CharField(max_length=255, null=False)
    attachment = models.FileField(upload_to='attachment/posts', null=True)
    schedule = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.schedule and self.schedule <= now():
            raise ValidationError("Waktu schedule harus lebih dari waktu sekarang.")

    