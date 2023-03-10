from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Book
from .forms import BookForm
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
    tags = bookObject.tags.all()
    context={"book":bookObject,'bookKey':bk,'tags':tags}
    return render(request,'LibraryRegister/details.html',context)
def createBook(request):
    form = BookForm()
    if request.method=='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        print('form data ',request.POST)
    context={'form':form}
    return render(request,'LibraryRegister/book-form.html',context)
def updateBook(request,bookKey):
    book = Book.objects.get(id=bookKey)
    form = BookForm(instance=book)

    if request.method=='POST':
        form = BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'LibraryRegister/book-form.html',context)
def deleteBook(request,bookKey):
    book= Book.objects.get(id=bookKey)
    if request.method=='POST':
        book.delete()
        return  redirect('home')
    return render(request,'LibraryRegister/book-delete.html',{'book':book})
