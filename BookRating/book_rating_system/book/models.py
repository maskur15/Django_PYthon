from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    book_rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name



class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_rating = models.FloatField()

    def __str__(self):
        return f"Rating {self.id} - {self.user.name} - {self.book.name} ({self.user_rating})"
