# api/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from django.contrib.auth.models import User
from book.models import Book, Rating,User
from .serializers import UserSerializer,CreateUserSerializer, BookSerializer, RatingSerializer
from rest_framework import status

@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['GET'])
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    

@api_view(['GET'])
def get_all_users(request):
    print("API GET request received for all users.")  # Print debug message

    try:
        users = User.objects.all()
        print(users)
        serializer = UserSerializer(users, many=True)
        print("Serialized data:", serializer.data)  # Print serialized data
        return Response(serializer.data)
    except Exception as e:
        print("Error occurred:", str(e))  # Print error message
        return Response({"error": "An error occurred"}, status=500)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def rate_book(request):
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
