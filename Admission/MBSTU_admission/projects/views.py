from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

bookList=[
    {
    'id':1, 'title':'Java programming',
    'author':'kathy siera',
    'rated': True
    },
    {
     'id':2, 'title':'C++ programming',
     'author': 'danitch riche',
     'rated':False
    },
    {
     'id':3 ,'title':'python programming',
      'author': 'Maskur al shal sabil',
      'rated': False
    }
]
def showHome(request):
    name='Maskur al'
    age=18  
    context = {'student':name,'age':age,'booklist':bookList}
    return render(request,'projects/home.html',context)

def reviewBook(request,pk):
    bookObject = None 
    for i in bookList:
        if i['id']==int(pk):
            bookObject=i 
    return render(request,'projects/single-project.html',{'book':bookObject})
