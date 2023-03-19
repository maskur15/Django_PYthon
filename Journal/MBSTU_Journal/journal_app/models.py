from django.db import models

# Create your models here.
import uuid 
class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) -> str:
        return self.name
    
class Papers(models.Model):
    #owner 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    author = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True,blank=True)

    demo_link = models.CharField(max_length=1000,null=True,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.title)
    @property
    def imageUrl(self):
        try:
            img = self.featured_image.url
        except:
            img=''
        return img 
class Review(models.Model):
    #owner
    Vote_type=(('up','up'),('down','down'))

    project = models.ForeignKey(Papers,on_delete=models.CASCADE,null=True,blank=True,related_name='review')
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=50,choices=Vote_type)
    updated=models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self) -> str:
        return str(self.value)
