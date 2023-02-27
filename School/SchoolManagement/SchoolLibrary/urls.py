from django.urls import path
from .import views

urlpatterns=[
    path('',views.getDate),
    path('create-book/',views.create),
    path('show-book/',views.getBook),
]