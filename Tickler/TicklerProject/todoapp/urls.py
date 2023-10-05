from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView,name='home'),
    path('register/', views.registration_view, name='register'),
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('create/',views.createTask,name='create_task'),
    path('update/<int:item_id>/',views.updateTask,name='update_item'),
    path('delete/<int:item_id>/',views.deleteTask,name='delete_item'),
]
