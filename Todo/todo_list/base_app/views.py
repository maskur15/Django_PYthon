from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.detail import DetailView

class TaskList(ListView):
    model = Task
    context_object_name= 'tasks'

class TaskDetail(DetailView):
    #detail view return the specific item 
    model = Task 
    context_object_name='task'
    template_name='base_app/task.html'