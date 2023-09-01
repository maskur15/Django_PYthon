from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
# Create your views here.
from .models import Todo
def getTodoList(request):
    tasks = Todo.objects.all()
    context = {'todoList':tasks}
    return render(request,'todos/todo_list.html',context=context)
def insert(request:HttpRequest):
    task = request.POST['content']
    todo_object = Todo(content=task)
    todo_object.save()
    return redirect('/todos/list_all')
def delete_item(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    return redirect('/todos/list_all/')

def update_item(request,item_id):
    todoList  = Todo.objects.all().exclude(id=item_id)
    item= Todo.objects.get(id=item_id)
    context = {'item':item,'todoList':todoList}
    if request.method=='POST':
        item.content= request.POST['task_description']
        item.save()
        return redirect('/todos/list_all/')
    return render(request,'todos/edit_form.html',context=context)