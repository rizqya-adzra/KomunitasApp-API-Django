from django.db import models
from posts.models import Post
from users.models import User

class Bookmark(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookmarks', null=False )
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks', null=False )
    bookmark = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    