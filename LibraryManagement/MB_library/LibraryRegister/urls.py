from django.urls import path 
from . import views 
urlpatterns=[
    path('home/',views.showHome),
    path('',views.showMain),
    path('library/',views.showLibrary),
    path('search/<int:bk>/',views.search)
]