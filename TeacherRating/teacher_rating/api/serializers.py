# serializers.py
from rest_framework import serializers
from teacher.models import CustomUser,Book,Rating

class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'phone','password']

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:    
        model = CustomUser
        fields = ['name', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}
class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        exclude=['id']
class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'book_rating', 'release_date']
class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['id']

class RatingReadSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=CustomUser.objects.all(), required=True)
    class Meta:
        model = Rating
        fields = ['id', 'user_id', 'book', 'user_rating']