from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView,DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView 

from .models import Task

class CustomLogin(LoginView):
    template_name= 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 
    print('maskur al shal sabil')

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(ListView):
    #this view will return all the tasks in the database 
    model = Task
    context_object_name= 'tasks'

class TaskDetail(DetailView):
    #detail view return the specific item 
    model = Task 
    context_object_name='task'
    template_name='base_app/task.html' # this html file will be looked when this view called 

class TaskCreate(CreateView):
    #this view will look for a html template task_form 
    model= Task 
    fields= '__all__'
    success_url= reverse_lazy('tasks') # after submitting the form 'tasks' url will be called

class TaskUpdate(UpdateView):
    #this view will also look for a html template task_form
    model = Task
    fields= '__all__'
    success_url=reverse_lazy('tasks')

class TaskDelete(DeleteView):
    #this view will look for task_confirm delete html page 
    model = Task
    context_object_name= 'task'
    success_url= reverse_lazy('tasks') #when successfully delete then 'tasks' url will be called 