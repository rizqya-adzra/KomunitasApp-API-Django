from django.core.exceptions import ValidationError
from django.db import models
from categories.models import Category

class Community(models.Model):
    class Status(models.TextChoices):
        PUBLIC = 'PUBLIC'
        PRIVATE = 'PRIVATE'

    UNLIMITED = None 

    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='communities', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='communities', null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='images/communities', null=True)
    visibility = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.PUBLIC,
    )
    members = models.IntegerField(default=0) 
    max_members = models.IntegerField(null=True, blank=True, default=UNLIMITED)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.description or 'No description'}"

    def clean(self):
        if self.max_members is not None and self.members > self.max_members:
            raise ValidationError(
                f"Jumlah member ({self.members}), dan sudah mencapai batas maksimum ({self.max_members})."
            )
        
    def is_unlimited(self):
        return self.max_members is None
