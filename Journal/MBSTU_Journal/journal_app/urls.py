from django.urls import path 
from . import views

urlpatterns = [
    path('',views.showHome,name='home'),
    path('main/',views.showMain),
    path('paper/<str:paperid>/',views.singlePaper,name='singlepaper'),
    path('update-paper<str:paperid>/',views.updatePaper,name='updatepaper')
]
