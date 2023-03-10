from django.db import models
import  uuid
# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200,null=True,blank=True)
    description= models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True)
    demo_link= models.CharField(max_length=100,null=True,blank=True)
    source_link= models.CharField(max_length=100,null=True,blank=True)
    vote_total= models.IntegerField(default=0)
    vote_ratio= models.FloatField(default=0)
    tags= models.ManyToManyField('Tag',blank=True)
    created= models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
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
    vote_type= (('up','up'),('down','down'))
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True,blank=True,related_name='review')
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=vote_type)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return str(self.value)
class Tag(models.Model):
    name= models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self) -> str:
        return str(self.name)
