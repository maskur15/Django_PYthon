from django.urls import path 
from . import views

urlpatterns = [
    path('',views.showHome,name='home'),
    path('main/',views.showMain),
    path('paper/<str:paperid>/',views.singlePaper,name='singlepaper'),
    path('create-paper/',views.createPaper,name='createpaper'),
    path('update-paper<str:paperid>/',views.updatePaper,name='updatepaper'),
    path('delete-paper/<str:paperid>/',views.deletePaper,name='deletepaper'),
]
