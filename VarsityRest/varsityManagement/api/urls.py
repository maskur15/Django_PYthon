from django.urls import path
from . import views 
urlpatterns = [
    path('students/',views.getData),
    path('add/',views.addItem),
    path('get/<int:id>',views.getItem),
    path('update/<int:id>',views.putItem),
    path('delete/<int:id>',views.deleteItem),

]