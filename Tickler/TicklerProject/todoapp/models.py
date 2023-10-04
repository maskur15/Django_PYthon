from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    # Define the choices for the 'gender' field
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # 'gender' field with choices
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    # 'country' field as a CharField
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.username

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
