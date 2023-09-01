from django.urls import path
from . import views
urlpatterns = [
    path('list_all/', views.getTodoList ),
    path('insert_todo/',views.insert,name='insert_todo_item'),
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
    path('update/<int:item_id>/',views.update_item,name='update_item'),
]
