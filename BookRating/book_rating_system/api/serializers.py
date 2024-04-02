# api/serializers.py
from rest_framework import serializers
#from django.contrib.auth.models import User
from book.models import Book, Rating,User

#this for create a user wehere id is auto generated
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id']
#this serializer for response where id should sent 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'password', 'email']
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'book_rating', 'release_date']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'book', 'user_rating']
