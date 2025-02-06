from django.db import models
from posts.models import Post
from users.models import User
from communities.models import Community

class Notification(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='notifications', null=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='notifications', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', null=True)
    notification = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification
