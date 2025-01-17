from django.db import models
from communities.models import Community

class Post(models.Model):
    class Status(models.TextChoices):
        PUBLIC = 'PUBLIC'
        PRIVATE = 'PRIVATE'

    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='communities', null=False)
    # like = models.ForeignKey(Like, on_delete=models.CASCADE, related_name='communities', null=True)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='communities', null=True)
    # bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, related_name='communities', null=True)
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

    