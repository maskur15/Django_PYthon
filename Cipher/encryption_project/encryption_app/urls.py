from django.urls import path
from . import views
urlpatterns = [
    path('',views.showHome,name='home'),
    path('encrypt_image/',views.cipherImage,name='encrypt_image'),
    path('encrypt_stegano/',views.encrypt_stegano,name='encrypt_stegano'),
    path('decrypt_text/',views.decryptText,name='decryptText')

]
