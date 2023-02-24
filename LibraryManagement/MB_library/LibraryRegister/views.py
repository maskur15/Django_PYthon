from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from .models import Book
bookList =[
    {'id':1,'author':'wakedi' , 'title':'History of nobel man','rated':True},
    {"id":2 , 'author': 'kathy sierra', 'title': 'java programming','rated':False},
    {'id':3, 'author': 'kenth rosen','title':'discrete mathematics','rated':True}
]
def showHome(request):
    return HttpResponse("THis is our home page")
def showMain(request):
    books= Book.objects.all()
    context={'books':books}
    return render(request,'LibraryRegister/home.html',context)


def search(request,bk):
    bookObject= Book.objects.get(id=bk)
    context={"book":bookObject,'bookKey':bk}
    return render(request,'LibraryRegister/details.html',context)


