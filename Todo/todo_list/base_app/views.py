from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView,DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin 

from .models import Task

class CustomLogin(LoginView):
    template_name= 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 
    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin,ListView):
    #this view will return all the tasks in the database 
    model = Task
    context_object_name= 'tasks'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    #detail view return the specific item 
    model = Task 
    context_object_name='task'
    template_name='base_app/task.html' # this html file will be looked when this view called 

class TaskCreate(LoginRequiredMixin,CreateView):
    #this view will look for a html template task_form 
    model= Task 
    fields= ['title','description','complete']
    success_url= reverse_lazy('tasks') # after submitting the form 'tasks' url will be called

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user 
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    #this view will also look for a html template task_form
    model = Task
    fields= '__all__'
    success_url=reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    #this view will look for task_confirm delete html page 
    model = Task
    context_object_name= 'task'
    success_url= reverse_lazy('tasks') #when successfully delete then 'tasks' url will be called 