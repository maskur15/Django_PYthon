# api/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from django.contrib.auth.models import User
from book.models import Book, Rating,User
from .serializers import UserSerializer,CreateUserSerializer,CreateBookSerializer, BookSerializer,CreateRatingSerializer, RatingSerializer
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
def get_book(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
# @api_view(['POST'])
# def add_book(request):
#     if request.method == 'POST':
#         serializer = CreateBookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        # Extract book data from request
        book_data = request.data

        # Check if a book with the same name already exists
        existing_book = Book.objects.filter(name=book_data['name']).first()

        if existing_book:
            # If the book already exists, return a custom message
            return Response({"message": "Book already exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If the book does not exist, create a new book entry
            serializer = CreateBookSerializer(data=book_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def rate_book(request):
    # Extract user_id, book_id, and user_rating from request data
    user_id = request.data.get('user_id')
    book_id = request.data.get('book_id')
    user_rating=request.data.get('user_rating')
    print(user_id,book_id,user_rating)
    # Check if user_id, book_id, and user_rating are provided
    if not (user_id and book_id and user_rating):
        return Response({"error": "user_id, book_id, and user_rating are required"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the user and book exist in the database
    try:
        user = User.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    # Validate the rating value
    if not (0 <= user_rating <= 5):
        return Response({"error": "Invalid rating value. Must be between 0 and 5"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        rating = Rating.objects.get(user_id=user_id,book_id=book_id)
    except Rating.DoesNotExist:
        rating = None
    if rating:
         # If rating exists, update the existing rating
        serializer = CreateRatingSerializer(rating, data={'user_rating': user_rating}, partial=True)
    else:
        # Create the Rating object with primary key values for user and book
        serializer = CreateRatingSerializer(data={'user': user_id, 'book': book_id, 'user_rating': user_rating})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_all_ratings(request):
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

    
