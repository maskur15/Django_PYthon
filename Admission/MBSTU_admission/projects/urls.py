from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.showHome),
    path('query/<int:pk>/',views.reviewBook)


    ]