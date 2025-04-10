from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
