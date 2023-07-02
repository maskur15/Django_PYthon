
from django.urls import path
from project_app import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.show_main,name='main'),
    path('home/',views.show_home,name='home'),

]