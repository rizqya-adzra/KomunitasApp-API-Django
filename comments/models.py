from django.db import models
from posts.models import Post
# from users.models import User

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=False )
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
