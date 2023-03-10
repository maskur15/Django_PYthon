from django.urls import path
from .import views

urlpatterns=[
    path('',views.showHome),
    path('create-book/',views.create),
    path('show-book/',views.getBook),
]