from django.urls import path 
from . import views 
urlpatterns=[
    path('home/',views.showHome),
    path('',views.showMain),

    path('search/<str:bk>/',views.search,name='search')
]