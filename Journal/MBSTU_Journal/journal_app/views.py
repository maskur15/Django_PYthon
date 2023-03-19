from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.http import HttpResponse 
from . models import Papers
from .forms import paperForm

def showHome(request):
    paperlist = Papers.objects.all()

    print(paperlist)
    context = {'papers':paperlist,}
    return render(request,'journal_app/home.html',context=context)
def showMain(request):
    return render(request,'main.html')
def singlePaper(request,paperid):
    paperobj = Papers.objects.get(id=paperid)
    tags = paperobj.tags.all()
    context = {'paper':paperobj,'tags':tags }
    return render(request,'journal_app/single-paper.html',context)

def updatePaper(request,paperid):
    paper = Papers.objects.get(id=paperid)
    form = paperForm(instance=paper)
    if request.method =="POST":
        form = paperForm(request.POST,request.FILES,instance=paper)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'journal_app/paper-form.html',context)