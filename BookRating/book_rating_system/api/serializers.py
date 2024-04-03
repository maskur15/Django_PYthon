# api/serializers.py
from rest_framework import serializers
#from django.contrib.auth.models import User
from book.models import Book, Rating,User

#this for create a user wehere id is auto generated
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id','username']
    
#this serializer for response where id should sent 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'password', 'email']
class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        exclude=['id']
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'book_rating', 'release_date']

class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['id']

class RatingSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), required=True)
    class Meta:
        model = Rating
        fields = ['id', 'user_id', 'book', 'user_rating']
