from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginUser,name='home'),
    path('register/', views.registration_view, name='register'),
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),

    path('logout/',views.logoutUser,name='logout'),
    path('create/',views.createTask,name='createTask'),
]
