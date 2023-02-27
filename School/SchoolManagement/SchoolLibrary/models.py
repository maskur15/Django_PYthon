from django.db import models

# Create your models here.


class Book(models.Model):
    title= models.CharField(max_length=110)
    author=models.CharField(max_length=111)
    book_link=models.CharField(max_length=100,null=True,blank=True)
    quantity= models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.title)
