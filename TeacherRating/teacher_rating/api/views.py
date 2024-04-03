# views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from .serializers import UserWriteSerializer,UserReadSerializer,BookReadSerializer,BookWriteSerializer,CreateRatingSerializer,RatingReadSerializer
from teacher.models import CustomUser,Book,Rating

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserWriteSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated data
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            phone = serializer.validated_data.get('phone')
            password = serializer.validated_data.get('password')

            # Create user object
            user = CustomUser.objects.create_user(name=name, email=email, phone=phone, password=password)

            # Optionally perform additional actions like sending confirmation email
            # ...

            return Response({'message': 'User registered successfully'}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            print(user.name,user.phone)
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response({'token': token.key},status=status.HTTP_200_OK)
           
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    """
    Retrieve all users from the database.
    """
    print("Request headers:", request.headers)

    users = CustomUser.objects.all()
    serializer = UserReadSerializer(users, many=True)
    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
            serializer = BookWriteSerializer(data=book_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookReadSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookReadSerializer(book)
        
        # Add the average rating to the serializer data
        serializer_data = serializer.data
        serializer_data['average_rating'] = book.average_rating
        
        return Response(serializer_data)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)
#only login user can rate the book 
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def rate_book(request):
#     # Extract user_id, book_id, and user_rating from request data
#     user_id = request.data.get('user_id')
#     book_id = request.data.get('book_id')
#     user_rating=request.data.get('user_rating')
#     print(user_id,book_id,user_rating)
#     # Check if user_id, book_id, and user_rating are provided
#     if not (user_id and book_id and user_rating):
#         return Response({"error": "user_id, book_id, and user_rating are required"}, status=status.HTTP_400_BAD_REQUEST)

#     # Check if the user and book exist in the database
#     try:
#         user = CustomUser.objects.get(id=user_id)
#         book = Book.objects.get(id=book_id)
#     except CustomUser.DoesNotExist:
#         return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#     except Book.DoesNotExist:
#         return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

#     # Validate the rating value
#     if not (0 <= user_rating <= 5):
#         return Response({"error": "Invalid rating value. Must be between 0 and 5"}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         rating = Rating.objects.get(user_id=user_id,book_id=book_id)
#     except Rating.DoesNotExist:
#         rating = None
#     if rating:
#          # If rating exists, update the existing rating
#         serializer = CreateRatingSerializer(rating, data={'user_rating': user_rating}, partial=True)
#     else:
#         # Create the Rating object with primary key values for user and book
#         serializer = CreateRatingSerializer(data={'user': user_id, 'book': book_id, 'user_rating': user_rating})

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_book(request):
    # Extract book_id and user_rating from request data
    book_id = int(request.data.get('book_id'))
    user_rating = float(request.data.get('user_rating'))
    print(type(book_id),type(user_rating))
    # Check if book_id and user_rating are provided
    if not (book_id and user_rating):
        return Response({"error": "book_id and user_rating are required"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the book exists in the database
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    # Validate the rating value
    if not (0 <= user_rating <= 5):
        return Response({"error": "Invalid rating value. Must be between 0 and 5"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if a rating already exists for the user and book
    existing_rating = Rating.objects.filter(user=request.user, book=book).first()
    if existing_rating:
        # If rating exists, update the existing rating
        serializer = CreateRatingSerializer(existing_rating, data={'user_rating': user_rating}, partial=True)
    else:
        # Create a new Rating object
        serializer = CreateRatingSerializer(data={'user': request.user.id, 'book': book_id, 'user_rating': user_rating})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_all_ratings(request):
    ratings = Rating.objects.all()
    serializer = RatingReadSerializer(ratings, many=True)
    return Response(serializer.data)