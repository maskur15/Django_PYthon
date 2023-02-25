from django.urls import path 
from . import views 
urlpatterns=[
    path('home/',views.showHome),
    path('',views.showMain,name='home'),
    path('search/<str:bk>/',views.search,name='search'),
    path('create-book/',views.createBook,name='create-book'),
    path('update-book/<str:bookKey>/',views.updateBook,name='update-book'),
    path('delete-book/<str:bookKey>/', views.deleteBook, name='delete-book'),

]