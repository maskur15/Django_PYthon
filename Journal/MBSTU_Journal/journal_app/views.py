from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponse 
from . models import Papers
def showHome(request):
    paperlist = Papers.objects.all()
    print(paperlist)
    context = {'papers':paperlist}
    return render(request,'journal_app/home.html',context=context)
def showMain(request):
    return render(request,'main.html')