from django.urls import path 
from . import views

urlpatterns = [
    path('',views.showHome,name='home'),
    path('main/',views.showMain),
]
