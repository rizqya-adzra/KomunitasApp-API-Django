from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/icon', null=True)

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.icon