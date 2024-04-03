from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(AbstractUser):
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.email

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


from django.db import models
from django.db.models import Avg

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    book_rating = models.CharField(max_length=10)  # Assuming it stores 'good' or 'bad'
    release_date = models.DateField()

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        return self.rating_set.aggregate(Avg('user_rating'))['user_rating__avg']



class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_rating = models.FloatField()
    
    def __str__(self):
        return f"Rating {self.id} - {self.user.name} - {self.book.name} ({self.user_rating})"
