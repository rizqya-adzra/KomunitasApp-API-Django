from django.db import models
from posts.models import Post
from users.models import User

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', null=False)
    like = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
