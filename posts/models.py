from django.db import models

# Create your models here.
from django.db import models
from communities.models import Community
from users.models import User
# from users.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Post(models.Model):
    class Status(models.TextChoices):
        PUBLIC = 'PUBLIC'
        PRIVATE = 'PRIVATE'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts', null=False)
    # like = models.IntegerField(default=0)
    # comment = models.IntegerField(default=0)
    # bookmark = models.IntegerField(default=0)
    visibility = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.PUBLIC
    )
    description = models.CharField(max_length=255, null=False)
    attachment = models.FileField(upload_to='attachment/posts', null=True)
    image = models.ImageField(upload_to='attachment/posts/image', null=True)
    schedule = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# class Attachment(models.Model):
#     post = models.ForeignKey(Post, related_name='attachments', on_delete=models.CASCADE)
#     file = models.FileField(upload_to='attachment/posts', null=True)
#     image = models.ImageField(upload_to='attachment/posts/image', null=True)