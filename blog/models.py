
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField()  # Add this field

    def __str__(self):
        return self.title

    def is_published(self):
        return self.publish_date is not None and self.publish_date <= timezone.now()
class UserExperience(models.Model):
    name = models.CharField(max_length=100)
    song = models.CharField(max_length=200)

    def __str__(self):
        return self.name