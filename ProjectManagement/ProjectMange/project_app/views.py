from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls home .")
def index(request):
    return HttpResponse("Hello, world. You're at the polls INDEX.")
def class_based(request):
    return HttpResponse("Hello, world. You're at the polls ClassBased.")

def show_main(request):
    return render(request,'main.html')
def show_home(request):
    return render(request,'project_app/home.html')