# api/urls.py
from django.urls import path
from .views import create_user, get_user,get_all_users, get_all_books,add_book, rate_book

urlpatterns = [
    path('user/', create_user),
    path('users/', get_all_users),
    path('user/<int:user_id>/', get_user),
    path('books/', get_all_books),
    path('books/add/', add_book),
    path('rate/', rate_book),

]
