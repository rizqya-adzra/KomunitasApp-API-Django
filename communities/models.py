from django.core.exceptions import ValidationError
from django.db import models
from categories.models import Category
from users.models import User
from roles.models import Role

class Community(models.Model):
    class Status(models.TextChoices):
        PUBLIC = 'PUBLIC'
        PRIVATE = 'PRIVATE'

    UNLIMITED = None 

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='communities', null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/communities', null=True)
    visibility = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.PUBLIC,
    )
    members = models.ManyToManyField(User, through=Role, related_name='joined_communities') 
    max_members = models.IntegerField(null=True, blank=True, default=UNLIMITED)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.description or 'No description'}"