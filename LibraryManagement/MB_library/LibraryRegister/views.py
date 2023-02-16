from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
bookList =[
    {'id':1,'author':'wakedi' , 'title':'History of nobel man','rated':True},
    {"id":2 , 'author': 'kathy sierra', 'title': 'java programming','rated':False},
    {'id':3, 'author': 'kenth rosen','title':'discrete mathematics','rated':True}
]
def showHome(request):
    return HttpResponse("THis is our home page")
def showMain(request):
    return render(request,'main.html')
def showLibrary(request):
    return render(request,'LibraryRegister/home.html',context={'booklist':bookList})
def search(request,bk):
    bookObject=None
    for book in bookList:
        if  book['id']==bk:
            bookObject=book
    context={"book":bookObject,'bookKey':bk}
    return render(request,'LibraryRegister/details.html',context)


