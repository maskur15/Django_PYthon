# urls.py
from django.urls import path
from .views import register_user, login_user,get_all_users,get_all_books,get_book,add_book,rate_book,get_all_ratings

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('users/',get_all_users,name='get_all_users'),
    path('book/<int:book_id>/',get_book),
    path('books/', get_all_books),
    path('add_book/', add_book),
    path('rate_book/',rate_book),
    path('ratings/',get_all_ratings),
]
