from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .forms import SignUpForm ,AddRecordForm
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()
    try:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST["password"]
            user = authenticate(request=request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,'You have been logged in ')
                return redirect('home')
            else:
                messages.success(request,'Enter correct username & password')
                return redirect('home')
    except Exception:
        pass
    print(records)
    return render(request,'home.html',{'records':records})
def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request,'You have been loggged out ')
    return redirect('home')
    pass 
def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        print(request.POST)
        if form.is_valid():
           
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
    
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'you have successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})

    return render(request,'register.html',{'form':form})

def customer_record(request,pk):
    #shows individual customer record 
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request,'record.html',{'record':record})
    else:
        messages.success(request,'You must be logged in to view this page ')
        return redirect('home')
        
    pass
def delete_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request,'Customer deleted successfully')
        return redirect('home')
    else:
        messages.success(request,'You must be logged in to delete')
        return redirect('home')
def add_record(request):
    if request.user.is_authenticated:

        if request.POST:
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Recorded Added')
                return redirect('home')
            else:
                return render(request,'add_record.html',{'form':form})
            
        else:
            form = AddRecordForm()
            return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,'You must be logged in to add record')
        return redirect('home')

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record updated ')
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,'You must be logged in to update record')
        return redirect('home')