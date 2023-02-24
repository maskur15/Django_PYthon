from django.shortcuts import render,redirect
from django.http import HttpResponse 
# Create your views here.
from . models import Projects
from .forms import ProjectForm

def projects(request):
    projects=Projects.objects.all()
    print(projects)
    context={'projects':projects}
    return render(request,'projects/home.html',context)
def showHome(request):
    name='Maskur al'
    age=18  
    context = {'student':name,'age':age,'booklist':bookList}
    return render(request,'projects/home.html',context)

def getProject(request,pk):
    projectObject= Projects.objects.get(id=pk)
    tags= projectObject.tags.all()
    reviews= projectObject.review.all()
    context= {'reviews':reviews,'project':projectObject,'tags':tags}
    return render(request,'projects/single-project.html',context)

def createProject(request):
   form=ProjectForm()

   if request.method =='POST':
       print('Form data ',request.POST)
   # storing the data in the database one way 
    #    title = request.POST['title']
    #    Projects.objects.create(
    #        title=title,
    #    ) 
       form = ProjectForm(request.POST)
       
       if form.is_valid:
         form.save()
         return redirect('project')

   context={'form':form}
   return render(request,'projects/project-form.html',context )

def updateProject(request,pk):
    project = Projects.objects.get(id=pk)

    form = ProjectForm(instance=project)
    if request.method =='POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form': form}
    return render(request,'projects/project-form.html',context)

def deleteProject(request,pk):
    project = Projects.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('project')
    return render(request,'projects/delete.html',{'object':project})

