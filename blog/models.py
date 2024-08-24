from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Ajoute ce champ
    author = models.CharField(max_length=100, default="Anonymous")
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Nouveau champ pour les images

    def __str__(self):
        return self.title
