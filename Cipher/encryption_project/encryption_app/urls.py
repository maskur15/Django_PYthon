from django.urls import path
from . import views
urlpatterns = [
    path('',views.showHome,name='home'),
    path('encrypt_image/',views.encrypt_image,name='encrypt_image'),
    path('encrypt_stegano/',views.encrypt_stegano,name='encrypt_stegano'),

]
