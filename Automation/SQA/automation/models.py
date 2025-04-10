from django.db import models

# Create your models here.
# models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # You can add any additional fields here if needed
    # For now, it uses the default fields: username, email, and password
    pass
from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()  # Replaces the plain TextField
    tags = models.CharField(max_length=100, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Unit(models.Model):
    unit_title = models.CharField(max_length=200)
    unit_description = models.TextField()
    unit_image = models.ImageField(upload_to='unit_images/', blank=True, null=True)

    def __str__(self):
        return self.unit_title
    
class Lesson(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()  # This will store TinyMCE's HTML output
    def __str__(self):
        return self.title