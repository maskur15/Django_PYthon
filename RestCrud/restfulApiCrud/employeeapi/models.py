from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_code= models.CharField(max_length=5)
    mobile = models.CharField(max_length=15)
    #CREATE- POST, Retrive-GET, Update-PUT, Delete-DELETE
