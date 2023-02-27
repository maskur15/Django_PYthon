from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
from .models import Book 
def getDate(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def create(request):
    book= Book(title='The golden hour ',author='Maskur')
    book.save()
    html = "<html><body> %s book saved </body></html>" %book  
    return HttpResponse(html)
def getBook(request):
    book= str(Book.objects.all())
    print(book)
    return HttpResponse('type is:',str(type(book)))