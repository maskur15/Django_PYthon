from django.contrib import admin

# Register your models here.
from . models import Papers,Review,Tag
admin.site.register(Papers)
admin.site.register(Tag)